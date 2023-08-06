from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .visit_main_page import visit_main_page

import time


def selection_settings():
    """
    Selects the desired options step-by-step (e.g region of interest, start datetime and time zone).

    Returns
    -------
    Driver (remote control interface)
    """
    driver = visit_main_page()
    options = driver.find_element_by_xpath(
        "/html/body/usgs-root/usgs-header/header/usgs-panel-chooser/nav/i[3]")
    options.click()

    earthquake_catalog = driver.find_element_by_xpath(
        "/html/body/usgs-root/div/usgs-settings/section/usgs-earthquakes-filter/a")
    earthquake_catalog.click()

    custom_selection = driver.find_element_by_xpath(
        "/html/body/main/div/form/section/div[2]/section/ul[1]/li[3]/label")
    custom_selection.click()

    start_datetime = driver.find_element_by_xpath(
        "/html/body/main/div/form/section/div[2]/section/ul[2]/li[1]/input")
    start_datetime.click()
    start_datetime.clear()
    start_datetime.send_keys(input("Datetime:"))
    start_datetime.send_keys(Keys.RETURN)
    time.sleep(1)

    search = driver.find_element_by_xpath(
        "/html/body/main/div/form/footer/button")
    search.click()

    time.sleep(1)

    options = driver.find_element_by_xpath(
        "/html/body/usgs-root/usgs-header/header/usgs-panel-chooser/nav/i[3]")
    options.click()

    time_zone = driver.find_element_by_xpath(
        "/html/body/usgs-root/div/usgs-settings/section/usgs-time-zone/mat-radio-group/mat-list/mat-list-item[2]/div/mat-radio-button")
    time_zone.click()
    time.sleep(3)

    return driver
