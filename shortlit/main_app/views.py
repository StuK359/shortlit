from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>BOOOOKS</h1>')

def about(request):
    return render(request, 'about.html')