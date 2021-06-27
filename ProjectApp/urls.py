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
from django.conf.urls import url


urlpatterns = [

    path('admin/',admin.site.urls),
    path('homes/',views.home, name="homes/"),
    path('', views.loginpage, name="first"),
    path('login/loginpage', views.loginpage, name="login/"),
    path('respondent/<str:pk_test>/', views.respondent, name="respondent"),
    path('create_respondent/', views.CompleteProfile, name="create_respondent"),
    path('home/',views.homepage, name='home/'),
    path('discussion/',views.discussion, name='discussion/'),
    path('login/' ,views.logout, name='login/'),
    
    path('shop/' ,views.Market, name='shop/'),
    path('myaccount/' ,views.myaccount, name = 'myaccount/'),
    path('about/',views.index, name='about/'),
    url(r'^about/create$', views.create, name='create'),
    url(r'^about/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^about/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^about/delete/(?P<id>\d+)$', views.delete, name='delete'),

]
