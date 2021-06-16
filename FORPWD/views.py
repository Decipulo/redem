from django.shortcuts import render, redirect
from .models import Applicant

# Create your views here.
def loginpage(request):

	return render(request,'login.html')

def homepage(request):

	 return render (request, 'homepage.html')

def discussion(request):

    return render (request, 'discussions.html')

def logout(request):

    return render (request, 'login.html')

def aboutuspage(request):
    return render (request, 'aboutus.html')

def Market(request):
    return render (request, 'shop.html')
