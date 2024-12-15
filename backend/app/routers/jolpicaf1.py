from fastapi import APIRouter, Query, Path
from app.services.jolpicaf1_data import fetch_data

# Initialize the router for JolpicaF1 API
router = APIRouter(prefix="/jolpicaf1", tags=["JolpicaF1"])

# Route to fetch all available F1 seasons
@router.get("/seasons")
async def get_seasons(
    limit: int = Query(30, description="Maximum number of seasons to return (default: 30, max: 100)"),
    offset: int = Query(0, description="Number of records to skip for pagination (default: 0)"),
):
    """
    Retrieve a list of all Formula 1 seasons.
    Each season contains the year and a URL pointing to the Wikipedia page for that season.
    
    Args:
        limit (int): Maximum number of results to return per request.
        offset (int): The starting point for pagination.

    Returns:
        JSON response containing season details, including year and Wikipedia URLs.
    """
    return await fetch_data("f1/seasons.json", {"limit": limit, "offset": offset})


# Route to fetch a list of F1 drivers
@router.get("/drivers")
async def get_drivers(
    limit: int = Query(30, description="Maximum number of drivers to return (default: 30, max: 100)"),
    offset: int = Query(0, description="Number of records to skip for pagination (default: 0)"),
):
    """
    Retrieve a paginated list of all Formula 1 drivers.
    Each driver entry includes details like name, nationality, and date of birth.

    Args:
        limit (int): Maximum number of results to return per request.
        offset (int): The starting point for pagination.

    Returns:
        JSON response with driver information, including name, nationality, and date of birth.
    """
    return await fetch_data("f1/drivers.json", {"limit": limit, "offset": offset})


# Route to fetch a list of F1 circuits
@router.get("/circuits")
async def get_circuits(
    limit: int = Query(30, description="Maximum number of circuits to return (default: 30, max: 100)"),
    offset: int = Query(0, description="Number of records to skip for pagination (default: 0)"),
):
    """
    Retrieve a paginated list of Formula 1 circuits.
    Each circuit includes details like circuit name, location, and URL.

    Args:
        limit (int): Maximum number of results to return per request.
        offset (int): The starting point for pagination.

    Returns:
        JSON response with circuit details, including location and circuit name.
    """
    return await fetch_data("f1/circuits.json", {"limit": limit, "offset": offset})


# Route to fetch a list of F1 constructors
@router.get("/constructors")
async def get_constructors(
    limit: int = Query(30, description="Maximum number of constructors to return (default: 30, max: 100)"),
    offset: int = Query(0, description="Number of records to skip for pagination (default: 0)"),
):
    """
    Retrieve a paginated list of Formula 1 constructors.
    Each constructor includes details like name, nationality, and associated URL.

    Args:
        limit (int): Maximum number of results to return per request.
        offset (int): The starting point for pagination.

    Returns:
        JSON response with constructor information, including name and nationality.
    """
    return await fetch_data("f1/constructors.json", {"limit": limit, "offset": offset})


# Route to fetch constructor standings for a specific season
@router.get("/{season}/constructorstandings")
async def get_constructor_standings(
    season: int = Path(..., description="The season year for which to fetch constructor standings (e.g., 2021)"),
    limit: int = Query(30, description="Maximum number of results to return per request (default: 30, max: 100)"),
    offset: int = Query(0, description="The starting point for pagination (default: 0)"),
):
    """
    Retrieve constructor standings for a specific Formula 1 season.
    Each entry includes details about the constructor and their points.

    Args:
        season (int): The season year (e.g., 2021).
        limit (int): Maximum number of results to return per request.
        offset (int): The starting point for pagination.

    Returns:
        JSON response with constructor standings, including points and position.
    """
    return await fetch_data(f"f1/{season}/constructorstandings.json", {"limit": limit, "offset": offset})


# Route to fetch driver standings for a specific season
@router.get("/{season}/driverstandings")
async def get_driver_standings(
    season: int = Path(..., description="The season year for which to fetch driver standings (e.g., 2021)"),
    limit: int = Query(30, description="Maximum number of results to return per request (default: 30, max: 100)"),
    offset: int = Query(0, description="The starting point for pagination (default: 0)"),
):
    """
    Retrieve driver standings for a specific Formula 1 season.
    Each entry includes details about the driver, points, and position.

    Args:
        season (int): The season year (e.g., 2021).
        limit (int): Maximum number of results to return per request.
        offset (int): The starting point for pagination.

    Returns:
        JSON response with driver standings, including points and position.
    """
    return await fetch_data(f"f1/{season}/driverstandings.json", {"limit": limit, "offset": offset})


# Route to fetch lap data for a specific race in a season
@router.get("/{season}/{round}/laps")
async def get_laps(
    season: int = Path(..., description="The season year (e.g., 2021)"),
    round: int = Path(..., description="The race round number (e.g., 1 for the first race of the season)"),
    limit: int = Query(30, description="Maximum number of results to return per request (default: 30, max: 100)"),
    offset: int = Query(0, description="The starting point for pagination (default: 0)"),
):
    """
    Retrieve lap data for a specific race in a Formula 1 season.
    Each entry includes lap timing information.

    Args:
        season (int): The season year (e.g., 2021).
        round (int): The race round number (e.g., 1).
        limit (int): Maximum number of results to return per request.
        offset (int): The starting point for pagination.

    Returns:
        JSON response with lap data for the specified race.
    """
    return await fetch_data(f"f1/{season}/{round}/laps.json", {"limit": limit, "offset": offset})


# Route to fetch status data for F1 events
@router.get("/status")
async def get_status(
    limit: int = Query(30, description="Maximum number of results to return (default: 30, max: 100)"),
    offset: int = Query(0, description="Number of records to skip for pagination (default: 0)"),
):
    """
    Retrieve status data for Formula 1 events.
    Status entries indicate various outcomes of races (e.g., finished, accident, disqualified).

    Args:
        limit (int): Maximum number of results to return per request.
        offset (int): The starting point for pagination.

    Returns:
        JSON response with race statuses and their occurrences.
    """
    return await fetch_data("f1/status.json", {"limit": limit, "offset": offset})
