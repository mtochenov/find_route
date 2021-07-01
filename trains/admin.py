from django.contrib import admin
from .models import Train


class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train

    list_display = ("name", "travel_time", "departure_city", "destination_city")
    list_editable = ("travel_time", )  # Внешние ключи из др. таблиц лучше не редактировать, т.к. повышается время работы из-за сверок каждого поля с др. таблицами


admin.site.register(Train, TrainAdmin)
