import httpx
import logging

BASE_URL = "http://ergast.com/api"

async def fetch_data(endpoint: str, params: dict = None):
    """
    Generic function to fetch data from the Ergast API.
    """
    url = f"{BASE_URL}/{endpoint}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        logging.error(f"An error occurred while requesting {url}: {e}")
        return {"error": "Failed to connect to the Ergast API"}
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
        return {"error": f"HTTP error: {e.response.status_code}"}
