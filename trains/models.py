from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City


class Train(models.Model):
    """Задаем поля в таблице: имя, время_в_пути, город_отправления и город_назначения"""
    name = models.CharField(max_length=50, unique=True, verbose_name="Номер поезда")
    travel_time = models.PositiveSmallIntegerField(verbose_name="Время в пути")

    departure_city = models.ForeignKey(City, on_delete=models.CASCADE,  # CASCADE - Приудалении данных в одной таблице удаляются и связанные данные в др. таблицах
                                       # null=True, blank=True,
                                       related_name="departure_city_set",  # Указание имени для набора (множества) экземпляров класса Train
                                       verbose_name="Город отправления"
                                       )
    destination_city = models.ForeignKey("cities.City", on_delete=models.CASCADE,  # К модели City можно обратиться не только импортировав такую модель,
                                         related_name="destination_city_set",  # from .. import City, но и указав напрямую название приложения и имя модели
                                         verbose_name="Город назначения"
                                         )

    def __str__(self):
        return f'Поезд {self.name} из города {self.departure_city} в город {self.destination_city}'

    class Meta:
        verbose_name = "Поезд"
        verbose_name_plural = "Поезда"
        ordering = ["name"]

    def clean(self):
        """В данной функции мы проверяем уникальность новой записи и поднимаем ошибку в случае, если запись не уникальна"""
        if self.departure_city == self.destination_city:
            raise ValidationError("Города отправления и назначения должны отличаться")
        qs = Train.objects.filter(departure_city=self.departure_city,
                                  destination_city=self.destination_city,
                                  travel_time=self.travel_time,
                                  ).exclude(pk=self.id)
        # Запись Train аналогична записи self.__class__
        if qs.exists():
            raise ValidationError("Изменить время в пути")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
