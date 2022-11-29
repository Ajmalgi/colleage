from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'colleage_templates/index.html')

def about(request):
    return render(request,'colleage_templates/about.html')

def courses(request):
    return render(request,'colleage_templates/courses.html')

