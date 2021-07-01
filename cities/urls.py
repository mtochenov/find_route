from django.urls import path, include
from . import views
from .views import CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, CityListView

urlpatterns = [
    # path('', views.cities, name="cities"),
    path('', CityListView.as_view(), name="cities"),
    path('<int:pk>/', CityDetailView.as_view(), name="cities_detail"),
    path('create/', CityCreateView.as_view(), name="cities_create"),
    path('<int:pk>/update/', CityUpdateView.as_view(), name="cities_update"),
    path('<int:pk>/delete/', CityDeleteView.as_view(), name="cities_delete"),
]
