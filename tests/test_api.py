from src.api.app import app

def test_hello_endpoint():
    with app.test_client() as client:
        response = client.get("/api/hello")
        assert response.status_code == 200
        assert response.json == {"message": "Hello from the backend!"}
