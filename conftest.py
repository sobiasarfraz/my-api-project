from h11 import InformationalResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging
from selenium.webdriver.chrome.options import Options
import tempfile
import os


@pytest.fixture(scope="class")
def setup(request):
    user_data_dir = tempfile.mkdtemp()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

    # Cleanup: remove the temporary user data directory after the test
    if os.path.exists(user_data_dir):
        os.rmdir(user_data_dir)


def setlog():
    logging.basicConfig(
        filename = 'test.log',
        level = logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s',
        filemode = 'a'

    )
setlog()