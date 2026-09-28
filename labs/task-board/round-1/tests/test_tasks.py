from fastapi.testclient import TestClient

from app.main import app, tasks

client = TestClient(app)


def setup_function() -> None:
    tasks.clear()


def test_create_and_list_tasks() -> None:
    response = client.post("/api/tasks", json={"title": "Write tests"})
    assert response.status_code == 201
    assert response.json()["title"] == "Write tests"
    assert client.get("/api/tasks").json() == [response.json()]


def test_reject_blank_title() -> None:
    response = client.post("/api/tasks", json={"title": "   "})
    assert response.status_code == 422
