from django.shortcuts import render
from .models import Group,Chat

# Create your views here.
def index(request): 
    return render(request,'app/index.html')