import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_home(client):
    response = client.get("/home")
    assert response.status_code == 302
    # assert response.location == "http://localhost/"
    assert response.location == "http://127.0.0.1:5000/"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Index</title>" in response.data


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"<title>About</title>" in response.data


""" Write your own tests below."""


def test_extra(client):
    response = client.get("/extra")
    assert response.status_code == 200
    assert b"<title>Extra</title>" in response.data
