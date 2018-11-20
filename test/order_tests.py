import unittest
import requests
from flask import Flask

from src import app, order_functions


class TestOrderMethods(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)

        app.config["TEST"] = True
        self.app = app.run()

    #GET METHODS
    def test_get_order_success(self):
        response = self.app.get("127.0.0.1:5000/statistics/orders/1")
        self.assertEqual(200, response.status)

    def test_get_order_fail(self):
        response = self.app.get("127.0.0.1:5000/statistics/orders/1000")
        self.assertEqual(404, response.status)
    
    def test_get_all_succeed(self):
        response = self.app.get("127.0.0.1:5000/statistics/orders")
        self.assertEqual(200, response.status)

    def test_get_order_name(self):
        response = requests.get("127.0.0.1:5000/statistics/orders/1")
        print(response)
        self.assertEqual("inhouse", response.text) #Delivery method

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOrderMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)