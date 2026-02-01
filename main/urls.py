from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('services/', views.services, name = 'services'),
    path('portfolios/', views.portfolios, name = 'portfolios',),
    path('contact/', views.contact, name = 'contact'),
    path('about', views.about, name= 'about'),
]
