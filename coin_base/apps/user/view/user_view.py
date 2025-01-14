from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers.user import UserSerializer, UserPasswordSerializer
from apps.user.tasks import send_password_reset_email_celery_task
from apps.utils import generate_password
from apps.utils import ping_celery_redis
from config.celery import app


class RegisterView(APIView):
    """View for user registration."""
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['User'])
    def post(self, request):
        """Return a list of all users."""
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user_instance = User(**user.validated_data)
        user_instance.set_password(user.validated_data['password'])
        user_instance.save()
        return Response(status=status.HTTP_201_CREATED, data={"Message": "Successfully registered!"})


class EditPasswordView(APIView):
    """Views for editing user password."""
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['User'])
    def patch(self, request):
        """View for editing user password."""
        password = UserPasswordSerializer(data=request.data)
        password.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(request.data["current_password"]):
            return Response({"Error": "The current password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            validate_password(request.data["password"], user=user)
        except ValidationError as e:
            return Response({"Error": e}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(request.data["password"])
        user.save()
        return Response(status=status.HTTP_201_CREATED, data={"Message": "Successfully registered!"})


class DropPasswordView(APIView):
    """Views for drop user password."""
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['User'])
    def post(self, request):
        """Views for drop user password."""
        user = request.user
        ping_celery_redis(app)
        passw = generate_password()
        if not user.check_password(passw):
            send_password_reset_email_celery_task.delay(user.id, passw)
            User.objects.filter(id=user.id).update(password=make_password(passw))
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
