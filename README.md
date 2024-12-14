# f1-season-predictor

An app that predicts F1 season standings and race outcomes using historical and live data.

## Features

- **Predict race outcomes** based on historical performance data for both drivers and teams.
- **Fetch race data** for specific years and Grand Prix events, including lap times, qualifying results, weather conditions, and more.
- **Analyze driver trends** and performance across multiple races in a season.
- **Retrieve season standings** and historical data for a detailed view of performance.

## Setup

### Prerequisites

- Python 3.9+
- Virtual environment (`venv`) setup
- Installed dependencies:
  - `fastapi`
  - `uvicorn`
  - `fastf1`
  - `pytest` (for testing)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/f1-season-predictor.git
   cd f1-season-predictor
   ```
2. Set up the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4.Run the app:
```bash
uvicorn app.main:app --reload
```
The app will be running on http://127.0.0.1:8000.
## Here is a quick overview of the main endpoints:

### 1. **Historical Data**
   - Fetch historical data for a specific year, optionally filtered by driver.

### 2. **Driver Standings**
   - Retrieve the driver standings for a specific season.

### 3. **Race Prediction**
   - Fetch race data for a specific year and grand prix (e.g., Monaco 2023).

### 4. **Driver Performance**
   - Fetch performance data for a specific driver in a specific race.

### 5. **Race Results**
   - Fetch race results for all drivers in a specific race.

### 6. **Qualifying Results**
   - Retrieve qualifying results for a specific race.

### 7. **Weather Data**
   - Fetch weather data for a specific race.

### 8. **Driver Trends**
   - Fetch performance trends for a specific driver over a given year.

For detailed documentation and usage, please refer to the API documentation at `/docs` on the local server.

## Tests

To run the tests for this app, follow these steps:

1. Ensure that the virtual environment is activated:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install the required testing dependencies if you haven't already:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests using pytests:

   ```bash
   pytest
   ```
