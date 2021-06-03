from django.db import models
from django.shortcuts import reverse
from django.db.models import Sum
from django.contrib.auth.models import User
import os

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


	name = models.CharField(max_length=100, null=True)
	disability = models.CharField(max_length=200, choices= DISABILITY_CATEGORIES)
	address = models.CharField(max_length=100, null=True)
	age = models.CharField(max_length=200, null=True)
	Cnum = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)
	date = models.DateTimeField(auto_now=True, null=True)
	Idpic = models.FileField(upload_to="static/")



	def __str__(self):
		return self.name

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
        return self.title

    def get_product_url(self):
        return reverse("myapp:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("myapp:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("myapp:remove-from-cart", kwargs={
            'slug': self.slug
        })


class Variants(models.Model):
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # Type

    class Meta:
        unique_together = (
            ('item', 'name')
        )

    def __str__(self):
        return self.name

class ItemVariant(models.Model):
    variation = models.ForeignKey(Variants, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)  # Colors
    attachment = models.ImageField(blank=True)

    class Meta:
        unique_together = (
            ('variation', 'value')
        )

    def __str__(self):
        return self.value

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    item_variations = models.ManyToManyField(ItemVariant)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Productsenderaddress = models.CharField(max_length=200, null=True)
    cotumer_address = models.CharField(max_length=200, null=True)
    zipbnumber = models.CharField(max_length=200)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class BAYAD(models.Model):

	PAYMENT_CHOICES = (
		('Online', 'online'),
		('Cash On Delivery', 'Cod'),)


	stripe_charge_id = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)                          
	amount = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code



class OrderDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    referencecode = models.CharField(max_length=100, blank=True, null=True)
    itemwiths = models.ManyToManyField(OrderItem)
    datestart = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    sender_address = models.ForeignKey('Address', related_name='sender_address', on_delete=models.SET_NULL, blank=True, null=True)       
    costumer_address = models.ForeignKey('Address', related_name='costumer_address', on_delete=models.SET_NULL, blank=True, null=True)       
    payment = models.ForeignKey('BAYAD', on_delete=models.SET_NULL, blank=True, null=True)        
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)        
    Item_being_ready_fo_pick = models.BooleanField(default=False)
    tobedelivered = models.BooleanField(default=False)
    Order_received = models.BooleanField(default=False)
    refund_request = models.BooleanField(default=False)
    refund_approved = models.BooleanField(default=False)
	

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

class Refund(models.Model):

	PRODUCT_ISSUE = (('Damaged','damaged'),
		('Defective','defective'),('Wrong Item','wrong item'))


	order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
	product_issue = models.CharField(max_length=200, choices=PRODUCT_ISSUE, null=True)
	reason_description = models.TextField()
	imageevidence = models.ImageField(null=True)
	accepted = models.BooleanField(default=False)
    
	def __str__(self):
		return self.order