import pandas as pd

from apps.coin.models import Directive
from apps.crypto_platform.models import OrderBook


def create_record():
    """Load data from a CSV file and create or update records in the Directive model."""
    df = pd.read_csv('src/generators/crypto_base.csv')
    active_records = df[df['active']]
    for row in active_records.itertuples(index=True):
        order_book, created = OrderBook.objects.get_or_create(
            currency=Directive.objects.get_or_create(
                key=row.key,
                symbol=row.symbol,
                name=row.name,
            )[0]
        )
        if not created:
            break
    print("Successfully created records!!!")
