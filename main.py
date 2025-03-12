import geocoder
from api import weather, zipcode_to_latlong
import parser
from datetime import datetime as dt
import time

def main():

    print("~☀️~☀️~☀️~☀️~☀️~☀️~☀️~☀️~☀️~~☀️~☀️~☀️~☀️~☀️~☀️~☀️~\nWelcome to Will I Be Depressed! :D")

    #time.sleep(0.5)

    ip = input("\nEnter 0 to input your ZIP code, 1 for WillIBeDepressed to detect your location: ").strip()

    while ip != str(1) and ip != str(0):
        ip = input("Please enter 0 (for ZIP code) or 1 (detect location): ")
    ip = int(ip)

    if ip == 1:
        g = geocoder.ip("me")
        latlon_list = g.latlng
        lat, lon = latlon_list
    elif ip == 0:
        zipcode = input("Enter your ZIP code: ").strip()
        if not (zipcode.isdigit() and (len(zipcode) == 5 or len(zipcode) == 9)):
            print("Invalid ZIP code format. Please enter a 5 or 9 digit ZIP code.")
            return
        else:
            coords = zipcode_to_latlong.get_coordinates_from_zipcode(zipcode)
            if not coords:
                print("Could not determine coordinates for the provided ZIP code.")
                return
            else:
                lat, lon = coords
    print(f"Found coordinates: Lat {lat}, Lon {lon}")

    # Get current time
    current_hour = dt.now().hour

    # Determine if we should show today or tomorrow's forecast
    show_tomorrow = current_hour >= 12

    day = "tomorrow" if show_tomorrow else "today"
    print(f"\nGetting the weather forecast for {day}...")

    # Get forecast data
    forecast_data = weather.get_forecast(lat, lon)

    parsed_forecast = parser.parse_forecast(forecast_data)

    results = parser.calculate_depression(parsed_forecast)

    if results["depressed"]:
        print(f"\nYou are going to be depressed {day}. Sorry :/")
    else:
        print(f"You aren't going to be depressed {day}!! Yay!! :D")
    print(f"{day.capitalize()} will be {results["temperature"]} F and {results["view"].lower()}. There is a {results["prob_precipitation"]}% chance of rain with winds up to {results["wind_max"]} mph.")


if __name__ == "__main__":
    main()
