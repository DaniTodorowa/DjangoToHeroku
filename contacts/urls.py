from django.urls import path

from accounts.views import register, login, dashboard, logout
from cars.views import cars, car_detail, search
from contacts.views import inquiry

urlpatterns = [
    path('inquiry/', inquiry, name='inquiry'),

]