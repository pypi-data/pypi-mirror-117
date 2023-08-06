from selenium import webdriver


def visit_main_page():
    """
    Visit the main page and clicks on the "latest earthquakes" element

    Returns
    -------
    Driver (remote control interface)
    """
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get("https://earthquake.usgs.gov/")

    page = driver.find_element_by_xpath(
        "/html/body/main/div/div/div[2]/div[2]/ul[1]/li/a")
    page.click()

    latest_earthquakes = driver.find_element_by_xpath(
        "/html/body/div[6]/div/div/div/div/div[2]/div/nav/div/div/ul/li[2]/ul/li[1]/a")
    latest_earthquakes.click()

    return driver
