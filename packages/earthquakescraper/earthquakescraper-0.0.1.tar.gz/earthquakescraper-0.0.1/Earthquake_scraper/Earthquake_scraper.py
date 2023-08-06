import time

import Earthquake_scraper
from .visit_main_page import visit_main_page
from .selection_settings import selection_settings
from .scrapeandsave import scrapeandsave
from .upload_file import upload_file


time.sleep(1)
driver = visit_main_page()
time.sleep(1)

# Scraping the data
driver = selection_settings()
time.sleep(3)

scrapeandsave()

upload_file('df.csv', 'earthquakescraper')
