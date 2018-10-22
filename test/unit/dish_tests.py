import unittest
import requests
from flask import Flask

from src import app, dish_functions

class TestDishMethods(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)

        app.config["TEST"] = True
        self.app = app.run()

    #GET METHODS
    def test_get_dish_success(self):
        response = self.app.get("127.0.0.1:5000/statistics/dish/1")
        self.assertEqual(200, response.status)

    def test_get_dish_fail(self):
        response = self.app.get("127.0.0.1:5000/statistics/dish/100")
        self.assertEqual(404, response.status)
    
    def test_get_all_succeed(self):
        response = self.app.get("127.0.0.1:5000/statistics/dish")
        self.assertEqual(200, response.status)

    def test_get_dish_name(self):
        response = requests.get("127.0.0.1:5000/statistics/dish/3")
        print(response)
        self.assertEqual("Ribeye", response.text)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDishMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)