import pytest
import allure
import logging
from assertpy import assert_that

#GET function

def test_get_all_albums(client):
    res = client.get('/albums')
    res_body = res.json()

    #Assertions
    with allure.step("Assert status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}."
        logging.info(f"Assert pass. Status code is {res.status_code}.")

    with allure.step("Assert length of albums."):
        assert len(res_body) == 100, f"Assert failed. length is {len(res_body)}."
        logging.info(f"Assert pass. length is {len(res_body)}.")

    with allure.step("Assert all albums contain 'title' parameter"):
        assert all(
            album['title'] != None
            for album in res_body
        ), f"Assert failed. not all albums contain 'title' parameter."
        logging.info("Assert pass. all album contain 'title' parameter.")


def test_get_album_by_id(client, id):
    res = client.get(f"/albums/{id}")
    res_body = res.json()

    #Assertions
    with allure.step("Assert Status code"):
        assert client.status_code(res, 200), f"Assert failed. Status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")

    with allure.step("Assert album id"):
        assert res_body['id'] == id, f"Assert failed. Id is {res_body['id']}"
        logging.info(f"Assert passed. Id is {res_body['id']}")

    with allure.step("Assert album contain all relevant keys"):
        assert_that(res_body).contains_key('userId')
        assert_that(res_body).contains_key('id')
        assert_that(res_body).contains_key('title')
        logging.info(f"Assert passed. object has all relevant keys")

#POST functions

def test_insert_new_album(client):

    payload = {
        'userId': 10,
        'id': 101,
        'title': 'new album'
    }

    res = client.post(f"/albums", payload)
    res_body = res.json()

    #Assertions

    with allure.step("Assert Status code"):
        assert client.status_code(res, 201), f"Assert failed. Status code is {res.status_code}"
        logging.info(f"Assert passed. Status code is {res.status_code}")


    with allure.step("Assert new album is created"):
        assert res_body['id'] == payload['id'], f"Assert failed. new album not created successfully."
        logging.info(f"Assert passed. new album created successfully.")


    with allure.step("Assert new album contain all data"):
        assert set(res_body.keys()) == {"userId", "id", "title"}
        assert res_body['userId'] == payload['userId']
        assert res_body['id'] == payload['id']
        assert res_body['title'] == payload['title']
        logging.info("Assert passed. new album contain all data.")