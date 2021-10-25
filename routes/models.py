from django.db import models
from cities.models import City
from trains.models import Train


class Route(models.Model):
    """Задаем поля в таблице: имя, время_в_пути, город_отправления и город_назначения"""
    name = models.CharField(max_length=50, unique=True, verbose_name="Название маршрута")
    travel_time_common = models.PositiveSmallIntegerField(verbose_name="Общее время в пути")

    departure_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                       related_name="route_departure_city_set",
                                       verbose_name="Город отправления"
                                       )
    destination_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,
                                         related_name="route_destination_city_set",
                                         verbose_name="Город назначения"
                                         )

    trains = models.ManyToManyField(Train, verbose_name="Список поездов")

    def __str__(self):
        return f'Маршрут {self.name} из города {self.departure_city}'

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"
        ordering = ["travel_time_common"]
