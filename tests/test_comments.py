import allure
import pytest
import logging
from assertpy import assert_that

#GET functions

def test_get_all_comments(client):
    res = client.get("/comments")
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}."
        logging.info(f"Assert passed. Status code is {res.status_code}.")


    with allure.step("Assert length of comments."):
        assert len(res_body) == 500, f"Assert failed. length of comments = {len(res_body)}."
        logging.info(f"Assert passed. length of comments = {len(res_body)}")


    with allure.step("Assert all comments contain 'body' parameter."):
        assert all(
            comment['body'] != None
            for comment in res_body
        ), f"Assert failed. not all comments contain 'body' parameter."
        logging.info(f"Assert passed. all comments contain 'body' parameter. ")


def test_get_comment_by_id(client, id):
    res = client.get(f"/comments/{id}")
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step("Assert comment Id"):
        assert res_body['id'] == id, f"Assert failed. id is {res_body['id']}."
        logging.info(f"Assert passed. id is {res_body['id']}.")


    with allure.step("Assert comment contain all relevant fields."):
        assert_that(res_body).contains_key('postId')
        assert_that(res_body).contains_key('name')
        assert_that(res_body).contains_key('email')
        assert_that(res_body).contains_key('body')
        logging.info("Assert passed. comment contain all relevant fields.")


def test_insert_new_comment(client, id):
    payload = {
        "postId": 1,
        "id": 501,
        "name": "comment 501",
        "email": "aaaa@hotmail.com",
        "body": "new comment"
    }

    res = client.post(f"/comments", payload)
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 201), f"Assert failed. Status code is {res.status_code}."
        logging.info(f"Assert passed. Status code is {res.status_code}.")


    with allure.step("Assert new comment was created"):
        assert res_body['id'] == payload['id'], f"Assert failed. comment not created. {res_body}"
        logging.info(f"Assert passed. comment created. {res_body}")


