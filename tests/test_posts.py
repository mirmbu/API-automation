import allure
import pytest
import logging
from assertpy import assert_that

#GET functions

def test_get_all_posts(client):
    res = client.get("/posts")
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
       assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
       logging.info(f"Request send successfully. status code is {res.status_code}")

    with allure.step("Assert length of comments."):
        assert len(res_body) == 100, f"Assert failed. length of posts = {len(res_body)}."
        logging.info(f"Assert passed. length of posts = {len(res_body)}.")

    with allure.step("Assert first post"):
        assert_that(res_body[0]).is_not_empty()
        assert_that(res_body[0]).contains_key('id')
        assert_that(res_body[0]['id']).is_equal_to(1)
        logging.info(f"Assert passed. First post is {res_body[0]}")


def test_get_post_by_id(client, id):
    res = client.get(f"/posts/{id}")
    res_body = res.json()

    #Assersions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step("Assert selected post"):
        assert res_body['id'] == id
        assert_that(res_body).contains_key('userId')
        assert_that(res_body).contains_key('body')
        assert_that(res_body).contains_key('title')
        logging.info(f"Assert passed. selected post is {res_body}")


def test_get_all_comments_of_post_by_postId(client, id):

    """
    Verify comments retrieval using the nested resource endpoint.
    param: id
    """

    res = client.get(f"/posts/{id}/comments")
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step("Assert len of comments"):
        assert len(res_body) == 5, f"Assert failed. len of posts = {len(res_body)}."
        logging.info(f"Assert passed. len of posts = {len(res_body)}.")


    with allure.step(f"Assert all postId = {id}"):
        assert all(
            comment['postId'] == id
            for comment in res_body
        ), f"Assert failed. not all comments belong to postId = {id}"
        logging.info(f"Assert passed. all postId = {id}")


def test_get_all_comments_of_post_by_postId_2(client, id):

    """
    Test that Verify comments retrieval using the postId query parameter.
    param: id
    """

    res = client.get(f"/comments?postId={id}")
    res_body = res.json()

    #Assertions
    with allure.step(f"Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step(f"Assert length of comments"):
        assert len(res_body) == 5, f"Assert failed. length of comments = {len(res_body)}"
        logging.info(f"Assert passed. length of comments = {len(res_body)}")


    with allure.step(f"Assert all postId = {id}"):
        assert all(
            comments['postId'] == id
            for comments in res_body
        ), f"Assert failed. not all comments belong to postId = {id}"
        logging.info(f"Assert passed. all comments has postId = {id}")

    with allure.step(f"Assert all comments have email"):
        assert all(
            comment['email'] != None
            for comment in res_body
        ), f"Assert failed. not all comments have email."
        logging.info(f"Assert passed. all comments have email.")

#POST function

def test_insert_new_post(client):

    payload = {
        "userId": 1,
        "id": 101,
        "title": "abcd",
        "body": "hello world."
    }

    res = client.post(f"/posts", payload)
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 201), f"Assert failed. Status code = {res.status_code}."
        logging.info(f"Assert passed. Status code = {res.status_code}.")


    with allure.step("Assert new post was created"):
        assert res_body['id'] == payload['id'], f"Assert failed. post not created. {res_body}."
        logging.info(f"Assert passed. post created successfully. {res_body}.")


    with allure.step("Assert post contain all data"):
        assert set(res_body.keys()) == {"id", "userId", "title", "body"}
        assert res_body['id'] == payload['id']
        assert res_body['userId'] == payload['userId']
        assert res_body['title'] == payload['title']
        assert res_body['body'] == payload['body']
        assert "application/json" in res.headers["Content-Type"]
        logging.info(f"Assert passed. post contain all data.")


#PUT function

def test_put_post(client, id):

    payload = {
        "userId": 1,
        "id": id,
        "title": "abcd",
        "body": "hello abcd"
    }

    res = client.put(f"/posts/{id}", payload)
    res_body = res.json()
    logging.info(res_body)

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code = {res.status_code}."
        logging.info(f"Assert passed. Status code = {res.status_code}.")


    with allure.step("Assert post was updated."):
        assert res_body['title'] == 'abcd', f"Assert failed. post not updated. title = {res_body["title"]}."
        logging.info(f"Assert passed. post was updated. title = {res_body["title"]}.")


    with allure.step("Assert post update with relevant data."):
        assert set(res_body.keys()) == {"userId", "id", "title", "body"}
        assert res_body['id'] == payload['id']
        assert res_body['userId'] == payload['userId']
        assert res_body['title'] == payload['title']
        assert res_body['body'] == payload['body']
        logging.info(f"Assert passed. post updated with all data.")


#PATCH functions

def test_patch_post(client, id):

    payload = {
        "title": "new title",
    }


    res = client.patch(f"/posts/{id}", payload)
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}."
        logging.info(f"Assert passed. Status code is {res.status_code}.")

    with allure.step("Assert new title"):
        assert res_body['title'] == payload['title']
        logging.info(f"Assert passed. new title is {res_body['title']}.")



#DELETE functions

def test_delete_post(client, id):
    res = client.delete(f"/posts/{id}")
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}."
        logging.info(f"Assert passed. Status code is {res.status_code}.")

    with allure.step("Assert deleted post not exist."):
        assert_that(res_body).is_empty(), f"Assert failed. not delete the post."
        logging.info(f"Assert passed. post deleted successfully.")

