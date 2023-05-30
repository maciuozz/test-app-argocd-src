"""
Module for test API endpoints
"""

from fastapi.testclient import TestClient

from application.app import app, health_message, root_endpoint_message

client = TestClient(app)


class TestFastAPIApp:
    """
    Class define tests for testing FastAPI application
    """

    def read_main_test(self):
        """Tests access to the root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == root_endpoint_message

    def read_health_test(self):
        """Tests access to the healtcheck endpoint"""
        response = client.get("health")
        assert response.status_code == 200
        assert response.json() == health_message
