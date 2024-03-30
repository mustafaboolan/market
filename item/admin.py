from django.contrib import admin
from .models import Category,Item
# Register your models here.
# use to add new models to database my new tables
admin.site.register(Category)
admin.site.register(Item)
