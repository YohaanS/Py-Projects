from django.shortcuts import render, redirect
from .models import login
from .forms import PersonForm

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def calculate(request):
    return render(request, "calculator.html")

def firstpage(request):
    return render(request, "firstpage.html")

def signup(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/homepage')
    else:
        form = PersonForm()
    return render(request, 'Signup.html', {'form': form})
