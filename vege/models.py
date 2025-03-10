from django.db import models
# The User model is Django's default user authentication model, which is part of the django.contrib.auth module.
# It provides built-in authentication features like user registration, login, logout, and password management.
'''


'''
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    #model.CASCADE means if any user deletes its account then all the receipes uploaded by him/her will be deleted
    #model.SET_NULL means it set null value at the place of user receipes
    #model.SET_DEFAULT means it sets default values
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="receipe")
    view_count = models.IntegerField(default=1)

class Department(models.Model):
    department = models.CharField(max_length=100)
    #__str__ Method → Returns the department name when the object is printed or displayed.
    def __str__(self) -> str:
        return self.department
    '''
    Meta Class (ordering = ['department']) → Specifies that when querying the Department model,
      results should be sorted alphabetically by the department field.
    '''
    class Meta:
        ordering = ['department']


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class Subject(models.Model):
    Subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Subject_name


class Student(models.Model):
    #on_delete=models.CASCADE  means if department is deleted then all students associated with that department will also delete
    #here many to one relationship exits means many students can belongs to same department
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    '''
        A One-to-One relationship ensures that each student has a unique student_id entry.
        on_delete=models.CASCADE → If a StudentID is deleted, the student record is also deleted.

    '''
    student_id     = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name    = models.CharField(max_length=100)
    student_email   = models.EmailField(unique=True)
    student_age     = models.IntegerField(default=18)
    student_address = models.TextField()

    #if we create any object suppose s1 of Student calss and if we print s1 it will call below method and print student name
    def __str__(self)-> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'

class subjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.Subject_name}'

    class Meta:
        unique_together = ['student', 'subject']


class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="reportcard", on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_reportcard = models.DateField(auto_now_add=True)  

    class Meta:
        unique_together = ['student_rank','date_of_reportcard']
    '''
    SQL queries
    //to get data in asending order
    vege = Receipe.objects.all().order_by('view_count')
    //to get data in decending order 
    vege = Receipe.objects.all().order_by('-view_count')
    //to get top or bottom limited data basically limit clause
    \\this will return top 3 records
     vege = Receipe.objects.all().order_by('-view_count')[0:2]
     //to get specific data like where clause
     Receipe.objects.filter(view_count__gte = 50)
     -> __gte is works like oprator (>= greater than or equal to)
     ->__lte (<= less than or equal to)

     >queryset = Student.objects.filter(student_name__startswith='A')
     -> this will return all student whose name starts with A
    
     >queryset = Student.objects.filter(student_email__endswith='.org')
     -> this will return all student whose email ends with .org

     > queryset = Student.objects.filter(student_name__icontains='An')
     -> this will return all student whose name contains An

     >queryset[0].department.department
     -> this will return department of first student in queryset

     >queryset = Student.objects.filter(department__department = 'Mecanical')
            -->department__department='Mecanical'
        department refers to a ForeignKey relationship in the Student model.
        department__department accesses a field (department) in the related Department model.
        'Mecanical' is the value being filtered.
        >queryset = Student.objects.filter(department__department__in = d)
        -->department__department__in = d   

        >queryset = Student.objects.exclude(department__department = 'Civil')
        -->exclude() is the opposite of filter() and returns all objects except those matching the given conditions

        >queryset.exists()
        -->exists() returns True if the QuerySet contains at least one object, False otherwise.

        >queryset.values()[0]
        -->values() returns a dictionary-like object for each object in the QuerySet.

        >queryset[0:50]
        -->returns the first 50 objects in the QuerySet.  

        Agreegate functions works on column  

      ->  Student.objects.aggregate(Avg('student_age'))
      ->  Student.objects.aggregate(Max('student_age'))
        annotate function used to work on two columns
        ->Student.objects.values('student_age').annotate(Count('student_age'))             
    '''