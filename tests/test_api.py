from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_health_endpoint():
    """
    verify that the health endpoint returns a 200 status code and the expected response
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_endpoint():
    """
    verify that the predict endpoint returns a 200 status code and the expected response
    """
    # Sample input data for prediction
    payload = {
        "sepal_length": 3.4,
        "sepal_width": 1.4, 
        "petal_length": 3.4,
        "petal_width": 0.4
        }
    
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    # Check if the response contains a prediction key
    result = response.json()

    assert "prediction" in result
    assert "class_name" in result
    assert result["class_name"] in ["setosa", "versicolor", "virginica"]
    assert result["prediction"] in [0, 1, 2]
    