"""ProjectApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FORPWD import views


urlpatterns = [

    path('admin/',admin.site.urls),
    path('', views.loginpage, name="first"),
    path('home/',views.homepage, name='home/'),
    path('discussion/',views.discussion, name='discussion/'),
    path('login/' ,views.logout, name='login/'),
    path('about/' ,views.aboutuspage, name='about/'),
    path('shop/' ,views.Market, name='shop/'),
    path('myaccount/', views.Account, name = 'myaccount'),

]
