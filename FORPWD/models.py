from django.db import models
from django.shortcuts import reverse
from django.db.models import Sum
from django.contrib.auth.models import User
import os

	

class Account(models.Model):

    name = models.ForeignKey(Applicant, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    birthdate = models.DateField()

class Applicant(models.Model):


	DISABILITY_CATEGORIES = (
	('Psychosocial Disability','psychosocial disability'),
	('Chronic Illness', 'chronic illness'),
	('Learning Disability', 'learning disability'),
	('Mental Disability', 'mental disability'),
	('Visual Disability','visual disability'),
	('Orthopedic Disability','orthopedic disability'),
	('Communication Disability','communication disability'),
	)


	name = models.CharField(max_length=100, null=True)
	disability = models.CharField(max_length=200, choices= DISABILITY_CATEGORIES)
	address = models.CharField(max_length=100, null=True)
	age = models.CharField(max_length=200, null=True)
	Cnum = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)
	Idpic = models.FileField(upload_to="static/")



	def __str__(self):
		return self.name



class Discussion(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=200, null=True) 
    date = models.DateTimeField(auto_now_add=True)
    url=models.ImageField(upload_to="static/", blank=True)

    def __str__(self):
        return self.user

class Comment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Discussion,on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Product(models.Model):

	
    itemname = models.CharField(max_length=100)
    price = models.FloatField()
    discountedprice = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=PRODUCTS_CHOICES, max_length=100)
    slugtourl = models.SlugField(max_length=200)
    itemdescription = models.TextField()
    itemImage = models.ImageField()

    def __str__(self):
        return self.itemname
    
