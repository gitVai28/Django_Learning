from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator
'''
to flash error or success messages
for more information refer {django messages}
'''
from django.contrib import messages
# it will check username and password and return bollean value to authenticate user
#login is functrion to maintain session 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here. 
@login_required(login_url='/login')
def receipes(request):
    if request.method == 'POST':
        # Get data from form
        data = request.POST
        image = request.FILES.get('image')
        name = data.get('name')
        description = data.get('description')

        # Create a new recipe entry
        Receipe.objects.create(
            name=name,
            description=description,
            image=image,
        )
        return redirect('/receipes/')

    # Initialize queryset before filtering
    queryset = Receipe.objects.all()

    # Apply search filter if there is a search query
    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(name__icontains=search_query)

    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)


def update_rep(request, id):
    queryset = Receipe.objects.get(id =id)
    print(queryset)
    if request.method == 'POST':
        data = request.POST
         
        image = request.FILES.get('image')
        name = data.get('name')
        description = data.get('description')

        queryset.name = name
        queryset.description = description

        if image:
            queryset.image = image
        
        queryset.save()
        return redirect('/receipes/')
    
    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)

def delete_rep(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')
 
def loginp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

         
        if not User.objects.filter(username = username).exists():
            messages.error(request, "User does't exits !")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        #authenticate function returns None if password or username doesn't match
        if user is None:
            messages.error(request, "Invalid username or password !")

        else:
            # login maintain session for given user
            # default time of session is 14 days
            login(request,user)
            return redirect('/receipes/')
            
    return render(request , 'login.html')

def logoutp(request):
    logout(request) 
    return redirect('/login/')

def registerp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user  = User.objects.filter(username = username)

        if  user.exists():
            messages.info(request, "user already exists.")
            return redirect('/register/')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        # set_password is used to hash password it is inbuilt method in django user model
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully.")

    return render(request , 'register.html')

from django.db.models import Q,Sum

def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = Student.objects.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_age__icontains=search)
            )  # Fixed filter query

    paginator = Paginator(queryset, 25)  # Show 25 results per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/students.html', {'queryset': page_obj})


def see_marks(request, student_id):
    queryset = subjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    return render(request, 'report/see_marks.html', {'queryset':queryset , 'total_marks':total_marks})

