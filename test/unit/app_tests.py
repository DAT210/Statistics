import unittest
import requests

class TestAPIMethods(unittest.TestCase):
    def test_root_path(self):        
        info = requests.get("http://127.0.0.1:5000/statistics/")
        self.assertEqual(200, info.status_code)
    
    def test_chart_path(self):
        info = requests.get("http://127.0.0.1:5000/statistics/charts")
        self.assertEqual(200, info.status_code)
    
    def test_tables_path(self):        
        info = requests.get("http://127.0.0.1:5000/statistics/tables/")
        self.assertEqual(200, info.status_code)
   
    def test_customer_path(self):        
        info = requests.get("http://127.0.0.1:5000/statistics/customers/")
        self.assertEqual(200, info.status_code)

    def test_customer_info_path(self):
        info = requests.get("http://127.0.0.1:5000/statistics/customers/1")
        self.assertEqual(200, info.status_code)

        info = requests.get("http://127.0.0.1:5000/statistics/customers/9999")
        self.assertEqual(500, info.status_code)
    
    def test_dish_path(self):        
        info = requests.get("http://127.0.0.1:5000/statistics/dish/")
        self.assertEqual(200, info.status_code)
    
    def test_dish_info_path(self):
        info = requests.get("http://127.0.0.1:5000/statistics/dish/1")
        self.assertEqual(200, info.status_code)

        info = requests.get("http://127.0.0.1:5000/statistics/dish/99999")
        self.assertEqual(500, info.status_code)

    def test_order_path(self):        
        info = requests.get("http://127.0.0.1:5000/statistics/orders/")
        self.assertEqual(200, info.status_code)
    
    def test_order_info_path(self):
        info = requests.get("http://127.0.0.1:5000/statistics/orders/1")
        self.assertEqual(200, info.status_code)

        info = requests.get("http://127.0.0.1:5000/statistics/orders/66666")
        self.assertEqual(500, info.status_code)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAPIMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)