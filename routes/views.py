from django.contrib import messages
from django.shortcuts import render
from .forms import RouteForm
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
