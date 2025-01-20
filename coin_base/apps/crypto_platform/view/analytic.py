from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.crypto_platform.services import AdministrationWork
from apps.permissions import IsAnalytic


class AnalyticGetOrderCryptView(APIView):
    """Class for the Analytic to get list orders."""

    permission_classes = [IsAuthenticated, IsAnalytic]

    @swagger_auto_schema(
        tags=['Analytic'],
        operation_description="Get list of order",
        operation_summary="Get list of order"
    )
    def get(self, request):
        """View for get list of order."""
        return AdministrationWork.get_list_orders()


class AnalyticGetUserView(APIView):
    """Class for analytic get list user."""

    permission_classes = [IsAuthenticated, IsAnalytic]

    @swagger_auto_schema(
        tags=['Analytic'],
        operation_description="Get list of user",
        operation_summary="Get list of user"
    )
    def get(self, request):
        """View for get list of user."""
        return AdministrationWork.get_list_user()


class AnalyticGetTransactionsView(APIView):
    """Class for analytic get list transactions user."""

    permission_classes = [IsAuthenticated, IsAnalytic]

    @swagger_auto_schema(
        tags=['Analytic'],
        operation_description="Get list of user",
        operation_summary="Get list of user"
    )
    def get(self, request, user_id):
        """View for get list of user."""
        return AdministrationWork.get_list_transactions_user(user_id)
