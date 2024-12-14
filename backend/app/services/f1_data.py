import fastf1
from fastf1 import get_event_schedule, get_session
from fastf1 import Cache
import pandas as pd

def load_race_data(year: int, grand_prix: str) -> dict:
    fastf1.Cache.enable_cache("cache")  # Enables caching to avoid repeated API calls

    try:
        # Load the race session
        session = fastf1.get_session(year, grand_prix, 'R')  # 'R' for race session
        session.load()

        # Get lap data for a specific driver (e.g., Verstappen)
        laps = session.laps.pick_drivers('VER')  # Replace 'VER' with dynamic input later
        lap_times = laps['LapTime'].dropna().dt.total_seconds().tolist()

        return {
            "race": f"{year} {grand_prix}",
            "driver": "VER",
            "lap_times": lap_times,
        }
    except Exception as e:
        raise RuntimeError(f"Error loading race data: {str(e)}")

def load_driver_performance(year: int, grand_prix: str, driver: str) -> dict:
    fastf1.Cache.enable_cache("cache")  # Enables caching

    try:
        # Load the race session
        session = fastf1.get_session(year, grand_prix, 'R')  # 'R' for Race
        session.load()

        # Get lap times and positions for the specified driver
        laps = session.laps.pick_drivers(driver)
        lap_times = laps['LapTime'].dropna().dt.total_seconds().tolist()
        positions = laps['Position'].dropna().astype(int).tolist()  # Convert positions to integers

        # Determine the final result
        result_row = session.results.loc[session.results['Abbreviation'] == driver]
        result = int(result_row['Position'].values[0]) if not result_row.empty else "DNF"  # Convert to integer if exists

        return {
            "race": f"{year} {grand_prix}",
            "driver": driver,
            "lap_times": lap_times,
            "lap_positions": positions,
            "result": result,
        }
    except Exception as e:
        raise RuntimeError(f"Error loading driver performance: {str(e)}")

def load_race_results(year: int, grand_prix: str) -> dict:
    fastf1.Cache.enable_cache("cache")  # Enables caching

    try:
        # Load the race session
        session = fastf1.get_session(year, grand_prix, 'R')  # 'R' for Race
        session.load()

        # Fetch race results for all drivers
        results = []
        for driver_number in session.drivers:
            # Map driver number to abbreviation
            driver_row = session.results.loc[session.results['DriverNumber'] == driver_number]
            if driver_row.empty:
                continue  # Skip if driver data is missing
            driver_abbreviation = driver_row['Abbreviation'].values[0]

            # Get lap data for the driver
            laps = session.laps.pick_drivers(driver_abbreviation)
            lap_times = laps['LapTime'].dropna().dt.total_seconds().tolist()
            lap_positions = laps['Position'].dropna().astype(int).tolist()

            # Get final race position
            final_position = int(driver_row['Position'].values[0]) if 'Position' in driver_row else "DNF"

            results.append({
                "driver_number": driver_number,  # Add driver number
                "driver_abbreviation": driver_abbreviation,  # Add driver abbreviation
                "final_position": final_position,
                "lap_times": lap_times,
                "lap_positions": lap_positions,
            })

        return {
            "race": f"{year} {grand_prix}",
            "results": results,
        }
    except Exception as e:
        raise RuntimeError(f"Error loading race results: {str(e)}")

def load_driver_standings(year: int) -> dict:
    fastf1.Cache.enable_cache("cache")  # Enable caching

    try:
        schedule = fastf1.get_event_schedule(year)
        races = schedule[schedule['Session1Date'].notnull()]

        # Create a standings dictionary
        driver_points = {}

        for _, race in races.iterrows():
            try:
                session = fastf1.get_session(year, race['EventName'], 'R')
                session.load()

                for driver in session.results.iterrows():
                    driver_data = driver[1]
                    abbreviation = driver_data['Abbreviation']
                    points = driver_data['Points']

                    if abbreviation in driver_points:
                        driver_points[abbreviation] += points
                    else:
                        driver_points[abbreviation] = points
            except Exception as e:
                print(f"Error processing race: {race['EventName']}: {e}")
                continue

        # Sort drivers by points
        sorted_standings = sorted(driver_points.items(), key=lambda x: x[1], reverse=True)
        return {"year": year, "standings": sorted_standings}

    except Exception as e:
        raise RuntimeError(f"Error loading standings: {str(e)}")

def load_historical_data(year: int, driver: str = None) -> dict:
    fastf1.Cache.enable_cache("cache")  # Enables caching

    try:
        # Load race schedule for the year
        schedule = fastf1.get_event_schedule(year)
        races = schedule[schedule['Session1Date'].notnull()]['EventName'].tolist()

        historical_data = []
        for race in races:
            try:
                # Load race session
                session = fastf1.get_session(year, race, 'R')  # 'R' for Race
                session.load()

                if driver:
                    # Fetch specific driver data
                    laps = session.laps.pick_drivers(driver)
                    lap_times = laps['LapTime'].dropna().dt.total_seconds().tolist()
                    lap_positions = laps['Position'].dropna().astype(int).tolist()

                    result_row = session.results.loc[session.results['Abbreviation'] == driver]
                    final_position = (
                        int(result_row['Position'].values[0]) if not result_row.empty else "DNF"
                    )

                    race_data = {
                        "race": f"{year} {race}",
                        "driver": driver,
                        "lap_times": lap_times,
                        "lap_positions": lap_positions,
                        "result": final_position,
                    }
                else:
                    # Fetch all drivers' data
                    results = []
                    for driver_number in session.drivers:
                        driver_row = session.results.loc[
                            session.results['DriverNumber'] == driver_number
                        ]
                        if driver_row.empty:
                            continue

                        driver_abbreviation = driver_row['Abbreviation'].values[0]
                        laps = session.laps.pick_drivers(driver_abbreviation)
                        lap_times = laps['LapTime'].dropna().dt.total_seconds().tolist()
                        lap_positions = laps['Position'].dropna().astype(int).tolist()

                        final_position = (
                            int(driver_row['Position'].values[0]) if 'Position' in driver_row else "DNF"
                        )

                        results.append({
                            "driver_number": driver_number,
                            "driver": driver_abbreviation,
                            "final_position": final_position,
                            "lap_times": lap_times,
                            "lap_positions": lap_positions,
                        })

                    race_data = {
                        "race": f"{year} {race}",
                        "results": results,
                    }

                historical_data.append(race_data)

            except Exception as race_error:
                print(f"Error loading data for {race}: {str(race_error)}")
                continue

        return {"year": year, "historical_data": historical_data}
    except Exception as e:
        raise RuntimeError(f"Error loading historical data: {str(e)}")

