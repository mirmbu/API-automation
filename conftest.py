import pytest
from utils.api_config import APIClient


def pytest_addoption(parser):
    parser.addoption(
        "--id",
        action="store",
        required=True,
        help="ID to retrieve comments for",
    )

@pytest.fixture()
def api_base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture()
def client(api_base_url):
    return APIClient(api_base_url)


@pytest.fixture()
def id(request):
    return int(request.config.getoption("--id"))