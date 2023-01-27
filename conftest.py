import pytest
import json


@pytest.fixture
def json_data():
    with open('TestFiles/ExampleBody1.json', 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture
def reponse_schema():
    schema = {
        "type": "object",
        "required": ["created", "filter", "id", "last_executed", "name", "updated"],
        "properties": {
            "__daily_email_enabled": {"type": "boolean"},
            "_links": {"type": "object"},
            "asset_types": {"type": "array"},
            "created": {"type": "string"},
            "filter": {"type": "object"},
            "id": {"type": "string"},
            "item_types": {"type": "array"},
            "last_executed": {"type": "null"},
            "name": {"type": "string"},
            "search_type": {"type": "string"},
            "updated": {"type": "string"},
        },
    }
    return schema


class ValueStorage():
    saved_search = None
