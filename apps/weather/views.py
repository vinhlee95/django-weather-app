from django.shortcuts import render


def render_view(request):
    return render(request, "weather/index.html")

