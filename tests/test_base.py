from requests.auth import HTTPBasicAuth
from constants import PL_API_KEY as API_KEY


class TestBase():

    SAVED_SEARCH_BASE_URL = "https://api.planet.com/data/v1/searches"
    auth = HTTPBasicAuth(API_KEY, '')
