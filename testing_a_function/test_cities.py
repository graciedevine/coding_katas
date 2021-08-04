import unittest
from city_functions import get_city_name


class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""


    def test_city_country(self):
        formatted_city = get_city_name("bangkok", "thailand")
        self.assertEqual(formatted_city, "Bangkok Thailand")


if __name__ == "__main__":
    unittest.main()
