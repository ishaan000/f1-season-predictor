import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

# Create a TestClient
client = TestClient(app)

# 1. Test Historical Data Endpoint
def test_historical_data():
    response = client.get("/prediction/historical-data/2023")
    assert response.status_code == 200
    assert "error" not in response.json()  # Ensure no error in response

# 2. Test Driver Standings Endpoint
def test_driver_standings():
    response = client.get("/prediction/standings/2023")
    assert response.status_code == 200
    assert "standings" in response.json()

# 3. Test Race Prediction Endpoint
def test_predict_race():
    response = client.get("/prediction/2023/Monaco")
    assert response.status_code == 200
    assert "race" in response.json()

# 4. Test Driver Performance Endpoint
def test_driver_performance():
    response = client.get("/prediction/driver-performance/2023/Monaco/VER")
    assert response.status_code == 200
    assert "driver" in response.json()

# 5. Test Race Results Endpoint
def test_race_results():
    response = client.get("/prediction/race-results/2023/Monaco")
    assert response.status_code == 200
    assert "results" in response.json()

# 6. Test Qualifying Results Endpoint
def test_qualifying_results():
    response = client.get("/prediction/qualifying-results/2023/Monaco")
    assert response.status_code == 200
    assert "qualifying_results" in response.json()

# 7. Test Weather Data Endpoint
def test_weather_data():
    response = client.get("/prediction/weather/2023/Monaco")
    assert response.status_code == 200
    assert "weather" in response.json()

# 8. Test Driver Trends Endpoint
def test_driver_trends():
    response = client.get("/prediction/driver-trends/2023/VER")
    assert response.status_code == 200
    assert "driver" in response.json()
