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

For detailed documentation and usage, please refer to the API documentation at `/docs` on the local server.

## Driver Name Format

When making requests to the endpoints that require specifying a driver (e.g., for performance data, trends, etc.), you should use the driver's **abbreviation** as the driver name.

### Example of Driver Abbreviations:
- **VER** - Max Verstappen
- **HAM** - Lewis Hamilton
- **SAI** - Carlos Sainz
- **LEC** - Charles Leclerc
- **ALO** - Fernando Alonso
- **PER** - Sergio Perez

These abbreviations can be used to query specific data for each driver. For example:
- To get Max Verstappen's performance for the Monaco GP in 2023, use **`/prediction/driver-performance/2023/Monaco/VER`**
- To get the trends for Lewis Hamilton in 2023, use **`/prediction/driver-trends/2023/HAM`**

You can find the full list of driver abbreviations on the official F1 website or other resources that provide current driver lists.

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
