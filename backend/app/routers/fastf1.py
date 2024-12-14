from fastapi import APIRouter
from app.services.f1_data import load_race_data, load_driver_performance, load_race_results, load_driver_standings, load_historical_data, load_qualifying_results, load_weather_data, load_driver_trends

router = APIRouter(prefix="/fastf1", tags=["FastF1"])

@router.get("/historical-data/{year}")
async def get_historical_data(year: int, driver: str = None):
    """
    Fetch historical data for a specific year. Optionally filter by driver.
    
    Parameters:
    - `year` (int): The year for which historical data is required.
    - `driver` (str, optional): The driver abbreviation (e.g., 'VER') to filter the data by. If not provided, data for all drivers will be returned.
    
    Returns:
    - `dict`: A dictionary containing the historical data for the specified year (and optionally filtered by driver).
    
    Error Handling:
    - Returns an error message if the data could not be loaded (e.g., invalid year or driver).
    """
    try:
        data = load_historical_data(year, driver)
        return data
    except Exception as e:
        return {"error": str(e)}

@router.get("/standings/{year}")
async def get_driver_standings(year: int):
    """
    Fetch driver standings for a specific season.
    
    Parameters:
    - `year` (int): The season year for which the standings are requested.
    
    Returns:
    - `dict`: A dictionary containing the driver standings for the given season.
    
    Error Handling:
    - Returns an error message if the standings data could not be loaded (e.g., invalid year).
    """
    try:
        standings = load_driver_standings(year)
        return standings
    except Exception as e:
        return {"error": str(e)}

@router.get("/{year}/{grand_prix}")
async def predict_race(year: int, grand_prix: str):
    """
    Fetch race data for a specific year and grand prix (race).
    
    Parameters:
    - `year` (int): The year for the race.
    - `grand_prix` (str): The name of the grand prix (e.g., 'Monaco').
    
    Returns:
    - `dict`: A dictionary containing the race data for the specified year and grand prix.
    
    Error Handling:
    - Returns an error message if the race data could not be loaded (e.g., invalid year or grand prix).
    """
    try:
        data = load_race_data(year, grand_prix)
        return data
    except Exception as e:
        return {"error": str(e)}

@router.get("/driver-performance/{year}/{grand_prix}/{driver}")
async def get_driver_performance(year: int, grand_prix: str, driver: str):
    """
    Fetch performance data for a specific driver in a specific race.
    
    Parameters:
    - `year` (int): The year of the race.
    - `grand_prix` (str): The name of the grand prix (e.g., 'Monaco').
    - `driver` (str): The driver abbreviation (e.g., 'VER') for which performance data is required.
    
    Returns:
    - `dict`: A dictionary containing the lap times, lap positions, and final result for the specified driver.
    
    Error Handling:
    - Returns an error message if the performance data could not be loaded (e.g., invalid year, grand prix, or driver).
    """
    try:
        data = load_driver_performance(year, grand_prix, driver)
        return data
    except Exception as e:
        return {"error": str(e)}

@router.get("/race-results/{year}/{grand_prix}")
async def get_race_results(year: int, grand_prix: str):
    """
    Fetch race results for all drivers in a specific race.
    
    Parameters:
    - `year` (int): The year of the race.
    - `grand_prix` (str): The name of the grand prix (e.g., 'Monaco').
    
    Returns:
    - `dict`: A dictionary containing race results for all drivers, including lap times and final positions.
    
    Error Handling:
    - Returns an error message if the race results data could not be loaded (e.g., invalid year or grand prix).
    """
    try:
        data = load_race_results(year, grand_prix)
        return data
    except Exception as e:
        return {"error": str(e)}

@router.get("/qualifying-results/{year}/{grand_prix}")
async def get_qualifying_results(year: int, grand_prix: str):
    """
    Fetch qualifying results for a specific race.
    
    Parameters:
    - `year` (int): The year of the race.
    - `grand_prix` (str): The name of the grand prix (e.g., 'Monaco').
    
    Returns:
    - `dict`: A dictionary containing qualifying results, including driver grid positions and qualifying times.
    
    Error Handling:
    - Returns an error message if the qualifying results data could not be loaded (e.g., invalid year or grand prix).
    """
    try:
        data = load_qualifying_results(year, grand_prix)
        return data
    except Exception as e:
        return {"error": str(e)}

@router.get("/weather/{year}/{grand_prix}")
async def get_weather_data(year: int, grand_prix: str):
    """
    Fetch weather data for a specific race.
    
    Parameters:
    - `year` (int): The year of the race.
    - `grand_prix` (str): The name of the grand prix (e.g., 'Monaco').
    
    Returns:
    - `dict`: A dictionary containing weather information, including temperature, humidity, wind speed, and rain status.
    
    Error Handling:
    - Returns an error message if the weather data could not be loaded (e.g., invalid year or grand prix).
    """
    try:
        data = load_weather_data(year, grand_prix)
        return data
    except Exception as e:
        return {"error": str(e)}

@router.get("/driver-trends/{year}/{driver}")
async def get_driver_trends(year: int, driver: str):
    """
    Fetch performance trends for a specific driver across all races in a given year.
    
    Parameters:
    - `year` (int): The year for which the performance trends are required.
    - `driver` (str): The driver abbreviation (e.g., 'VER') for which performance data is required.
    
    Returns:
    - `dict`: A dictionary containing the average lap time, fastest lap, standard deviation of lap times, and the number of races completed.
    
    Error Handling:
    - Returns an error message if the driver trends data could not be loaded (e.g., invalid year or driver).
    """
    try:
        data = load_driver_trends(year, driver)
        return data
    except Exception as e:
        return {"error": str(e)}
