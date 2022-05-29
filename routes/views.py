from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from cities.models import City
from trains.models import Train
from .forms import RouteForm, RouteModelForm
from .models import Route
from .utils import get_routes


def home(request):
    form = RouteForm
    return render(request, "routes/home.html", {"form": form})


def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)

            except ValueError as err:
                messages.error(request, err)
                return render(request, "routes/home.html", {"form": form})

            return render(request, "routes/home.html", context)

        return render(request, "routes/home.html", {"form": form})

    else:
        form = RouteForm()
        messages.error(request, "Не корректные данные")
        return render(request, "routes/home.html", {"form": form})


def add_route(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data["total_time"])
            departure_city_id = int(data["departure_city"])
            destination_city_id = int(data["destination_city"])
            trains = data["trains"].split(",")
            trains_list = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_list).select_related("departure_city", "destination_city")
            cities = City.objects.filter(id__in=[departure_city_id, destination_city_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    "departure_city": cities[departure_city_id],
                    "destination_city": cities[destination_city_id],
                    "travel_time_common": total_time,
                    "trains": qs,
                         }
            )
            context["form"] = form
        return render(request, "routes/add_route.html", context)
    else:
        messages.error(request, "Невозможно сохранить несуществующий маршрут")
        return redirect("/")


def save_route(request):
    if request.method == "POST":
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Маршрут успешно сохранен")
            return redirect("/")
        return render(request, "routes/add_route.html", {"form": form})
    else:
        messages.error(request, "Невозможно сохранить несуществующий маршрут")
        return redirect("/")


class RoutesViewList(ListView):
    paginate_by = 10
    model = Route
    template_name = "routes/list_routes.html"


class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = "routes/detail_route.html"
