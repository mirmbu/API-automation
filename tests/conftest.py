import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--post-id",
        action="store",
        required=True,
        help="Post ID to retrieve comments for",
    )



@pytest.fixture()
def post_id(request):
    return int(request.config.getoption("--post-id"))