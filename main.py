import geocoder
from api import location, weather
import parser
from datetime import datetime as dt


def main():

    print("~☀️~☀️~☀️~☀️~☀️~☀️~☀️~☀️~☀️~~☀️~☀️~☀️~☀️~☀️~☀️~☀️~\nWelcome to Will I Be Depressed! :D")

    zip = input("Enter your ZIP code, or press enter for WillIBeDepressed to detect your location automatically: ").strip()

    while zip != "" and (not (zip.isdigit() and (len(zip) == 5 or len(zip) == 9))):
        zip = input("Please enter ZIP code or press enter: ")

    if zip == "":
        g = geocoder.ip("me")
        latlon_list = g.latlng
        lat, lon = latlon_list
    elif zip != "":
        if not (zip.isdigit() and (len(zip) == 5 or len(zip) == 9)):
            print("Invalid ZIP code format. Please enter a 5 or 9 digit ZIP code.")
            return
        else:
            coords = location.get_coordinates_from_zipcode(zip)
            if not coords:
                print("Could not determine coordinates for the provided ZIP code.")
                return
            else:
                lat, lon = coords
    print(f"Found coordinates: Lat {lat}, Lon {lon}")

    forecast_url, city, state = weather.get_forecast_url(lat, lon)

    # Get current time
    current_hour = dt.now().hour

    # Determine if we should show today or tomorrow's forecast
    show_tomorrow = current_hour >= 12

    day = "tomorrow" if show_tomorrow else "today"
    print(f"\nGetting the weather forecast for {day} in {city.title()}, {state.upper()}...")

    # Get forecast data
    forecast_data = weather.get_forecast(forecast_url)

    parsed_forecast = parser.parse_forecast(forecast_data, is_tomorrow=show_tomorrow)

    results = parser.calculate_depression(parsed_forecast)

    if results["depressed"]:
        print(f"\nYou are going to be depressed {day}. Sorry :/")
    else:
        print(f"You aren't going to be depressed {day}!! Yay!! :D")
    print(f"{day.capitalize()} will be {results['temperature']} F and {results['view'].lower()}. There is a {results['prob_precipitation']}% chance of rain with winds up to {results['wind_max']} mph.")


if __name__ == "__main__":
    main()
