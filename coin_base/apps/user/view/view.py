from apps.user.serializers import UserSerializer, UserPasswordSerializer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
    """View for editing user password."""
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['User'])
    def patch(self, request):
        """Return a list of all users."""
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
