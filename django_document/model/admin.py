from django.contrib import admin

# Register your models here.
from model.models import User, Car, Manufacturer

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Manufacturer)
