from django.contrib import admin
from .models import Thing, CoolThing
# Register your models here.

@admin.register(Thing)
class AdminThings(admin.ModelAdmin):
    pass

@admin.register(CoolThing)
class AdminCoolThings(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_cool']