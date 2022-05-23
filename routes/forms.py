from django import forms
from cities.models import City


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
