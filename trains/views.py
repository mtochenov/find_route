from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView, ListView)
from trains.forms import TrainForm
from trains.models import Train

__all__ = (
    "TrainDetailView",
    "TrainCreateView",
    "TrainUpdateView",
    "TrainDeleteView",
    "TrainListView",
)

# def trains(request, page_number=None, pk=None):
#     qs = Train.objects.all()
#     list = Paginator(qs, 4)
#     page_number = request.GET.get('page')
#     page_obj = list.get_page(page_number)
#     data = {
#         "title": "Список Поездов",
#         "page_obj": page_obj,
#             }
#
#     return render(request, "trains/trains.html", data)


class TrainListView(ListView):
    paginate_by = 4
    model = Train
    template_name = "trains/trains.html"


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = "trains/detail.html"


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/create.html"
    success_url = reverse_lazy("trains:trains")  # Заменяет def get_absolute_url в models.py
    success_message = "Поезд успешно добавлен"


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/update.html"
    success_url = reverse_lazy("trains:trains")
    success_message = "Поезд успешно отредактирован"


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    template_name = "trains/delete.html"
    success_url = reverse_lazy("trains:trains")

    def get(self, request, *args, **kwargs):
        messages.success(request, "Поезд успешно удален")  # Удаление объекта без перехода на
        return self.post(request, *args, **kwargs)  # соответствующую страницу html и подтверждения
