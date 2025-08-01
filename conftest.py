from h11 import InformationalResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Adding WebDriverWait to the driver for explicit waits
    driver.wait = WebDriverWait(driver, 10)  # waits up to 10 seconds

    request.cls.driver = driver  # 🔥 makes self.driver work inside class
    yield
    driver.quit()


def setlog():
    logging.basicConfig(
        filename = 'test.log',
        level = logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s',
        filemode = 'a'

    )
setlog()