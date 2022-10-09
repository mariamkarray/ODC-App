from django.contrib import admin
from .models import Course, Skill, Supplier 
# Register your models here.

admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(Supplier)
