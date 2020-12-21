
from django.urls import path

from pages import views
from pages.views import home, about, services, contact, add

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),
    path('contact/', contact, name="contact"),
    path('add/', add, name= 'add')
]