import pytest
import json

from modules.APIHelper import APIHelper
from test_base import TestBase
from conftest import ValueStorage


class TestEndToEnd(TestBase):

    @pytest.fixture
    def new_request_body(self):
        """Gets new field entries to update saved search"""
        with open('TestFiles/ExampleBody2.json', 'r') as f:
            data = json.load(f)
        return data

    def test_create_saved_search(self, json_data):
        """Creates a saved search"""
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        ValueStorage.id = res.json()['id']
        assert res.status_code == 200

    @pytest.mark.depends(on=['test_create_saved_search'])
    def test_saved_search_is_created(self):
        """Tests saved search created in test_create_saved_search is available"""
        saved_search = APIHelper.get_saved_search(
            self, search_id=ValueStorage.id, auth=self.auth)
        assert saved_search.status_code == 200

    @pytest.mark.depends(on=['test_create_saved_search'])
    def test_update_saved_search(self, new_request_body, json_data):
        """Tests updating multiple fields in saved search created in test_create_saved_search"""
        updated_json_body = new_request_body
        updated_saved_search = APIHelper.update_saved_search(
            self, json=updated_json_body, search_id=ValueStorage.id, auth=self.auth)

        assert updated_saved_search.status_code == 200
        assert updated_json_body['name'] == new_request_body['name']
        assert updated_json_body['filter'] == new_request_body['filter']
        assert updated_json_body['asset_types'] == new_request_body['asset_types']
        assert updated_json_body['__daily_email_enabled'] == new_request_body['__daily_email_enabled']

    @pytest.mark.depends(on=['test_update_saved_search'])
    def test_delete_saved_search(self):
        """Tests deleting saved search created in test_create_saved_search"""
        res = APIHelper.delete_saved_search(self, search_id=ValueStorage.id, auth=self.auth)
        assert res.status_code == 204

        get_saved_search = APIHelper.get_saved_search(self, search_id=ValueStorage.id, auth=self.auth)
        assert get_saved_search.status_code == 404, "Expected saved search to be deleted, instead it was found."
