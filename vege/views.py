from django.shortcuts import render, redirect
from .models import *

# Create your views here.

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

