from django.db import models
from dataclasses import dataclass


# Create your models here.
class City(models.Model):
    """
    City model
    """
    name: str = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "cities"


@dataclass
class WeatherData:
    __slots__ = ["city", "temperature", "description", "icon"]
    city: str
    temperature: int
    description: str
    icon: str


