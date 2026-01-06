# tests/test_flask.py
import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_status_code(client):
    resp = client.get("/")
    assert resp.status_code == 200

