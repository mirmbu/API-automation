import pytest
from utils.api_config import APIClient


def pytest_addoption(parser):
    parser.addoption(
        "--post-id",
        action="store",
        required=True,
        help="Post ID to retrieve comments for",
    )

@pytest.fixture()
def api_base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture()
def client(api_base_url):
    return APIClient(api_base_url)


@pytest.fixture()
def post_id(request):
    return int(request.config.getoption("--post-id"))