from django.contrib import admin
from .models import Applicant,Account,Discussion,Comment,ProductItem,Variants,ItemVariant,OrderItem,Address,BAYAD,Coupon,OrderDetails,Refund
# Register your models here.Address,

admin.site.register(Applicant)
admin.site.register(Account)
admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(ProductItem)
admin.site.register(Variants)
admin.site.register(ItemVariant)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(BAYAD)
admin.site.register(Coupon)
admin.site.register(OrderDetails)
admin.site.register(Refund)