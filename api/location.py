import requests


def get_coordinates_from_zipcode(zipcode):
    """Convert a zip code to latitude and longitude coordinates using a geocoding API

    Parameters
    ----------
    zipcode : str
        US zip code
    
    Returns
    -------
    tuple: (latitude, longitude) coordinates
    """

    # Using free census.gov geocoding API
    url = f"https://api.zippopotam.us/us/{zipcode}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "places" in data and data["places"]:
            lat = float(data["places"][0]["latitude"])
            lon = float(data["places"][0]["longitude"])
            return (lat, lon)

        print(f"Could not find coordinates for zip code {zipcode}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error getting coordinates from zip code: {e}")
        return None
