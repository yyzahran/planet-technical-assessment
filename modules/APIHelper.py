import requests


class APIHelper():
    def __init__(self):
        self.SAVED_SEARCH_BASE_URL = "https://api.planet.com/data/v1/searches/"

    def create_saved_search(self, json=None, auth=None):
        res = requests.post(url=self.SAVED_SEARCH_BASE_URL,
                            auth=auth, json=json)
        return res

    def get_saved_search(self, search_id="", auth=None):
        assert search_id, "Search id must be provided"
        url = f"{self.SAVED_SEARCH_BASE_URL}/{search_id}"
        res = requests.get(url=url, auth=auth)
        return res

    def update_saved_search(self, json=None, search_id="", auth=None):
        assert search_id, "Search id must be provided"
        url = f"{self.SAVED_SEARCH_BASE_URL}/{search_id}"
        res = requests.put(url=url, auth=auth, search_id=search_id, json=json)
        return res

    def delete_saved_search(self, search_id="", auth=None):
        assert search_id, "Search id must be provided"
        url = f"{self.SAVED_SEARCH_BASE_URL}/{search_id}"
        res = requests.delete(url=url, auth=auth)
        return res