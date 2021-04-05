from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentsInClass)
admin.site.register(ClassAssignment)
admin.site.register(SubmitAssignment)
