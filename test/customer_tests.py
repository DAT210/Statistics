import unittest
import requests
from flask import Flask

from src import app, customer_functions


class TestCustomerMethods(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)

        app.config["TEST"] = True
        self.app = app.run()

    #GET METHODS
    def test_get_customer_success(self):
        response = self.app.get("127.0.0.1:5000/statistics/customers/1")
        self.assertEqual(200, response.status)

    def test_get_customer_fail(self):
        response = self.app.get("127.0.0.1:5000/statistics/customers/1000000")
        self.assertEqual(404, response.status)
    
    def test_get_all_succeed(self):
        response = self.app.get("127.0.0.1:5000/statistics/customers")
        self.assertEqual(200, response.status)

    def test_get_customer_name(self):
        response = requests.get("127.0.0.1:5000/statistics/customers/1")
        print(response)
        self.assertEqual("Connie", response.text)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCustomerMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)