from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method == 'POST':
        #this is used to get data
        data = request.POST
        #this is used to get data in the form of file
        image = request.FILES.get('image')
        name = data.get('name')
        description = data.get('description')
        
        Receipe.objects.create(
            name=name,
            description=description,
            image=image,
        )
        # this is for the removing warning of resummition
        return redirect('/receipes/')

    queryset = Receipe.objects.all()
    print(queryset)
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def delete_rep(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')

