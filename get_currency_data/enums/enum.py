import pandas as pd


class WebSocketResource:
    @staticmethod
    def get_id_crypto() -> list:
        df = pd.read_csv('active_directive.csv')
        crypto_id_list = df['id'].tolist()
        return ','.join(map(str, crypto_id_list))

    WS_CRYPTO: str = "wss://push.coinmarketcap.com/ws?device=web&client_source=coin_detail_page"
    message_call_5s_normal = {
        "method": "RSUBSCRIPTION",
        "params": [
            "main-site@crypto_price_5s@{}@normal",
            get_id_crypto()
        ]
    }
