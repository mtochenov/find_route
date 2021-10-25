from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .forms import CityForm
from .models import City


__all__ = (
    "CityListView", "CityDetailView", "CityCreateView", "CityUpdateView", "CityDeleteView",
)


class CityListView(ListView):
    paginate_by = 4
    model = City
    template_name = "cities/cities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context["form"] = form
        return context


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):  # Требуется аутентификация
    model = City
    form_class = CityForm
    template_name = "cities/create.html"
    success_url = reverse_lazy("cities:cities")  # Заменяет def get_absolute_url в models.py
    success_message = "Город успешно добавлен"


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = "cities/update.html"
    success_url = reverse_lazy("cities:cities")
    success_message = "Город успешно отредактирован"


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = "cities/delete.html"
    success_url = reverse_lazy("cities:cities")
