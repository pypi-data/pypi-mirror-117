from persianBrokers.base_broker import BaseBroker


class Mofid(BaseBroker):
    def buy(self, isin, order_count, order_price, timeout=None):
        url = "https://api.cl3.mofid.dev/easy/api/OmsOrder"

        payload = {
            "isin": isin,
            "financeId": 1,
            "quantity": order_count,
            "price": order_price,
            "side": 0,
            "validityType": 74,
            "validityDateJalali": "1400/6/3",
            "easySource": 1,
            "referenceKey": "8f1751c3-9a84-40c9-ab4a-69ce51b1f453",
            "cautionAgreementSelected": False
        }
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json',
        }

        self.request(side='buy', url=url, payload=payload, headers=headers, timeout=timeout)

    def sell(self, isin, order_count, order_price, timeout=None):
        url = "https://api.cl3.mofid.dev/easy/api/OmsOrder"

        payload = {
            "isin": isin,
            "financeId": 1,
            "quantity": order_count,
            "price": order_price,
            "side": 1,
            "validityType": 74,
            "validityDateJalali": "1400/6/3",
            "easySource": 1,
            "referenceKey": "8f1751c3-9a84-40c9-ab4a-69ce51b1f453",
            "cautionAgreementSelected": False
        }
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json',
        }
        self.request(side='sell', url=url, payload=payload, headers=headers, timeout=timeout)

    def parse_response(self, response: dict) -> bool:
        return response.get('isSuccessfull', False)
