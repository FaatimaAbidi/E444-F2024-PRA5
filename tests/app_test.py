from application import application, load_model
import pytest
from pathlib import Path

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    with application.app_context():
        yield application.test_client()

def test_strings(client):
    strings = ["hello%20world","this_is_awesome:)","Joe%20Biden%20won%20the%20election.","ECE444%20has%20a%20final%20this%20year."]
    for index,string in enumerate(strings):
        new_string = "/" + string
        response = client.get(new_string)
        assert response.status_code == 200
        if index < 2:
            assert response.data == b'FAKE'
        if index > 2:
            assert response.data == b'REAL'