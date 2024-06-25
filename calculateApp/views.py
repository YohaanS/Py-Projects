from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def calculate(request):
    return render(request, "calculator.html")

def firstpage(request):
    return render(request, "firstpage.html")
