def test_create_user(client):
    payload = {
        "name": "Venu",
        "email": "venu@example.com"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "User created"
    assert response.json()["user"]["email"] == "venu@example.com"

def test_create_user_invalid_data(client):
    payload = {
        "name": "Venu"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 422