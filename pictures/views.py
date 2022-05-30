from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'pictures/gallery.html')

def viewPhoto(request, pk):
    return render(request, 'pictures/photo.html')

def addPhoto(request):
    return render(request, 'pictures/add.html')