# tests/test_flask.py
import pytest
from flask import Flask

# importe a instância 'app' do seu módulo (ajuste se for outro nome/pacote)
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_status_code(client):
    resp = client.get("/")
    assert resp.status_code == 200

def test_index_content(client):
    resp = client.get("/")
    assert b"OK" in resp.data
