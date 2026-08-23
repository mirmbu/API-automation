import allure
import pytest
import logging
from assertpy import assert_that



def test_get_posts(client):
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


def test_get_post_by_id(client, post_id):
    res = client.get(f"/posts/{post_id}")
    res_body = res.json()


    #Assersions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step("Assert selected post"):
        assert res_body['id'] == post_id
        assert_that(res_body).contains_key('userId')
        assert_that(res_body).contains_key('body')
        assert_that(res_body).contains_key('title')
        logging.info(f"Assert passed. selected post is {res_body}")


def test_get_all_comments_of_post_by_postId(client, post_id):

    """
    Verify comments retrieval using the nested resource endpoint.
    param: post_id
    """

    res = client.get(f"/posts/{post_id}/comments")
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step("Assert len of comments"):
        assert len(res_body) == 5, f"Assert failed. len of posts = {len(res_body)}."
        logging.info(f"Assert passed. len of posts = {len(res_body)}.")


    with allure.step(f"Assert all postId = {post_id}"):
        assert all(
            comment['postId'] == post_id
            for comment in res_body
        ), f"Assert failed. not all comments belong to postId = {post_id}"
        logging.info(f"Assert passed. all postId = {post_id}")



def test_get_all_comments_of_post_by_postId_2(client, post_id):

    """
    Test that Verify comments retrieval using the postId query parameter.
    param: post_id
    """

    res = client.get(f"/comments?postId={post_id}")
    res_body = res.json()

    #Assertions
    with allure.step(f"Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step(f"Assert length of comments"):
        assert len(res_body) == 5, f"Assert failed. length of comments = {len(res_body)}"
        logging.info(f"Assert passed. length of comments = {len(res_body)}")


    with allure.step(f"Assert all postId = {post_id}"):
        assert all(
            comments['postId'] == post_id
            for comments in res_body
        ), f"Assert failed. not all comments belong to postId = {post_id}"
        logging.info(f"Assert passed. all comments has postId = {post_id}")

    with allure.step(f"Assert all comments have email"):
        assert all(
            comment['email'] != None
            for comment in res_body
        ), f"Assert failed. not all comments have email."
        logging.info(f"Assert passed. all comments have email.")
