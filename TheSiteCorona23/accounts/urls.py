from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('patients/', views.patients),
    path('beds/', views.beds),
    path('ventilators/', views.ventilators),

]