from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.permissions import IsUser
from apps.user.serializers.wallet import WalletBalanceSerializer


class BalanceView(APIView):
    """View for user balance."""

    permission_classes = [IsAuthenticated, IsUser]

    @swagger_auto_schema(tags=['Wallet'])
    def get(self, request):
        """Return a currency list balance user."""
        try:
            user = request.user
            balance = user.wallets.balances.all()
            data = WalletBalanceSerializer(balance, many=True).data
            return Response(status=status.HTTP_200_OK, data={"Message": data})
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
