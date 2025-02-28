from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from .models import *
from django.db.models import Sum

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

from django.db.models import Sum

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_reportcard']
    ordering = ['student_rank']
    def total_marks(self, obj):
        subject_marks = subjectMarks.objects.filter(student=obj.student)
        marks = ( subject_marks.aggregate(marks = Sum('marks'))) # FIXED
        return marks['marks']

    #total_marks.short_description = 'Total Marks'  # Optional: Sets column name in admin panel

admin.site.register(ReportCard, ReportCardAdmin)

