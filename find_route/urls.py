from django.contrib import admin
from django.urls import path, include

from routes.views import (
    home, find_routes,
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
]
