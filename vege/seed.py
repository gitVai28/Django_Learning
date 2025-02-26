# this is for to genrate fake data

from faker import Faker
fake = Faker()
import random
from .models import *
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