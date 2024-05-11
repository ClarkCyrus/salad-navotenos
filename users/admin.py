from django.contrib import admin
from . models import Salad_Customer, Salad_Employee, Crochet_Customer, Crochet_Employee

admin.site.register(Salad_Customer)
admin.site.register(Salad_Employee)
admin.site.register(Crochet_Customer)
admin.site.register(Crochet_Employee)