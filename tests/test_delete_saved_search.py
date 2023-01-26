import pytest
import json

from modules.APIHelper import APIHelper
from test_base import TestBase


class TestDeleteSavedSearch(TestBase):

    @pytest.fixture
    def new_saved_search(self, json_data):
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        response = res.json()
        return response

    def test_delete_saved_search(self, new_saved_search):
        """Tests deleting a saved search and the seach is not existent anymore"""
        id = new_saved_search['id']
        res = APIHelper.delete_saved_search(self, search_id=id, auth=self.auth)
        assert res.status_code == 204

        get_saved_search = APIHelper.get_saved_search(self, search_id=id, auth=self.auth)
        assert get_saved_search.status_code == 404

    def test_delete_non_existent_saved_search(self, new_saved_search):
        """Tests deleteing a saved search with incorrect id"""
        id = new_saved_search['id'][::-1]
        res = APIHelper.delete_saved_search(self, search_id=id, auth=self.auth)
        assert res.status_code == 404
