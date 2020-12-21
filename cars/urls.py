
from django.urls import path

from cars.views import cars, car_detail, search, create_car

urlpatterns = [
    path('', cars, name="cars"),
    path('<int:id>/', car_detail, name="car_detail"),
    path('search/', search, name='search'),
    path('add/', create_car, name='create car'),

]