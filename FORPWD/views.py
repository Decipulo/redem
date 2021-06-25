from django.shortcuts import render, redirect
from .models import login, Account, Applicant
from .forms import ApplicantForm, LoginForm

# Create your views here.
def loginpage(request):
    Signup=login.objects.create(
		Username = request.POST.get('Username', False),
		Email = request.POST.get('Email', False),
		password = request.POST.get('password', False),
		)
    return redirect('/login')
    return render(request, 'login.html')


def homepage(request):
    context={}

    form = ApplicantForm()
    if request.method == 'POST':
        form = ApplicantForm (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('mainpage.html')

    context['form'] = form
    return render (request, "homepage.html", context)


def myaccount(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["dataset"] = Applicant.objects.all()

    return render(request, "myaccount.html", context)
def discussion(request):

    return render (request, 'discussions.html')

def logout(request):

    return render (request, 'login.html')

def aboutuspage(request):
    return render (request, 'aboutus.html')

def Market(request):
    return render (request, 'shop.html')




