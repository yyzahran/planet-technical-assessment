import pytest
import json
from modules.APIHelper import APIHelper
from test_base import TestBase


class TestUpdateSavedSearch(TestBase):

    @pytest.fixture
    def new_saved_search(self, json_data):
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        response = res.json()
        return response

    def update_field(self, hash_map, search_id, key, new_value=None):
        """Helper function to update the request body and sends a put request to udpate
        the saved search"""
        hash_map[key] = new_value
        updated_saved_search = APIHelper.update_saved_search(
            self, json=hash_map, search_id=search_id, auth=self.auth)
        return updated_saved_search

    def test_udpate_saved_search_without_auth_returns_error(self, new_saved_search, json_data):
        """Tests authorization is required to update a saved search"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")
        saved_search = APIHelper.get_saved_search(
            self, search_id=id, auth=self.auth)
        assert saved_search.status_code == 200

        updated_saved_search = APIHelper.update_saved_search(
            self, json=json_data, search_id=id)
        assert updated_saved_search.status_code == 401

    def test_update_name_field(self, new_saved_search, json_data):
        """Tests updating name field of an already-existing saved search"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")
        saved_search = APIHelper.get_saved_search(
            self, search_id=id, auth=self.auth)
        assert saved_search.status_code == 200

        new_value="Updated saved search name"
        updated_saved_search = self.update_field(hash_map=json_data, search_id=id, key='name',
                                            new_value=new_value)
        ##
        # new_value = 'Updated saved search name'
        # updated_json_body = json_data
        # updated_json_body['name'] = new_value
        # print(f"Updated saved search \n{updated_json_body}")

        # updated_saved_search = APIHelper.update_saved_search(
        #     self, json=json_data, search_id=id, auth=self.auth)
        ##
        assert updated_saved_search.status_code == 200
        assert updated_saved_search.json(
        )['name'] == new_value, f"Field was not updated, expected {new_value}, instead found {updated_saved_search['name']}."

    def test_update_daily_email_enabled_field(self, new_saved_search, json_data):
        """Tests updating __daily_email_enabled field of an already-existing saved search"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")
        saved_search = APIHelper.get_saved_search(
            self, search_id=id, auth=self.auth)
        assert saved_search.status_code == 200

        new_value = False
        updated_saved_search = self.update_field(hash_map=json_data, search_id=id, key='__daily_email_enabled',
                                            new_value=new_value)
        #
        # updated_json_body = json_data
        # updated_json_body['__daily_email_enabled'] = new_value
        # print(f"Updated saved search \n{updated_json_body}")

        # updated_saved_search = APIHelper.update_saved_search(
        #     self, json=json_data, search_id=id, auth=self.auth)
        #

        assert updated_saved_search.status_code == 200
        assert updated_saved_search.json()['__daily_email_enabled'] == new_value, \
            f"Field was not updated, expected {new_value}, instead found {updated_saved_search['__daily_email_enabled']}."

    def test_update_filter_field(self, new_saved_search, json_data):
        """Tests updating filter field of an already-existing saved search"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")

        new_value = {
            "type": "AndFilter",
            "config": [
                {
                    "type": "AssetFilter",
                    "config": [
                        "analytic_sr"
                    ]
                },
                {
                    "type": "AssetFilter",
                    "config": [
                        "udm2"
                    ]
                }
            ]
        }
        updated_saved_search = self.update_field(hash_map=json_data, search_id=id, key='filter',
                                            new_value=new_value)
        # updated_json_body = json_data
        # updated_json_body['filter'] = new_value
        # print(f"Updated saved search \n{updated_json_body}")

        # updated_saved_search = APIHelper.update_saved_search(
        #     self, json=json_data, search_id=id, auth=self.auth)
        assert updated_saved_search.status_code == 200
        assert updated_saved_search.json()['filter'] == new_value, \
            f"Field was not updated, expected {new_value}, instead found {updated_saved_search['filter']}."

    def test_update_asset_types_field(self, new_saved_search, json_data):
        """Tests updating asset_types field of an already-existing saved search"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")
        saved_search = APIHelper.get_saved_search(
            self, search_id=id, auth=self.auth)
        assert saved_search.status_code == 200

        new_value = ["ortho_analytic_8b_xml", "ortho_udm2", "ortho_visual"]
        updated_saved_search = self.update_field(hash_map=json_data, search_id=id, key='asset_types',
                                            new_value=new_value)
        # updated_json_body = json_data
        # updated_json_body['asset_types'] = new_value
        # print(f"Updated saved search \n{updated_json_body}")

        # updated_saved_search = APIHelper.update_saved_search(
        #     self, json=json_data, search_id=id, auth=self.auth)
        assert updated_saved_search.json()['asset_types'] == new_value, \
            f"Field was not updated, expected {new_value}, instead found {updated_saved_search['asset_types']}."
        assert updated_saved_search.status_code == 200

    def test_update_name_field_with_invalid_value_returns_error(self, new_saved_search, json_data):
        """Tests updating name field of an already-existing saved search
        with an invalid value returns error"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")
        saved_search = APIHelper.get_saved_search(
            self, search_id=id, auth=self.auth)
        assert saved_search.status_code == 200

        new_value = ["New name in a list"]
        updated_saved_search = self.update_field(hash_map=json_data, search_id=id, key='name',
                                            new_value=new_value)
        # updated_json_body = json_data
        # updated_json_body['name'] = new_value
        # print(f"Updated saved search \n{updated_json_body}")

        # updated_saved_search = APIHelper.update_saved_search(
        #     self, json=json_data, search_id=id, auth=self.auth)
        assert updated_saved_search.status_code == 400

    def test_update_daily_email_enabled_field_with_invalid_value_returns_error(self, new_saved_search, json_data):
        """Tests updating __daily_email_enabled field of an already-existing saved search
        with an invalid value returns error"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")
        saved_search = APIHelper.get_saved_search(
            self, search_id=id, auth=self.auth)
        assert saved_search.status_code == 200

        new_value = "False"
        updated_saved_search = self.update_field(hash_map=json_data, search_id=id, key='__daily_email_enabled',
                                            new_value=new_value)
        # updated_json_body = json_data
        # updated_json_body['__daily_email_enabled'] = new_value
        # print(f"Updated saved search \n{updated_json_body}")

        # updated_saved_search = APIHelper.update_saved_search(
        #     self, json=json_data, search_id=id, auth=self.auth)
        assert updated_saved_search.status_code == 400

    def test_update_filter_field_with_an_invalid_value_returns_error(self, new_saved_search, json_data):
        """Tests updating filter field of an already-existing saved search
        with an invalid value returns error"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")

        new_value = {"filter": "filter_value"}
        updated_saved_search = self.update_field(hash_map=json_data, search_id=id, key='filter',
                                            new_value=new_value)

        # updated_json_body = json_data
        # updated_json_body['filter'] = new_value
        # print(f"Updated saved search \n{updated_json_body}")

        # updated_saved_search = APIHelper.update_saved_search(
        #     self, json=json_data, search_id=id, auth=self.auth)
        assert updated_saved_search.status_code == 400

    def test_update_asset_types_field_with_an_invalid_value_returns_error(self, new_saved_search, json_data):
        """Tests updating asset_types field of an already-existing saved search
        with an invalid value returns error"""
        id = new_saved_search['id']
        print(f"Search id is {id}")
        print(f"Current saved search \n{new_saved_search}")
        saved_search = APIHelper.get_saved_search(
            self, search_id=id, auth=self.auth)
        assert saved_search.status_code == 200

        new_value = ["asset_type_1", "asset_type_3", "asset_type_5"]
        updated_saved_search = self.update_field(hash_map=json_data, search_id=id, key='asset_types',
                                            new_value=new_value)
        # updated_json_body = json_data
        # updated_json_body['asset_types'] = new_value
        # print(f"Updated saved search \n{updated_json_body}")

        # updated_saved_search = APIHelper.update_saved_search(
        #     self, json=json_data, search_id=id, auth=self.auth)
        assert updated_saved_search.status_code == 400
