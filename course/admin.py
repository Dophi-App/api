from django.contrib import admin
from .models import *

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(CourseOffering)
admin.site.register(Professor)