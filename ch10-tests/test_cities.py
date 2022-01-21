import unittest
import city_functions


class CityTestCase(unittest.TestCase):
    def test_format_city(self):
        formatted_city = city_functions.format_city("victoria", "canada")

        self.assertEqual(formatted_city, "Victoria, Canada")

    def test_format_city_population(self):
        formatted_city = city_functions.format_city("santiago", "chile", population=5000000)
        self.assertEqual(formatted_city, "Santiago, Chile - population 5000000")


if __name__ == "__main__":
    unittest.main()
