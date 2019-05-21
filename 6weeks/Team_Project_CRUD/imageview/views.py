from django.shortcuts import render
from .models import Imageview
# Create your views here.

def imageview(request) :
    imageviews = Imageview.objects
    return render(request, 'image.html', {'imgclass':imageviews})