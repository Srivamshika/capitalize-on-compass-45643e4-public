from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_overview_is_labelled_demo_data() -> None:
    response = client.get("/api/overview")
    assert response.status_code == 200
    assert response.json()["demo_data"] is True
