import unittest
from Earthquake_scraper.visit_main_page import visit_main_page


class VisitMainPageTestCase(unittest.TestCase):  # <1>
    def test_visit_main_page(self):
        actual_value = 'https://earthquake.usgs.gov/earthquakes/map/?extent=14.0087,-126.47461&extent=56.65623,-63.54492'
        driver = visit_main_page()
        expected_value = driver.current_url

        self.assertEqual(actual_value, expected_value)  # <6>
