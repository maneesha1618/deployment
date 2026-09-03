from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome to my django project")

def new(request):
    # return HttpResponse("New Project") 
    # Jinja Format : Dynamically data passing
    # context={
    #     'title': 'New Heading', 
    #     'message':'New Message'
    # }
    return render(request, 'index.html')

def add(request):
    return render(request,'add.html')