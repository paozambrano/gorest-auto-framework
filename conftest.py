import pytest
from apis.user_api import UserApi
from utils.data_gen import DataGenerator

@pytest.fixture
def user_api():
    return UserApi()

@pytest.fixture
def random_user_payload():
    return DataGenerator.generate_user_data()