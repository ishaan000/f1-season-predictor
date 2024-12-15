import pandas as pd
import os

# File paths
DATA_DIR = "app/data/Formula 1 World Championship (1950 - 2024)"
PROCESSED_FILE = os.path.join(DATA_DIR, "processed_race_details.csv")
RACES_FILE = os.path.join(DATA_DIR, "races.csv")
CIRCUITS_FILE = os.path.join(DATA_DIR, "circuits.csv")
RESULTS_FILE = os.path.join(DATA_DIR, "results.csv")
DRIVERS_FILE = os.path.join(DATA_DIR, "drivers.csv")
CONSTRUCTORS_FILE = os.path.join(DATA_DIR, "constructors.csv")

# Create the output directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

print("Loading datasets...")
# Load datasets
races = pd.read_csv(RACES_FILE)
circuits = pd.read_csv(CIRCUITS_FILE)
results = pd.read_csv(RESULTS_FILE)
drivers = pd.read_csv(DRIVERS_FILE)
constructors = pd.read_csv(CONSTRUCTORS_FILE)

# Rename columns for consistency
print("Renaming columns for consistency...")
circuits.rename(columns={"name": "circuitName"}, inplace=True)
drivers.rename(columns={
    "forename": "driverForename",
    "surname": "driverSurname",
    "nationality": "driverNationality"
}, inplace=True)
drivers["driverName"] = drivers["driverForename"] + " " + drivers["driverSurname"]
constructors.rename(columns={"name": "constructorName"}, inplace=True)

print("Merging DataFrames...")
# Merge races and circuits
race_details = pd.merge(races, circuits, on="circuitId", suffixes=("_race", "_circuit"))

# Merge with results
race_details = pd.merge(race_details, results, on="raceId", suffixes=("", "_results"))

# Merge with drivers
race_details = pd.merge(race_details, drivers, on="driverId", suffixes=("", "_drivers"))

# Merge with constructors
race_details = pd.merge(race_details, constructors, on="constructorId", suffixes=("", "_constructors"))

print("Columns after merging:", race_details.columns)

print("Selecting relevant columns...")
# Select relevant columns
race_details = race_details[[
    "raceId", "circuitName", "year", "round", "name", "date", "driverName", 
    "driverNationality", "constructorName", "position", "points", "grid", "fastestLapTime"
]]

# Rename columns for consistency
race_details.rename(columns={
    "name": "raceName",
    "date": "raceDate",
    "grid": "startingGrid",
    "fastestLapTime": "fastestLap"
}, inplace=True)

# Additional cleaning or feature engineering
print("Performing additional data cleaning and enrichment...")
race_details["position"] = pd.to_numeric(race_details["position"], errors="coerce").fillna(-1).astype(int)
race_details["year"] = race_details["year"].astype(int)
race_details["round"] = race_details["round"].astype(int)
race_details["podium"] = race_details["position"].apply(lambda x: "Yes" if x in [1, 2, 3] else "No")
race_details["fastestLap"] = race_details["fastestLap"].fillna("N/A")
race_details["points_per_grid"] = race_details["points"] / (race_details["startingGrid"] + 1)

print("Saving processed data...")
race_details.to_csv(PROCESSED_FILE, index=False)

print(f"Preprocessed data saved to {PROCESSED_FILE}")
print("Preprocessing completed! Here's a summary:")
print(race_details.head())
print(f"Total rows: {len(race_details)}, Total columns: {len(race_details.columns)}")
