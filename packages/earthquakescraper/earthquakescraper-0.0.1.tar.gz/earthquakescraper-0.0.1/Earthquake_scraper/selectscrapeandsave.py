from Earthquake_scraper.visit_main_page import visit_main_page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import pandas as pd


class SelectScrapeandSave:

    def __init__(self):
        self.driver = visit_main_page()

    def selection_settings(self):
        """
        Selects the desired options step-by-step (e.g region of interest, start datetime and time zone).

        Returns
        -------
        Driver (remote control interface)
        """
        options = self.driver.find_element_by_xpath(
            "/html/body/usgs-root/usgs-header/header/usgs-panel-chooser/nav/i[3]")
        options.click()

        earthquake_catalog = self.driver.find_element_by_xpath(
            "/html/body/usgs-root/div/usgs-settings/section/usgs-earthquakes-filter/a")
        earthquake_catalog.click()

        custom_selection = self.driver.find_element_by_xpath(
            "/html/body/main/div/form/section/div[2]/section/ul[1]/li[3]/label")
        custom_selection.click()

        start_datetime = self.driver.find_element_by_xpath(
            "/html/body/main/div/form/section/div[2]/section/ul[2]/li[1]/input")
        start_datetime.click()
        start_datetime.clear()
        start_datetime.send_keys(input("Datetime:"))
        start_datetime.send_keys(Keys.RETURN)
        time.sleep(1)

        search = self.driver.find_element_by_xpath(
            "/html/body/main/div/form/footer/button")
        search.click()

        time.sleep(1)

        options = self.driver.find_element_by_xpath(
            "/html/body/usgs-root/usgs-header/header/usgs-panel-chooser/nav/i[3]")
        options.click()

        time_zone = self.driver.find_element_by_xpath(
            "/html/body/usgs-root/div/usgs-settings/section/usgs-time-zone/mat-radio-group/mat-list/mat-list-item[2]/div/mat-radio-button")
        time_zone.click()
        time.sleep(3)

        return self.driver

    def scrapeandsave(self):
        """
        This function creates an empty dictionary in which the data will be stored.
        It iterates through the results of an infinitely loading page extracting the text from the elements of interest (Magnitude, Place
        Datetime and Depth).
        It created a pandas dataframe from the populated dictionary and saves it in a .csv file
        after checking if that file already exists.

        Returns
        -------
        Message
        """
        data = {"Magnitude": [], "Place": [], "Datetime": [], "Depth": []}
        iter = 0

        # The number of iterations depends on the amount of results. The number 400 was chosen to accommodate the iteration through 15500 results (approximately).
        while iter < 400:
            list_eq = self.driver.find_element_by_xpath(
                '//mat-list[@class="mat-list mat-list-base ng-star-inserted"]')
            earthquakes = list_eq.find_elements_by_xpath('./mat-list-item')
            for earth in earthquakes:
                data["Magnitude"].append(
                    earth.find_element_by_tag_name("span").text)
                data["Place"].append(earth.find_element_by_tag_name("h6").text)
                data["Datetime"].append(
                    earth.find_element_by_class_name("time").text)
                data["Depth"].append(earth.find_element_by_xpath(
                    ".//div[2]/div/aside/span").text)
            iter += 1
            ActionChains(self.driver).move_to_element(earthquakes[-1]).perform()
            time.sleep(1)

        df = pd.DataFrame.from_dict(data)

        # Looks for the df.csv file and if it finds it, the new results are appended and if the file does not exist it is created with the scraping results.
        if os.path.isfile('df.csv'):
            # Removes duplicates bsaed on the pair of Place and Datetime.
            df = df.drop_duplicates(subset=["Place", "Datetime"])
            df.to_csv('df.csv', mode='a', header=False)
            return f'Your file has been saved successfully!'
        else:
            df = df.drop_duplicates(subset=["Place", "Datetime"])
            df.to_csv('df.csv', mode='a', header=True)
            return f'Your file has been saved successfully!'
