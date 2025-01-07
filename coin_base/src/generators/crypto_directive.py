import pandas as pd
from apps.coin.models import Directive


def create_record():
    """Loads data from a CSV file and creates or updates records in the Directive model."""
    df = pd.read_csv('src/generators/crypto_base.csv')
    active_records = df[df['active'] == True]
    for row in active_records.itertuples(index=True):
        Directive.objects.get_or_create(
            key=row.key,
            symbol=row.symbol,
            name=row.name,
        )
