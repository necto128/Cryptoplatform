from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.coin.models import Directive
from apps.crypto_platform.serializers.subscription import SubscriptionSerializer


class RecommendationsView(APIView):
    """View for Subscription Directive."""
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        tags=['Recommendations'],
        operation_description="Get recommendations crypto",
        operation_summary="Get recommendations crypto"
    )
    def get(self, request):
        """Get recommendations crypto."""
        list_directive = Directive.objects.filter(is_active=True).order_by('-price24h')[:3]
        serializer = SubscriptionSerializer(list_directive, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={"data": serializer.data}
        )
