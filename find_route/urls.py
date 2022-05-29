from django.contrib import admin
from django.urls import path, include

from routes.views import (
    home, find_routes, add_route, save_route, RoutesViewList, RouteDetailView
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', include('main.urls')),
    path('cities/', include('cities.urls')),
    path('trains/', include('trains.urls')),
    path('accounts/', include('accounts.urls')),
    # path('routes/', include('routes.urls')),
    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_route/', add_route, name='add_route'),
    path('save_route/', save_route, name='save_route'),
    path('list_routes/', RoutesViewList.as_view(), name='list_routes'),
    path('detail_route/<int:pk>/', RouteDetailView.as_view(), name='detail_route'),
]
