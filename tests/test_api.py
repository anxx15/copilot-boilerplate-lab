from fastapi.testclient import TestClient

from app.main import app


def test_api_hello_returns_expected_message() -> None:
    client = TestClient(app)
    response = client.get("/api/hello")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI boilerplate"}
