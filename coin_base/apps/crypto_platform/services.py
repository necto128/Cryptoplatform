from apps.coin.models import Directive
from apps.crypto_platform.models import OrderBook, Order
from apps.crypto_platform.models import Transaction
from apps.user.models import WalletBalance


class WorkingOrder:
    """WorkingOrder services."""

    def __init__(self, data, user):
        """WorkingOrder services initialization."""
        self.user = user
        self.id_currency = data["currency"]
        self.order_type = data["order_type"]
        self.amount = data["amount"]
        self.currency = None
        self.main_currency = None
        self.last_price = None
        self.user_balance = None
        self.price_amount_currency = None
        self.purchased_crypt = None
        self.user_wallet = None
        self.amount_currency = None
        self.currency = None
        self.usdt = None
        self.working_currency = None
        self.order = None

    def calculating_difference(self):
        """Get calculating difference."""
        self.working_currency.balance -= self.amount_currency
        self.usdt.balance += self.amount_currency * self.last_price
        self.working_currency.save()
        self.usdt.save()

    def main_block(self):
        """Block get wallet and user."""
        self.user_wallet = self.user.wallets
        self.main_currency = self.user_wallet.balances.filter(currency__key__in=[self.id_currency, 825])
        self.usdt = self.main_currency.filter(currency__key=825).first()
        self.working_currency = self.main_currency.filter(currency__key=self.id_currency).first()
        if self.working_currency is None:
            WalletBalance.objects.create(wallet=self.user_wallet, currency=self.currency, balance=0)
        self.amount_currency = self.amount

    def purchased_crypto(self):
        """Get purchased crypto."""
        if self.purchased_crypt is None:
            WalletBalance.objects.create(
                wallet=self.user_wallet,
                currency=self.currency,
                balance=self.amount
            )
        else:
            self.purchased_crypt.balance += self.amount
            self.purchased_crypt.save()

    def get_currency(self):
        """Get currency price."""
        self.currency = Directive.objects.get(key=self.id_currency)
        self.last_price = self.currency.price_history.latest('timestamp').value

    def get_wallet(self):
        """Block get wallet user."""
        self.user_wallet = self.user.wallets
        self.user_balance = self.user_wallet.balances.get(currency__symbol="USDT")
        self.price_amount_currency = self.amount * self.last_price

    def user_block(self):
        """Block user."""
        self.user_balance.balance -= self.price_amount_currency
        self.user_balance.save()
        self.purchased_crypt = self.user_wallet.balances.filter(currency__key=self.id_currency).first()

    def order_block(self):
        """Block order."""
        order_book = OrderBook.objects.get(currency=self.currency)
        self.order = Order.objects.create(
            order_type=self.order_type,
            currency=order_book.currency.symbol,
            wallet=self.user_wallet,
            amount=self.amount,
            price=self.last_price,
            status="close"
        )
        order_book.orders.add(self.order)

    def buy_transaction_block(self):
        """Transaction order."""
        Transaction.objects.create(
            buy_order=self.order,
            price=self.order.price,
            amount=self.amount
        )

    def sell_transaction_block(self):
        """Transaction order."""
        Transaction.objects.create(
            sell_order=self.order,
            price=self.order.price,
            amount=self.amount
        )
