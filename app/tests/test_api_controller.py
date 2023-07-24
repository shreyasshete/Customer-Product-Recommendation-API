# Importing necessary packages
import json
import unittest
from app.controller.api_controller import app


class TestAPIController(unittest.TestCase):
    def setUp(self):
        # Creating test client for Flask app
        self.app = app.test_client()

    def test_get_recommendations_with_missing_customer_id(self):
        response = self.app.get('/recommendations')

        # Verifing the missing customer ID response case
        self.assertEqual(response.status_code, 400)

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], 'Customer ID is missing')

    def test_get_recommendations_with_valid_customer_id(self):
        response = self.app.get("/recommendations?customer_id=17850")
        # Verifing the success case response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0)

    def test_get_recommendations_with_no_recommendations(self):
        response = self.app.get('/recommendations?customer_id=9999099999998')

        # Verifing the missing customer ID response cases
        self.assertEqual(response.status_code, 400)

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], 'Customer ID 9999099999998 not found')

    def test_get_recommendations_with_invalid_input_type(self):
        response = self.app.get('/recommendations?customer_id=invalid')

        # Verifing the invalid customer ID response cases
        self.assertEqual(response.status_code, 400)

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], "invalid literal for int() with base 10: 'invalid'")

if __name__ == '__main__':
    unittest.main()
