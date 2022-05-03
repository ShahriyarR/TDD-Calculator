import pytest

from src.entrypoints.api.app import app


@pytest.fixture
def get_test_client_with_context():
    with app.app_context():
        with app.test_request_context():
            with app.test_client() as client:
                yield client
