from django import forms
from trains.models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(label="Поезд",
                           widget=forms.TextInput(attrs={
                               "class": "form-control",
                               "placeholder": "Введите название поезда"
                           }))

    travel_time = forms.IntegerField(label="Время в пути",
                                     widget=forms.NumberInput(attrs={
                                           "class": "form-control",
                                           "placeholder": "Укажите время в пути"
                                     }))  # forms.ImageField - неверный формат ввода данных

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

    # def __init__(self, *args, **kwargs):  # comment on function was added
    #     super(TrainForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Train
        fields = "__all__"  # "name", "travel_time", "departure_city", "destination_city"
