from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from .models import *

admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

'''
    This class is used to customize how the SubjectMarks model 
        appears in the Django admin interface.
      The list_display attribute determines which fields of the 
      model should be displayed as columns in the admin panel.
'''

class SubjectMarksAdmin(ModelAdmin):
    list_display = ['student', 'subject', 'marks']


admin.site.register(subjectMarks,SubjectMarksAdmin)

