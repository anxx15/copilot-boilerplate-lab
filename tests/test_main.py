from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app


def test_root_returns_health_check() -> None:
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == {"status": "ok", "app": settings.app_name}


def test_api_hello_returns_expected_message() -> None:
    with TestClient(app) as client:
        response = client.get("/api/hello")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == {"message": "Hello from FastAPI boilerplate"}


def test_unmatched_route_returns_404() -> None:
    with TestClient(app) as client:
        response = client.get("/does-not-exist")

    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


def test_app_routes_are_registered() -> None:
    route_paths = {route.path for route in app.routes}

    assert "/" in route_paths
    assert "/api/hello" in route_paths
