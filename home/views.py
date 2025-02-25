from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#function based view
#returning responce
# def firstr(request):
#     return HttpResponse("<h1> hii.. vaishnavi this side.</h1>")

#rendering html template
#at the time of rendering it will autometically search for the templates folder but 
# after that we have to provide path manually eg. home/index.html
#context is used to send data to frontent from backend
def firstr(request):
    students = [
        {'name':'vaishnavi chavan','age':20},
        {'name':'priti gaikwad','age':23},
        {'name':'pratham gaikwad','age':30},
        {'name':'sai chavan','age':14},
        {'name':'parth nalawde','age':8}
    ]

    
    return render(request,'home/index.html', context = {'page':'Home','students':students})

def contact(request):
    
    return render(request,'home/contact.html', context={'page':'contact'})

def about(request):
    
    return render(request,'home/about.html',context={'page':'about'})