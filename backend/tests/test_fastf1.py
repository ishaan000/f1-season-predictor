import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

# Create a TestClient
client = TestClient(app)

# 1. Test Historical Data Endpoint
def test_historical_data():
    response = client.get("/fastf1/historical-data/2023")
    assert response.status_code == 200
    assert "error" not in response.json()  # Ensure no error in response

# 2. Test Driver Standings Endpoint
def test_driver_standings():
    response = client.get("/fastf1/standings/2023")
    assert response.status_code == 200
    assert "standings" in response.json()

# 3. Test Race Prediction Endpoint
def test_predict_race():
    response = client.get("/fastf1/2023/Monaco")
    assert response.status_code == 200
    assert "race" in response.json()

# 4. Test Driver Performance Endpoint
def test_driver_performance():
    response = client.get("/fastf1/driver-performance/2023/Monaco/VER")
    assert response.status_code == 200
    assert "driver" in response.json()

# 5. Test Race Results Endpoint
def test_race_results():
    response = client.get("/fastf1/race-results/2023/Monaco")
    assert response.status_code == 200
    assert "results" in response.json()

# 6. Test Qualifying Results Endpoint
def test_qualifying_results():
    response = client.get("/fastf1/qualifying-results/2023/Monaco")
    assert response.status_code == 200
    assert "qualifying_results" in response.json()

# 7. Test Weather Data Endpoint
def test_weather_data():
    response = client.get("/fastf1/weather/2023/Monaco")
    assert response.status_code == 200
    assert "weather" in response.json()

# 8. Test Driver Trends Endpoint
def test_driver_trends():
    response = client.get("/fastf1/driver-trends/2023/VER")
    assert response.status_code == 200
    assert "driver" in response.json()
