import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utilities import ReadConfigurations
import time


@pytest.fixture()
def set_up_tear_down(request):
    browser = ReadConfigurations.read_Configurations("basic information", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("Provide browser name")
    driver.maximize_window()
    app_url = ReadConfigurations.read_Configurations("basic information", "url")
    driver.get(app_url)
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver

    # quit
    driver.quit()
