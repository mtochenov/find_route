from django import forms
from .models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(label="Поезд",
                           widget=forms.TextInput(attrs={
                               "class": "form-control",
                               "placeholder": "Введите название поезда"
                           }))

    travel_time = forms.ImageField(label="Время в пути",
                                   widget=forms.NumberInput(attrs={
                                       "class": "form-control",
                                       "placeholder": "Введите название поезда"
                                   }))

    departure_city = forms.ModelChoiceField(label="Город отправления",
                                            queryset=City.objects.all(),
                                            widget=forms.Select(attrs={
                                                "class": "form-control",
                                            }))

    destination_city = forms.ModelChoiceField(label="Город назначения",
                                              queryset=City.objects.all(),
                                              widget=forms.Select(attrs={
                                                  "class": "form-control",
                                              }))

    class Meta:
        model = Train
        fields = "__all__"  # "name", "travel_time", "departure_city", "destination_city"
