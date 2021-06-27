from django.contrib import admin
from .models import Applicant,Account,Discussion,Comment,ProductItem,login,Donation
# Register your models here.Address,

admin.site.register(Applicant)
admin.site.register(Account)
admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(ProductItem)
admin.site.register(login)
admin.site.register(Donation)
