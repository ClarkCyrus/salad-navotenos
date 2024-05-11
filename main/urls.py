from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.salad, name="room"),
    path('salad_signin/', views.salad_signin, name="salad_signin"),
    path('salad_signup/', views.salad_signup, name="salad_signup"),
    path('salad_employee_signin/', views.salad_employee_signin, name="salad_employee_signin"),
    path('salad_employee_signup/', views.salad_employee_signup, name="salad_employee_signup"),
    path('signout/', views.signout, name='signout'),
]