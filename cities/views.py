from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from rest_framework import permissions, authentication

from .forms import HtmlForm, CityForm
from .models import City

# from accounts.permissions import IsAuthenticated, AllowAny

__all__ = (
    "cities", "CityDetailView", "CityCreateView", "CityUpdateView", "CityDeleteView", "CityListView",
)


def cities(request, pk=None, page_number=None):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
    # if pk:
    # city = City.object.get(id=pk)
    # city = get_object_or_404(City, id=pk)
    # city = City.objects.filter(id=pk).first()
    # data = {
    #     "title": city,
    #     "object": city,
    # }
    # return render(request, "cities/details.html", data)

    form = CityForm()
    qs = City.objects.all()
    list = Paginator(qs, 4)
    page_obj = list.get_page(page_number)
    data = {
        "title": "Список городов",
        "page_obj": page_obj,
        "form": form,
    }

    return render(request, "cities/cities.html", data)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"
    authentication_classes = [authentication.TokenAuthentication]  # TODO Доработать
    permission_classes = [permissions.IsAdminUser]  # TODO Доработать


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):  # IsAuthenticated
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
    authentication_classes = [authentication.TokenAuthentication]  # TODO Доработать
    permission_classes = [permissions.IsAdminUser]  # TODO Доработать


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = "cities/delete.html"
    success_url = reverse_lazy("cities:cities")
    authentication_classes = [authentication.TokenAuthentication]  # TODO Доработать
    permission_classes = [permissions.IsAdminUser]  # TODO Доработать

    # def get(self, request, *args, **kwargs):
    #     messages.success(request, "Город успешно удален")  # Удаление объекта без перехода на
    #     return self.post(request, *args, **kwargs)  # соответствующую страницу html и подтверждения


class CityListView(ListView):
    paginate_by = 4
    model = City
    template_name = "cities/cities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context["form"] = form
        return context
