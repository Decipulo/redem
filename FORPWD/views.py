from django.shortcuts import render, redirect
from .models import login, Account, Applicant, Member
from .forms import ApplicantForm, LoginForm

# Create your views here.
def loginpage(request):
    return render(request, 'login.html')

def home(request):
    applicants = Applicant.objects.all()

    Applicants_summary = applicants.count()
    context = {
        "applicants":applicants,
        }

    return render(request, 'base/profile.html', context)

def respondent(request, pk_test):
	applicant = Applicant.objects.get(id=pk_test)

	context = {'applicant':applicant}
	return render(request, 'base/respondent.html',context)





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

    return render(request, 'mainpage.html')

def discussion(request):

    return render (request, 'discussions.html')

def logout(request):

    return render (request, 'login.html')

def aboutuspage(request):
    return render (request, 'aboutus.html')

def Market(request):
    return render (request, 'shop.html')

def CompleteProfile(request):
	form = ApplicantForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ApplicantForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'base/applicantform.html', context)

def index(request):
    donators = Donation.objects.all()
    context = {'donators': donators}
    return render(request, 'base/index.html', context)

def create(request):
    donators = Donation(Fullname=request.POST['firstname'], donate=request.POST['lastname'])
    donators.save()
    return redirect('/about')

def edit(request, id):
    donators = Donation.objects.get(id=id)
    context = {'donators': donators}
    return render(request, 'base/edit.html', context)

def update(request, id):
    donators = Donation.objects.get(id=id)
    donators.Fullname = request.POST['firstname']
    donators.donate = request.POST['lastname']
    donators.save()
    return redirect('/about')

def delete(request, id):
    donators = Donation.objects.get(id=id)
    donators.delete()
    return redirect('/about')



