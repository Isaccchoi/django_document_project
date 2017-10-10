from django.contrib import admin

# Register your models here.
from model.models import (
    User,
    Car, Manufacturer,
    Pizza, Topping,
    FacebookUser, InstagramUser,
    Idol, Group, Membership,
)

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)