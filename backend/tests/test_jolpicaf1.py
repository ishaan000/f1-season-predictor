import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from app.main import app  # Update this import if your FastAPI app is in a different module

client = TestClient(app)

@pytest.fixture
def mock_fetch_data():
    with patch("app.services.jolpicaf1_data.fetch_data", new_callable=AsyncMock) as mock:
        yield mock

@pytest.fixture
def mock_fetch_data():
    with patch("app.services.jolpicaf1_data.fetch_data", new_callable=AsyncMock) as mock:
        yield mock


# Test /seasons endpoint
def test_get_seasons_available(mock_fetch_data):
    mock_response = {"MRData": {"SeasonTable": {"Seasons": []}}}
    mock_fetch_data.return_value = mock_response

    response = client.get("/jolpicaf1/seasons")

    assert response.status_code == 200
    assert "MRData" in response.json()
    assert "SeasonTable" in response.json()["MRData"]


# Test /drivers endpoint
def test_get_drivers_available(mock_fetch_data):
    mock_response = {"MRData": {"DriverTable": {"Drivers": []}}}
    mock_fetch_data.return_value = mock_response

    response = client.get("/jolpicaf1/drivers")

    assert response.status_code == 200
    assert "MRData" in response.json()
    assert "DriverTable" in response.json()["MRData"]


# Test /circuits endpoint
def test_get_circuits_available(mock_fetch_data):
    mock_response = {"MRData": {"CircuitTable": {"Circuits": []}}}
    mock_fetch_data.return_value = mock_response

    response = client.get("/jolpicaf1/circuits")

    assert response.status_code == 200
    assert "MRData" in response.json()
    assert "CircuitTable" in response.json()["MRData"]


# Test /constructors endpoint
def test_get_constructors_available(mock_fetch_data):
    mock_response = {"MRData": {"ConstructorTable": {"Constructors": []}}}
    mock_fetch_data.return_value = mock_response

    response = client.get("/jolpicaf1/constructors")

    assert response.status_code == 200
    assert "MRData" in response.json()
    assert "ConstructorTable" in response.json()["MRData"]


# Test /{season}/constructorstandings endpoint
def test_get_constructor_standings(mock_fetch_data):
    season = 2021
    mock_response = {"MRData": {"StandingsTable": {"StandingsLists": []}}}
    mock_fetch_data.return_value = mock_response

    response = client.get(f"/jolpicaf1/{season}/constructorstandings")

    assert response.status_code == 200
    assert "MRData" in response.json()
    assert "StandingsTable" in response.json()["MRData"]


# Test /{season}/driverstandings endpoint
def test_get_driver_standings(mock_fetch_data):
    season = 2021
    mock_response = {"MRData": {"StandingsTable": {"StandingsLists": []}}}
    mock_fetch_data.return_value = mock_response

    response = client.get(f"/jolpicaf1/{season}/driverstandings")

    assert response.status_code == 200
    assert "MRData" in response.json()
    assert "StandingsTable" in response.json()["MRData"]


# Test /{season}/{round}/laps endpoint
def test_get_laps(mock_fetch_data):
    season = 2021
    round_number = 1
    mock_response = {"MRData": {"RaceTable": {"Races": []}}}
    mock_fetch_data.return_value = mock_response

    response = client.get(f"/jolpicaf1/{season}/{round_number}/laps")

    assert response.status_code == 200
    assert "MRData" in response.json()
    assert "RaceTable" in response.json()["MRData"]


# Test /status endpoint
def test_get_status_available(mock_fetch_data):
    mock_response = {"MRData": {"StatusTable": {"Status": []}}}
    mock_fetch_data.return_value = mock_response

    response = client.get("/jolpicaf1/status")

    assert response.status_code == 200
    assert "MRData" in response.json()
    assert "StatusTable" in response.json()["MRData"]


# Test invalid query parameters
def test_invalid_query_params(mock_fetch_data):
    mock_response = {"MRData": {"Error": "Invalid parameters"}}
    mock_fetch_data.return_value = mock_response

    response = client.get("/jolpicaf1/seasons", params={"limit": -1, "offset": "invalid"})

    assert response.status_code == 422  # Unprocessable Entity for invalid parameters
