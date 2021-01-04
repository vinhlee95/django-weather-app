import requests
from django.shortcuts import render


def render_view(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d7ca28c2bef8ad46a170d61b4dc1f115"
    city = "Helsinki"
    formatted_url = url.format(city)
    res = requests.get(formatted_url).json()
    weather_data = {
        "city": city,
        "temperature": int(res["main"]["temp"]),
        "description": res["weather"][0]["description"],
        "icon": res["weather"][0]["icon"]
    }

    return render(request, "weather/index.html", {"weather_data": [weather_data]})

