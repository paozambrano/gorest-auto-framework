import pytest

def test_create_and_verify_user(user_api, random_user_payload):
    response = user_api.create_user(random_user_payload)

    assert response.status_code == 201, f"Error: 201 was expected but {response.status_code} was obtained"

    user_data = response.json()
    user_id = user_data["id"]

    assert user_data["name"] == random_user_payload["name"]
    assert user_data["email"] == random_user_payload["email"]

    print(f"\nUser successfully created. ID: {user_id} | Name: {user_data['name']} ")

    delete_res = user_api.delete_user(user_id)
    assert delete_res.status_code == 204

