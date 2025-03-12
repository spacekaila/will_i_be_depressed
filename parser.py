from datetime import datetime


def parse_forecast(forecast_data, is_tomorrow=False):

    if not forecast_data or "properties" not in forecast_data:
        return None

    periods = forecast_data["properties"]["periods"]

    # Find relevant forecast period (today or tomorrow)
    target_period = None

    if is_tomorrow:
        # Look for tomorrow's daytime forecast
        for period in periods:
            if period["isDaytime"] and "night" not in period["name"].lower():
                if target_period is None or period['starTime'] > target_period['startTime']:
                    if datetime.fromisoformat(period["startTime"].replace("Z", "+00:00")).date() > datetime.now().date():
                        target_period = period
                        break
    else:
        # Look for today's forecast
        for period in periods:
            if datetime.fromisoformat(period["startTime"].replace("Z", "+00:00")).date() == datetime.now().date():
                target_period = period
                break
    if not target_period and periods:
        # Fallback to first period if we couldn't find the right one
        target_period = periods[0]

    return target_period


def calculate_depression(forecast):

    depressed = True

    view = "cloudy"
    wind_max = 0

    if ("sunny" in forecast["shortForecast"].lower()) or ("clear" in forecast["shortForecast"].lower()):
        if ("sunny" in forecast["shortForecast"].lower()):
            view = "sunny"
        else:
            view = "clear"
        if (forecast['probabilityOfPrecipitation']["value"] is None) or (forecast['probabilityOfPrecipitation']["value"] <= 15):
            if forecast["temperature"] >= 60:
                windspeed_list = forecast["windSpeed"].strip("mph").split("to")
                wind_max = int(windspeed_list[-1])
                if wind_max < 18:
                    depressed = False
    if forecast['probabilityOfPrecipitation']["value"] is None:
        prob_precipitation = "0"
    else:
        prob_precipitation = forecast['probabilityOfPrecipitation']["value"]

    results = {"depressed" : depressed,
               "view" : view,
               "prob_precipitation" : prob_precipitation,
               "temperature" : forecast["temperature"],
               "wind_max" : wind_max}
    return results
