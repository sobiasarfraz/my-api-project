import pytest
import requests
import time
import os
import logging

logger = logging.getLogger()

@pytest.mark.usefixtures("setup")
class Test_dogurl:

    def test_calldg(self):
        logger.info("test start")
        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url, timeout=5)
        assert response.status_code == 200, "url not valid"
        logger.info("data is fetched")
        image_url = response.json()["message"]
        # Step 2: Open the image URL in the browser using Selenium
        self.driver.get(image_url)
        time.sleep(4)


        # Step 3: Validate page loaded by checking page title is not empty
        assert self.driver.title != "", " page did not load "

        timestamp = time.strftime("%y%m%d-%H%M%S")
        path = os.path.join("..", "..", "screenshots", f"dog_img{timestamp}.png")
        self.driver.save_screenshot(path)
        logger.info(f"scrennshot is saved in {path}")
        # ✅ Optional: confirm working directory
        logger.info(f"Working directory: {path}")

        assert ".jpg" in self.driver.current_url or ".png" in self.driver.current_url


