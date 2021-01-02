from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients, name='patients'),
    path('beds/', views.beds, name='beds'),
    path('ventilators/', views.ventilators, name='ventilators'),
    path('add_patient/', views.addPatients, name='add_patient'),

]