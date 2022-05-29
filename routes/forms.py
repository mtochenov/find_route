from django import forms
from cities.models import City
from routes.models import Route
from trains.models import Train


class RouteForm(forms.Form):
    departure_city = forms.ModelChoiceField(
        label="Город отправления",
        queryset=City.objects.all(),
        empty_label=None,
        widget=forms.Select(
            attrs={"class": "form-control js-example-basic-single", }
        )
    )

    destination_city = forms.ModelChoiceField(
        label="Город назначения",
        queryset=City.objects.all(),
        empty_label=None,
        widget=forms.Select(
            attrs={"class": "form-control js-example-basic-single", }
        )
    )

    cities = forms.ModelMultipleChoiceField(
        label="Через города",
        queryset=City.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple", }
        )
    )

    route_time = forms.IntegerField(
        label="Время в пути",
        widget=forms.NumberInput(
            attrs={"class": "form-control",
                   "placeholder": "Укажите время в пути",
                   }
        )
    )


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(
        label="Название маршрута",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите название маршрута",
        })
    )

    departure_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.HiddenInput()
    )

    destination_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.HiddenInput()
    )

    trains = forms.ModelMultipleChoiceField(
        queryset=Train.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={"class": "form-control d-none", }
        )
    )

    travel_time_common = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Route
        fields = "__all__"
