import pytest
import json
from requests.auth import HTTPBasicAuth
from constants import PL_API_KEY as API_KEY

from modules.APIHelper import APIHelper


class TestDeleteSavedSearch():

    SAVED_SEARCH_BASE_URL = "https://api.planet.com/data/v1/searches/"
    auth = HTTPBasicAuth(API_KEY, '')

    @pytest.fixture
    def json_data(self):
        with open('TestFiles/ExampleBody.json', 'r') as f:
            data = json.load(f)
        return data

    @pytest.fixture
    def saved_search(self, json_data):
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        response = res.json()
        return response

    def test_delete_saved_search(self, saved_search):
        """Tests deleting a saved search"""
        id = saved_search['id']
        res = APIHelper.delete_saved_search(self, search_id=id, auth=self.auth)
        assert res.status_code == 204

    def test_delete_non_existent_saved_search(self, saved_search):
        """Tests deleteing a saved search with incorrect id"""
        id = saved_search['id'][::-1]
        res = APIHelper.delete_saved_search(self, search_id=id, auth=self.auth)
        assert res.status_code == 404
