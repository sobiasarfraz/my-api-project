from h11 import InformationalResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()



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