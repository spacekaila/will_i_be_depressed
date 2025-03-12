import requests

headers = {"User-Agent": "WillIBeDepressed/1.0"}


def get_forecast_url(lat, lon):
    grid_url = f"https://api.weather.gov/points/{lat},{lon}"

    try:
        response = requests.get(grid_url, headers=headers)
        response.raise_for_status()
        grid_data = response.json()

        # Get forecast url from grid data
        forecast_url = grid_data["properties"]["forecast"]
        city, state = grid_data["properties"]["relativeLocation"]["properties"]["city"],grid_data["properties"]["relativeLocation"]["properties"]["state"]

        return forecast_url, city, state

    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast url: {e}")
        return None


def get_forecast(forecast_url):

    try:
        # Get forecast data
        forecast_response = requests.get(forecast_url, headers=headers)
        forecast_response.raise_for_status()

        return forecast_response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast: {e}")
        return None
