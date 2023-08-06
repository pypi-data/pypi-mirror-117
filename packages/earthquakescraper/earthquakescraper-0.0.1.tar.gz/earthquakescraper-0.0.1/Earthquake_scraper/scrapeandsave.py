from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import pandas as pd


def scrapeandsave():
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
        list_eq = driver.find_element_by_xpath(
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
        ActionChains(driver).move_to_element(earthquakes[-1]).perform()
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
