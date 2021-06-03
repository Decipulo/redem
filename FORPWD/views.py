from django.shortcuts import render, redirect
from .models import Applicant
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def Regpage(request):

	return render(request,'html1.html')

def pendinglist(request):
	dem = Applicant.objects.all().order_by('date')
	return render(request,'html2.html', {'dem': dem})
