from django.urls import path, include
from . import views
from .views import *
# TrainListView, TrainDetailView, TrainCreateView, TrainUpdateView, TrainDeleteView

app_name = "trains"

urlpatterns = [
    path('', TrainListView.as_view(), name="trains"),
    path('<int:pk>/', TrainDetailView.as_view(), name="detail"),
    path('create/', TrainCreateView.as_view(), name="create"),
    path('<int:pk>/update/', TrainUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', TrainDeleteView.as_view(), name="delete"),
    # path('', views.trains, name="trains"),
]
