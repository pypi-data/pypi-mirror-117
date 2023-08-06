import unittest
from kollet.kollet import Kollet

class TestKollet(unittest.TestCase):
    def test_add_token(self): 
        self.client = Kollet(api_key="")

    def test_get_currencies(self):
        currencies = self.client.get_currencies()
        self.assertTrue(currencies["success"])

    def test_create_address(self):
        address = self.client.create_address('btc', 'kollet')
        self.assertTrue(address["success"])

    def test_get_balance(self):
        balance = self.client.get_balance("btc")
        self.assertTrue(balance["success"])

    def test_estimate_network_fee(self):        
        estimate_network_fee = self.client.estimate_network_fee("0.000536", "btc", "FASTEST")
        self.assertTrue(estimate_network_fee["success"])

    def test_send_coins(self):        
        send_coins = self.client.send_coins("0.000536", "btc", "FASTEST", "RECIPIENT_ADDRESS")
        self.assertTrue(send_coins["success"])

if __name__ == '__main__':
    unittest.main()