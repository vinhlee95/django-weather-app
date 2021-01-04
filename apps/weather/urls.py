from django.urls import path
from .views import render_view

app_name = "weather"

urlpatterns = [
    path("/view", render_view)
]