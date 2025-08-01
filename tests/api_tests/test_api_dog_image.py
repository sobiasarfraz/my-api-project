import requests
import pytest
import logging

logger = logging.getLogger()

@pytest.fixture()
def test_url():
    try:
        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url, timeout=4)
        #assert response.status_code == 200, "url not valid"
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"error happend: {e}")
        pytest.fail(f"an error accoured: {e}")

    else:
        data = response.json()
        return data

@pytest.mark.usefixtures("test_url")
class Testdog:

    def test_info(self, test_url):
        assert test_url["status"] == "success", f"invalid key :{test_url['status']}, it should be 'success' "
        assert test_url["message"].startswith("https"), " url not stat with http"
        logger.info("successfulyy fetch data , and tests are clear")


