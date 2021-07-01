from django.urls import path, include
from . import views
from .views import TrainListView, TrainDetailView, TrainCreateView, TrainUpdateView, TrainDeleteView

urlpatterns = [
    path('', TrainListView.as_view(), name="trains"),
    path('<int:pk>/', TrainDetailView.as_view(), name="trains_detail"),
    path('create/', TrainCreateView.as_view(), name="trains_create"),
    path('<int:pk>/update/', TrainUpdateView.as_view(), name="trains_update"),
    path('<int:pk>/delete/', TrainDeleteView.as_view(), name="trains_delete"),
]
