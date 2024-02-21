from django.shortcuts import render
from .models import Group,Chat

# Create your views here.
def index(request,group_name): 
    print("Group Name:  ",group_name)
    return render(request,'app/index.html',{'groupname':group_name})