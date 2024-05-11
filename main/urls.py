from django.urls import path
from . import views

urlpatterns = [
    path('salad_home/', views.salad_home, name="salad_home"),
    path('salad_room/', views.salad_room, name="salad_room"),
    path('salad_signin/', views.salad_signin, name="salad_signin"),
    path('salad_signup/', views.salad_signup, name="salad_signup"),
    path('salad_employee_signin/', views.salad_employee_signin, name="salad_employee_signin"),
    path('salad_employee_signup/', views.salad_employee_signup, name="salad_employee_signup"),
    path('salad_signout/', views.salad_signout, name='salad_signout'),

    path('crochet_home/', views.crochet_home, name="crochet_home"),
    path('crochet_room/', views.crochet_home, name="crochet_room"),
    path('crochet_signin/', views.crochet_signin, name="crochet_signin"),
    path('crochet_signup/', views.crochet_signup, name="crochet_signup"),
    path('crochet_employee_signin/', views.crochet_employee_signin, name="crcohet_salad_employee_signin"),
    path('crochet_employee_signup/', views.crochet_employee_signup, name="crochet_employee_signup"),
    path('crochet_signout/', views.crochet_signout, name='crochet_signout'),
]