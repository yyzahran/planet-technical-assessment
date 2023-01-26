import pytest
import json
from requests.auth import HTTPBasicAuth
from constants import PL_API_KEY as API_KEY

from modules.APIHelper import APIHelper
from tests.test_base import TestBase
auth = HTTPBasicAuth(API_KEY, '')


@pytest.fixture
def json_data():
    with open('TestFiles/ExampleBody.json', 'r') as f:
        data = json.load(f)
        return data
