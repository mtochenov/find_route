from django.db import models
from django.urls import reverse


class City(models.Model):
    """Задает поле в таблице"""
    name = models.CharField(max_length=128, unique=True, verbose_name="Город",)

    def __str__(self):
        """ В таблицах меняет обозначение объекта с city.object(id) на имя собственное объекта"""
        return self.name

    class Meta:
        """Задает название ед. и множ. числа элементов в таблице"""
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ["name"]  # Сортировка объектов таблицы по имени

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
