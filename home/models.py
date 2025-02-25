from django.db import models

# Create your models here.
# this file is used to create schemas of models
# django use default sql lite database
# migrations is very important folder which keeps track of changes in databse schema
# two cmmands py manage.py makemigrations -> makes chages in schema and make new mgration fiel
# py manage.py migrate -> apply changes in schema to database

class Student(models.Model):
    # id = models.AutoField  {this filed django adds automtically}
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.TextField()
    
    
    

# another modle

class Car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
    
    def __str__(self) -> str:
        return self.name


# Start Django Shell:
# python manage.py shell
# Import Model:
# from your_app.models import Student
# Create & Save Record:
# s = Student(name="pruthvi", email="pruthvi@gmail.com", age=16, address="kurduwadi")
# s.save()
# Fetch Data:
# s = Student.objects.get(id=1)  # Fetch single record  
# students = Student.objects.all()  # Fetch all records  
# filtered_students = Student.objects.filter(age=16)  # Filter records  
# Update Record:
# s = Student.objects.get(id=1)
# s.name = "updated name"
# s.save()
# Delete Record:
# s = Student.objects.get(id=1)
# s.delete()
#note that: after evry chage in code we have to restart django shell.

'''
CRUD OPRATIONS 
1] CREATE(three way to insert data)
 ->c = Car(name="nexon",speed = 200)
 ->c.save()
 ->Car.objects.create(name="alto", speed=100)
 ->car_dict = {"name":"nano","speed":60}
 -> Car.objects.create(**car_dict)
2] READ
 ->Car.objects.all() :- this will return something like below queryset
 <QuerySet [<Car: Car object (1)>, <Car: Car object (2)>, <Car: Car object (3)>]>
 ->to get proper queryset we have to write following function in model
      def __str__(self) -> str:
        return self.name
 -> which will return :- <QuerySet [<Car: nexon>, <Car: alto>, <Car: nano>]>
    car = <QuerySet [<Car: nexon>, <Car: alto>, <Car: nano>]> //store like this
    for i in car:
      print(f"{car.id} car name is {car.name} with speed {car.speed }")
 ->Car.objects.get(id = 2)
    <Car: alto> // this will return taht pericular obhject but id we enter id which is 
    not exists in database it will through error

 -> Car.objects.filter(id = 3)
    //instade of get if we use fillter it will return empty object as we enter 
    id which is not exists in database

3] UPDATE
    ->car = Car.objects.get(id = 1)
    ->car.name = "updated name"
    ->car.speed = 200
    ->car.save()

    ->Car.objects.filter(id = 1).update(name = "Creta dark edition limited")

4] DELETE
    ->car = Car.objects.get(id = 1)//to delete single record

    ->Car.objects.all().delete() // to delete all data from database
'''