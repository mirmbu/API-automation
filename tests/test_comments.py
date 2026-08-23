import allure
import pytest
import logging
from assertpy import assert_that


def test_get_all_comments(client):
    res = client.get("/comments")
    res_body = res.json()

