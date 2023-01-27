import jsonschema
from jsonschema import validate

from modules.APIHelper import APIHelper
from test_base import TestBase


class TestCreateSavedSearch(TestBase):

    def validate_get_response_schema(self, instance, reponse_schema):
        """Helper function to validate the response schema upon
        GET request a created saved search"""
        try:
            validate(instance=instance, schema=reponse_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def test_create_saved_search_without_auth(self, json_data):
        """Tests creating a saved search with proper authentication"""
        res = APIHelper.create_saved_search(self, json=json_data)
        print(res.json())
        assert res.json()['message'] == 'Please enter a valid API key.'
        assert res.status_code == 401

    def test_create_saved_search_with_auth(self, json_data, reponse_schema):
        """Tests authentication is needed to create a saved search"""
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 200

        saved_search = APIHelper.get_saved_search(
            self, search_id=res.json()['id'], auth=self.auth)
        assert saved_search.status_code == 200
        assert self.validate_get_response_schema(
            instance=saved_search.json(), reponse_schema=reponse_schema) == True

    def test_create_saved_search_without_name_returns_error(self, json_data):
        """Tests creating a saved search without the name field returns an error
        as this field is required"""
        json_data.pop('name')
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_create_saved_search_without_item_types_returns_error(self, json_data):
        """Tests creating a saved search without the item_types field returns an error
        as this field is required"""
        json_data.pop('item_types')
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_create_saved_search_without_filter_returns_error(self, json_data):
        """Tests creating a saved search without the filter field returns an error
        as this field is required"""
        json_data.pop('filter')
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_create_saved_search_without_request_body_returns_error(self):
        """Tests creating a saved search rqueires a request body"""
        res = APIHelper.create_saved_search(self, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_create_saved_search_without_asset_types_is_ok(self, json_data, reponse_schema):
        """Tests creating a saved search without the asset_types field is ok
        as this field is not required"""
        json_data.pop('asset_types')
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 200

        saved_search = APIHelper.get_saved_search(
            self, search_id=res.json()['id'], auth=self.auth)
        assert saved_search.status_code == 200
        assert self.validate_get_response_schema(
            instance=saved_search.json(), reponse_schema=reponse_schema) == True

    def test_create_saved_search_without_daily_email_enabled_is_ok(self, json_data, reponse_schema):
        """Tests creating a saved search without the __daily_email_enabled field is ok
        as this field is not required. Default value is false"""
        json_data.pop('__daily_email_enabled')
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.json()['__daily_email_enabled'] == False
        assert res.status_code == 200

        saved_search = APIHelper.get_saved_search(
            self, search_id=res.json()['id'], auth=self.auth)
        assert saved_search.status_code == 200
        assert self.validate_get_response_schema(
            instance=saved_search.json(), reponse_schema=reponse_schema) == True

    def test_name_has_to_be_string(self, json_data):
        """Tests that name field has to be a string"""
        json_data['name'] = 1234
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_daily_email_enabled_has_to_be_boolean(self, json_data):
        """Tests that __daily_email_enabled field has to be a boolean"""
        json_data['__daily_email_enabled'] = "True"
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_asset_types_has_to_be_list(self, json_data):
        """Tests that asset_types field has to be an array"""
        json_data['asset_types'] = "string"
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_asset_types_has_to_be_valid(self, json_data):
        """Tests that asset_types field has to be of valid data"""
        json_data['asset_types'] = [
            "asset_type_1", "asset_type_2", "asset_type_3"]
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_item_types_has_to_be_array(self, json_data):
        """Tests that item_types field has to be an array"""
        json_data['item_types'] = "list"
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400

    def test_filter_has_to_be_object(self, json_data):
        """Tests that filter field has to be of an object"""
        json_data['name'] = ['item 1', 'item 2']
        res = APIHelper.create_saved_search(
            self, json=json_data, auth=self.auth)
        print(res.json())
        assert res.status_code == 400
