from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('patients/', views.patients, name='patients'),
    path('beds/', views.beds, name='beds'),
    path('ventilators/', views.ventilators, name='ventilators'),
    path('add_patient/', views.addPatients, name='add_patient'),
    path('add_bed/', views.addBeds, name='add_bed'),
    path('add_ven/', views.addVen, name='add_ven'),
    # path('staff/<str:pk>/', views.staff, name='staff_page'),

]