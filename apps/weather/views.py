import requests
from django.shortcuts import render
import logging


def render_view(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d7ca28c2bef8ad46a170d61b4dc1f115"
    city = "Helsinki London"
    formatted_url = url.format(city)
    res = requests.get(formatted_url).json()

    if res["cod"] != 200:
        logging.error("Error in getting weather data for city", extra={"city": city, "status_code": res["cod"]})
        return render(request, "weather/index.html", {"error_message": res["message"]})

    weather_data = {
        "city": city,
        "temperature": int(res["main"]["temp"]),
        "description": res["weather"][0]["description"],
        "icon": res["weather"][0]["icon"]
    }

    return render(request, "weather/index.html", {"weather_data": [weather_data]})

