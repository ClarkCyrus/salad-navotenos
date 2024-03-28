from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('salad/<int:pk>/', views.salad_detail, name='salad_detail'),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('employee_signin/', views.employee_signin, name="employee_signin"),
    path('employee_signup/', views.employee_signup, name="employee_signup"),
    path('signout/', views.signout, name='signout'),
]