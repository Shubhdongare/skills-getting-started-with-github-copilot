import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: nothing to set up for a GET
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_success_and_duplicate():
    # Arrange
    email = "aaa_testuser@mergington.edu"
    activity = "Chess Club"
    # Act
    signup_response = client.post(f"/activities/{activity}/signup", params={"email": email})
    duplicate_response = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert signup_response.status_code == 200
    assert duplicate_response.status_code == 400

def test_unregister_success_and_not_found():
    # Arrange
    email = "aaa_testuser2@mergington.edu"
    activity = "Programming Class"
    client.post(f"/activities/{activity}/signup", params={"email": email})
    # Act
    unregister_response = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    unregister_again_response = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert unregister_response.status_code == 200
    assert unregister_again_response.status_code == 404
