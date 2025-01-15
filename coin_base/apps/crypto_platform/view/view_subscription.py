from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.crypto_platform.serializers.subscription import SubscriptionSerializer, CreateSubscriptionSerializer


class SubscriptionDirectiveView(APIView):
    """View for Subscription Directive."""
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['Subscription'],
        operation_description="Subscription on directive",
        operation_summary="Subscription on directive"
    )
    def post(self, request):
        """Create subscription on directive."""
        data, user = request.data, request.user
        serializer = CreateSubscriptionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user.subscriptions.create_subscribe(serializer.data)
        return Response(
            status=status.HTTP_201_CREATED,
            data={"Message": "Successfully subscription!"}
        )

    @swagger_auto_schema(
        tags=['Subscription'],
        operation_description="Delete subscription directive",
        operation_summary="Delete subscription directive"
    )
    def delete(self, request):
        """Delete subscription on directive."""
        data, user = request.data, request.user
        serializer = SubscriptionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user.subscriptions.unsubscribe(serializer.data)
        return Response(
            status=status.HTTP_200_OK,
            data={"Message": "Successfully unsubscription!"}
        )

    @swagger_auto_schema(
        tags=['Subscription'],
        operation_description="Get subscription ",
        operation_summary="Get subscription"
    )
    def get(self, request):
        """Create subscription on directive."""
        user = request.user
        list_subscriptions = user.subscriptions.get_subscriptions()
        directives = [sub.directive for sub in list_subscriptions]
        serializer = SubscriptionSerializer(directives, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={"data": serializer.data}
        )
