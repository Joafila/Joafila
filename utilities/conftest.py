import pytest
from selenium import webdriver


from utilities.test_data import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
        request.cls.driver = driver
        print("Browser: ", request.param)
        driver.get(TestData.URL)
        driver.maximize_window()
        yield
        print("close driver")
        driver.close()

