import app.controller.routes
import pytest

class TestRoutes:

    def test_create_client(self, client):

        payload ={
            "name": "Livinha",
            "phone": "12992240202",
            "address": "rua teste",
            "address_number": 1
        }

        response = client.post("/create_clients",json= payload)

        assert response.status_code == 201
        
        body = response.json()

        assert body["name"]             == payload["name"]
        assert body["phone"]            == payload["phone"]
        assert body["address"]          == payload["address"]
        assert body["address_number"]   == payload["address_number"]

    def test_create_orders(self, client):
        client_payload = {
            "name": "Test Client",
            "phone": "12992240202",
            "address": "rua teste",
            "address_number": 1
        }
        client_response = client.post("/create_clients", json=client_payload)
        client_data = client_response.json()
        client_id = client_data["id"]

        product_payload = {
            "product_name": "calabresa",
            "price": 50
        }
        product_response = client.post("/create_catalog_product", json=product_payload)
        product_data = product_response.json()
        product_id = product_data["id"]

        payload = {
            "product_id": product_id,
            "client_id": client_id
        }

        response = client.post("/create_orders", json=payload)

        assert response.status_code == 201

        body = response.json()

        assert body["product_id"] == payload["product_id"]
        assert body["client_id"] == payload["client_id"]

    def test_create_catalog_product(self, client):

        payload = {
            "product_name": "calabresa",
            "price": 50
        }

        response = client.post("/create_catalog_product", json=payload)

        assert response.status_code == 201

        body = response.json()

        assert body["product_name"] == payload["product_name"]
        assert body["price"] == payload["price"]

    def test_list_clients(self, client):
        response = client.get("/clients")

        assert response.status_code == 200

        assert len(response.json()) >= 0
    
    def test_list_orders(self, client):
        response = client.get("/orders")

        assert response.status_code == 200

        assert len(response.json()) >= 0