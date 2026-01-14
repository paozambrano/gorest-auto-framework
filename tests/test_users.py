import pytest
from jsonschema import validate
import os
import json

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

def test_user_schema_contract(user_api, random_user_payload):
    response = user_api.create_user(random_user_payload)
    response_data = response.json()

    schema_path = os.path.join(os.path.dirname(__file__), "../schemas/user_schema.json")

    with open(schema_path, "r") as file:
        schema = json.load(file)

    validate(instance=response_data, schema=schema)

    print("\n The API contract is valid. The structure is correct.")

    user_api.delete_user(response_data["id"])
