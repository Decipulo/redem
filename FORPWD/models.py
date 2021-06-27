from django.db import models
from django.shortcuts import reverse
from django.db.models import Sum
from django.contrib.auth.models import User
import os

class login(models.Model):
    Username = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Username

PRODUCTS_CHOICES = (
    ('Eye Wear','eye wear'),
    ('Wheelchairs','wheelchairs'),
    ('Hearingaids','hearingaids'),
    ('Crutches','crutches'),
    ('Tactiles','tactiles'),)


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


	User = models.CharField(max_length=100, null=True)
	disability = models.CharField(max_length=200, choices= DISABILITY_CATEGORIES)
	Address = models.CharField(max_length=100, blank=True)
	Age = models.IntegerField(default=0)
	ContactNumber = models.CharField(max_length=100, null=True)
	DateCreated = models.DateTimeField(auto_now_add=True, null=True)
	DateUpdated = models.DateTimeField(auto_now=True, null=True)
	Avatar = models.FileField(default='default.jpeg', upload_to='avatar')



	def __str__(self):
		return self.User

class Account(models.Model):

	name = models.ForeignKey(Applicant, on_delete=models.CASCADE, null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date = models.DateField(null=True, blank=True)
	birthdate = models.DateField()


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

class ProductItem(models.Model):


    itemname = models.CharField(max_length=100)
    price = models.FloatField()
    discountedprice = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=PRODUCTS_CHOICES, max_length=100)
    slugtourl = models.SlugField(max_length=200)
    itemdescription = models.TextField()
    itemImage = models.ImageField()

    def __str__(self):
        return self.itemname

class Donation(models.Model):
    Fullname = models.CharField(max_length=40)
    donate = models.CharField(max_length=40)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Fullname + " " + self.donate

    class Meta:
        ordering = ['created']

    class Meta:
        db_table = "db_donator"