def load_qualifying_results(year: int, grand_prix: str) -> dict:
    """
    Load qualifying results for a specific race, with calculated grid positions.
    """
    fastf1.Cache.enable_cache("cache")  # Enable caching

    try:
        session = fastf1.get_session(year, grand_prix, 'Q')  # 'Q' for Qualifying
        session.load()

        qualifying_results = []
        lap_times = []

        for driver_data in session.results.itertuples():
            driver = driver_data.Abbreviation

            # Extract the best lap time from session.laps
            driver_laps = session.laps.pick_drivers(driver)
            if not driver_laps.empty:
                best_lap = driver_laps.pick_fastest()
                best_lap_time = best_lap['LapTime'].total_seconds()
                lap_times.append((driver, best_lap_time))
            else:
                lap_times.append((driver, float('inf')))  # Assign infinity for drivers with no time

        # Sort drivers by best lap time to determine grid positions
        lap_times.sort(key=lambda x: x[1])

        for grid_position, (driver, lap_time) in enumerate(lap_times, start=1):
            qualifying_results.append({
                "driver": driver,
                "grid_position": grid_position if lap_time != float('inf') else "N/A",
                "qualifying_time": lap_time if lap_time != float('inf') else "N/A",
            })

        return {
            "race": f"{year} {grand_prix}",
            "qualifying_results": qualifying_results,
        }

    except Exception as e:
        raise RuntimeError(f"Error loading qualifying results: {str(e)}")
    
def load_weather_data(year: int, grand_prix: str) -> dict:
    """
    Load weather data for a specific race.
    """
    fastf1.Cache.enable_cache("cache")  # Enable caching

    try:
        session = fastf1.get_session(year, grand_prix, 'R')  # 'R' for Race
        session.load()

        weather_data = session.weather_data  # Extract weather data
        weather_info = {
            "temperature": weather_data['AirTemp'].mean(),
            "humidity": weather_data['Humidity'].mean(),
            "wind_speed": weather_data['WindSpeed'].mean(),
            "rain": any(weather_data['Rainfall'] > 0),  # True if rain detected
        }

        return {
            "race": f"{year} {grand_prix}",
            "weather": weather_info,
        }

    except Exception as e:
        raise RuntimeError(f"Error loading weather data: {str(e)}")

import pandas as pd
import fastf1

def load_driver_trends(year: int, driver: str) -> dict:
    """
    Load performance trends for a specific driver across all races in a given year.

    Args:
        year (int): The year to analyze.
        driver (str): The driver's three-letter abbreviation.

    Returns:
        dict: A dictionary containing driver's performance trends.
    """
    fastf1.Cache.enable_cache("cache")  # Enable caching

    try:
        # Fetch event schedule for the given year
        schedule = fastf1.get_event_schedule(year)
        races = schedule[schedule['Session1Date'].notnull()]
        
        total_laps = []
        fastest_laps = []
        race_count = 0

        for _, race in races.iterrows():
            try:
                session = fastf1.get_session(year, race['EventName'], 'R')
                session.load()
                driver_laps = session.laps.pick_drivers(driver)

                # Append lap times
                lap_times = driver_laps['LapTime'].dropna().dt.total_seconds().tolist()
                total_laps.extend(lap_times)

                # Append fastest lap for this race
                fastest_lap = driver_laps['LapTime'].min().total_seconds()
                fastest_laps.append(fastest_lap)

                race_count += 1
            except Exception as e:
                print(f"Error processing race {race['EventName']}: {e}")
                continue

        if not total_laps:
            available_drivers = session.laps['Driver'].unique().tolist() if 'session' in locals() else []
            return {
                "error": f"No valid lap data found for driver '{driver}' in {year}.",
                "available_drivers": available_drivers,
            }

        # Calculate trends
        average_lap_time = sum(total_laps) / len(total_laps)
        fastest_lap = min(fastest_laps)
        lap_time_std_dev = (sum((x - average_lap_time) ** 2 for x in total_laps) / len(total_laps)) ** 0.5

        return {
            "year": year,
            "driver": driver,
            "average_lap_time": average_lap_time,
            "fastest_lap": fastest_lap,
            "lap_time_std_dev": lap_time_std_dev,
            "completed_races": race_count,
            "total_laps_analyzed": len(total_laps),
            "min_lap_time": min(total_laps),
            "max_lap_time": max(total_laps),
        }

    except Exception as e:
        raise RuntimeError(f"Error loading driver trends: {str(e)}")
