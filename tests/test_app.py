from chalice.test import Client
from app import app

list = [
    {
        "name": "Maça",
        "price": "1.99"
    },
    {
        "name": "Morango",
        "price": "3.99"
    }
]


def testProducts():
    with Client(app) as client:
        response = client.http.get('/products')
        assert response.json_body == list
