from django.contrib import admin

# Register your models here.

from apps.ingreso.models import Ingreso
admin.site.register(Ingreso)