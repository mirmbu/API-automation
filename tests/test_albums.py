import pytest
import allure
import logging
from assertpy import assert_that


def test_get_albums(client):
    res = client.get('/albums')
    res_body = res.json()

    #Assertions