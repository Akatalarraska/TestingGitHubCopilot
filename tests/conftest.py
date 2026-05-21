from fastapi.testclient import TestClient
import copy
import src.app as app_module
import pytest

_original_activities = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_state():
    # Restore in-memory activities before each test
    app_module.activities = copy.deepcopy(_original_activities)
    yield
    app_module.activities = copy.deepcopy(_original_activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)
