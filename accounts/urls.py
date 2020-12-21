from django.urls import path, include

from accounts.views import register, login, dashboard, logout
from cars.views import cars, car_detail, search

urlpatterns = [
    path('register/', include('django.contrib.auth.urls')),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]