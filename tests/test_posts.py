import allure
import pytest
import logging
from assertpy import assert_that
from utils.api_config import APIClient

client = APIClient()

def test_get_posts():
    res = client.get("/posts")
    res_body = res.json()


    #Assertions
    with allure.step("Assert status code"):
       assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
       logging.info(f"Request send successfully. status code is {res.status_code}")

    with allure.step("Assert count of list"):
        assert len(res_body) == 100, f"Assert failed. length of posts = {len(res_body)}."
        logging.info(f"Assert passed. length of posts = {len(res_body)}.")

    with allure.step("Assert first post"):
        assert_that(res_body[0]).is_not_empty()
        assert_that(res_body[0]).contains_key('id')
        assert_that(res_body[0]['id']).is_equal_to(1)
        logging.info(f"Assert passed. First user is {res_body[0]}")