from django.contrib import admin
from .models import ufc_fighter, weight_division

# Register your models here.
admin.site.register(ufc_fighter)
admin.site.register(weight_division)