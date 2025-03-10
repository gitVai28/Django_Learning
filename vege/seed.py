# this is for to genrate fake data

from faker import Faker
fake = Faker()
import random
from .models import *
from django.db.models import Sum

def create_subject_marks():
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
                subjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)   
                )
    except Exception as e:
        print(e)

def seed_db(n=10)->None:
    try:
        for i in range(0, n):

            
            dpt_obj = Department.objects.all()
            random_idx = random.randint(0,len(dpt_obj)-1)
            dpt = dpt_obj[random_idx]
            student_id  = f'STU-0{random.randint(100, 999)}'
            student_name   = fake.name()
            student_email  = fake.email()
            student_age    = random.randint(20,30)
            student_address = fake.address()


            sutdent_id_obj = StudentID.objects.create(student_id = student_id)
            student_obj = Student.objects.create(
                student_id = sutdent_id_obj,
                department = dpt,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address

                
            )
    except Exception as e:
        print(e)

def generate_rank():
    current_rank = -1
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i = 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
        i += 1