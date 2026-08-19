import allure
import pytest
import logging
from assertpy import assert_that
from numpy.random import logistic

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
        logging.info(f"Assert passed. First post is {res_body[0]}")


def test_get_post_by_id():
    res = client.get(f"/posts/3")
    res_body = res.json()


    #Assersions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step("Assert selected post"):
        assert_that(res_body).is_not_empty()
        assert_that(res_body['id']).is_equal_to(3)
        assert_that(res_body['userId']).is_equal_to(1)
        assert_that(res_body).contains_key('body')
        assert_that(res_body['title']).is_equal_to('ea molestias quasi exercitationem repellat qui ipsa sit aut')
        logging.info(f"Assert passed. selected post is {res_body}")