import requests
from django.shortcuts import render
import logging
from .models import City, WeatherData
from django.http import HttpResponse


def render_view(request):
    if request.method == "POST":
        city_name = request.POST.get("city_name", None)
        if city_name:
            City.objects.create(name=city_name)

    return render(request, "weather/index.html", {"weather_data": get_weather_data()})


def get_weather_data() -> [WeatherData]:
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d7ca28c2bef8ad46a170d61b4dc1f115"
    cities = City.objects.all()
    weather_data: [WeatherData] = []

    for city in cities:
        formatted_url = url.format(city.name)
        res = requests.get(formatted_url).json()

        if res["cod"] != 200:
            logging.error(f"Error in getting weather data for city {city.name}", extra={"city": city, "status_code": res["cod"]})
        else:
            weather_data.append(
                WeatherData(
                    city=city.name,
                    temperature=int(res["main"]["temp"]),
                    description=res["weather"][0]["description"].capitalize(),
                    icon=res["weather"][0]["icon"]
                )
            )

    return weather_data
