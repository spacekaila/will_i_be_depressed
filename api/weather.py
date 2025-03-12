import requests


def get_forecast(lat, lon):

    headers = {"User-Agent": "WillIBeDepressed/1.0"}

    grid_url = f"https://api.weather.gov/points/{lat},{lon}"

    try:
        response = requests.get(grid_url, headers=headers)
        response.raise_for_status()
        grid_data = response.json()

        # Get forecast url from grid data
        forecast_url = grid_data["properties"]["forecast"]

        # Get forecast data
        forecast_response = requests.get(forecast_url, headers=headers)
        forecast_response.raise_for_status()

        return forecast_response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast: {e}")
        return None
