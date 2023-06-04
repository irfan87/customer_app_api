import pytest

from rest_framework.test import APIClient


@pytest.fixture(scope="function")
def api_client():
    yield APIClient()


@pytest.mark.django_db
def test_create_new_customer(api_client):
    """
    TEST the create new customer
    :param api_client:
    :return: None
    """
    payload = {
        "firstName": "wokyoh",
        "lastName": "dollah",
        "dob": "2023-06-03",
        "phoneNumber": "012311211",
        "age": 21,
        "email": "john_doe@test.com",
    }

    # create new customer
    response_create = api_client.post("/customers/", data=payload, format="json")
    customer_id = response_create.data["customers"]["id"]
    assert response_create.status_code == 201
    assert response_create.data["customers"]["firstName"] == payload["firstName"]
    assert response_create.data["customers"]["lastName"] == payload["lastName"]
    assert response_create.data["customers"]["dob"] == payload["dob"]
    assert response_create.data["customers"]["phoneNumber"] == payload["phoneNumber"]
    assert response_create.data["customers"]["age"] == payload["age"]
    assert response_create.data["customers"]["email"] == payload["email"]

    # read customer
    response_read = api_client.get(f"/customers/{customer_id}", format="json")
    assert response_read.status_code == 200
    assert response_read.data["customer"]["firstName"] == payload["firstName"]


@pytest.mark.django_db
def test_patch_customer(api_client):
    """
    TEST the update current customer
    :param api_client:
    :return: None
    """

    payload = {
        "firstName": "wokyoh",
        "lastName": "dollah",
        "dob": "2023-06-03",
        "phoneNumber": "012311211",
        "age": 21,
        "email": "john_doe@test.com",
    }

    # create new customer
    response_create = api_client.post("/customers/", data=payload, format="json")
    customer_id = response_create.data["customers"]["id"]
    assert response_create.status_code == 201
    assert response_create.data["customers"]["firstName"] == payload["firstName"]
    assert response_create.data["customers"]["lastName"] == payload["lastName"]
    assert response_create.data["customers"]["dob"] == payload["dob"]
    assert response_create.data["customers"]["phoneNumber"] == payload["phoneNumber"]
    assert response_create.data["customers"]["age"] == payload["age"]
    assert response_create.data["customers"]["email"] == payload["email"]

    # update current customer
    payload["firstName"] = "said"
    response_update = api_client.put(
        f"/customers/{customer_id}", data=payload, format="json"
    )
    assert response_update.status_code == 200
    assert response_update.data["customer"]["firstName"] == payload["firstName"]

    # test if customer does not exists
    response_update = api_client.put(
        f'/customers/{customer_id + int("1")}',
        data=payload,
        format="json",
    )
    assert response_update.status_code == 404


@pytest.mark.django_db
def test_delete_customer(api_client):
    """
    TEST the delete customer API
    :param api_client:
    :return: None
    """
    payload = {
        "firstName": "wokyoh",
        "lastName": "dollah",
        "dob": "2023-06-03",
        "phoneNumber": "012311211",
        "age": 21,
        "email": "john_doe@test.com",
    }
    # create new customer
    response_create = api_client.post("/customers/", data=payload, format="json")
    customer_id = response_create.data["customers"]["id"]
    assert response_create.status_code == 201
    assert response_create.data["customers"]["firstName"] == payload["firstName"]
    assert response_create.data["customers"]["lastName"] == payload["lastName"]
    assert response_create.data["customers"]["dob"] == payload["dob"]
    assert response_create.data["customers"]["phoneNumber"] == payload["phoneNumber"]
    assert response_create.data["customers"]["age"] == payload["age"]
    assert response_create.data["customers"]["email"] == payload["email"]

    # delete the customer
    response_delete = api_client.delete(f"/customers/{customer_id}", format="json")
    assert response_delete.status_code == 204
    # check the customer's id
    response_read = api_client.get(f"/customers/{customer_id}", format="json")
    assert response_read.status_code == 404
