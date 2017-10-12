from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, School, Place, Restaurant, Champion

class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'champion_type', 'rank')
    list_editable = ('rank',)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Champion, ChampionAdmin)