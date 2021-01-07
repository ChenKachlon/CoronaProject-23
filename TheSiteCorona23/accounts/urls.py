from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('department/', views.departmentPage, name='department'),
    path('patients/', views.patients, name='patients'),
    path('beds/', views.beds, name='beds'),
    path('ventilators/', views.ventilators, name='ventilators'),
    path('add_patient/', views.addPatients, name='add_patient'),
    path('update_patient/<str:pk>', views.updatePatient, name='update_patient'),
    # path('search_patient/<str:pk>', views.SearchPatient, name='search_patient'),


    path('delete_patient/<str:pk>', views.deletePatient, name='delete_patient'),
    path('add_bed/', views.addBeds, name='add_bed'),
    path('update_beds/<str:pk>', views.updateBeds, name='update_beds'),
    path('delete_bed/<str:pk>', views.deleteBed, name='delete_bed'),
    path('add_ven/', views.addVen, name='add_ven'),
    path('update_ven/<str:pk>', views.updateVen, name='update_ven'),
    path('delete_ventilators/<str:pk>', views.deleteVen, name='delete_ventilators'),
    path('set_concentration/<str:pk>', views.setConcentration, name='set_concentration'),
    # path('max', views.MaxConcentration, name='max'),
    # path('staff/<str:pk>/', views.staff, name='staff_page'),
]
