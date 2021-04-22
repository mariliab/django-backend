from django.contrib import admin
from .models import Ad, Category

classes = [Ad, Category]
admin.site.register(classes)