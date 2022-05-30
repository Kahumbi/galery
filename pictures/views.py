from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    
    return render(request, 'pictures/gallery.html', context)

def viewPhoto(request, pk):
    return render(request, 'pictures/photo.html')

def addPhoto(request):
    return render(request, 'pictures/add.html')