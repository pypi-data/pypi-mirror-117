# Full test suite for product and shopping cart
import unittest
import numpy as np
import pandas as pd
from Earthquake_scraper.selection_settings import selection_settings
from Earthquake_scraper.selectscrapeandsave import SelectScrapeandSave


class SelectScrapeandSaveTestCase(unittest.TestCase):
    def test_selection_settings(self):

        actual_value = 'https://earthquake.usgs.gov/earthquakes/map/?extent=-87.54007,40.78125&extent=87.50971,319.21875&range=search&timeZone=utc&settings=true&search=%7B%22name%22:%22Search%20Results%22,%22params%22:%7B%22starttime%22:%222021-01-01%2000:00:00%22,%22endtime%22:%222021-08-25%2023:59:59%22,%22minmagnitude%22:2.5,%22orderby%22:%22time%22%7D%7D'
        driver = selection_settings()
        expected_value = driver.current_url

        self.assertEqual(actual_value, expected_value)  # <6>

    def test_scrapeandsave(self):

        data = pd.read_csv('df.csv')
        self.assertEqual(len(data), 15424)

        test_message = f'Your file has been saved successfully!'
        actual_message = SelectScrapeandSave()
        self.assertEqual(test_message, actual_message)
