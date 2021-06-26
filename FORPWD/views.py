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
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'base/index.html', context)

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/about')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'base/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/about')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/about')



