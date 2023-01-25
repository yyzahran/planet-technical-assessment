import pytest
import json
from requests.auth import HTTPBasicAuth
from constants import PL_API_KEY as API_KEY

from modules.APIHelper import APIHelper


class TestCreateSavedSearch():

    SAVED_SEARCH_BASE_URL = "https://api.planet.com/data/v1/searches"
    auth = HTTPBasicAuth(API_KEY, '')

    @pytest.fixture
    def json_data(self):
        with open('TestFiles/ExampleBody.json', 'r') as f:
            data = json.load(f)
        return data

    def test_create_saved_search_without_auth(self, json_data):
        """Tests creating a saved search with proper authentication"""
        res = APIHelper.create_saved_search(self, json=json_data)
        print(res.json())
        assert res.json()['message'] == 'Please enter a valid API key.'
        assert res.status_code == 401

    def test_create_saved_search_with_auth(self, json_data):
        """Tests authentication is needed to create a saved search"""
        res = APIHelper.create_saved_search(self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 200

    def test_create_saved_search_without_name_returns_error(self, json_data):
        """Tests creating a saved search without the name field returns an error
        as this field is required"""
        json_data.pop('name')
        res = APIHelper.create_saved_search(self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_create_saved_search_without_item_types_returns_error(self, json_data):
        """Tests creating a saved search without the item_types field returns an error
        as this field is required"""
        json_data.pop('item_types')
        res = APIHelper.create_saved_search(self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_create_saved_search_without_filter_returns_error(self, json_data):
        """Tests creating a saved search without the filter field returns an error
        as this field is required"""
        json_data.pop('filter')
        res = APIHelper.create_saved_search(self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_create_saved_search_without_request_body_returns_error(self):
        """Tests creating a saved search rqueires a request body"""
        res = APIHelper.create_saved_search(self, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_create_saved_search_without_asset_types_is_ok(self, json_data):
        """Tests creating a saved search without the asset_types field is ok
        as this field is not required"""
        json_data.pop('asset_types')
        res = APIHelper.create_saved_search(self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 200

    def test_create_saved_search_without_daily_email_enabled_is_ok(self, json_data):
        """Tests creating a saved search without the __daily_email_enabled field is ok
        as this field is not required. Default value is false"""
        json_data.pop('__daily_email_enabled')
        res = APIHelper.create_saved_search(self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.json()['__daily_email_enabled'] == False
        assert res.status_code == 200
