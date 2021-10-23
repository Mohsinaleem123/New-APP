from django.urls import path ,include
from . import views

urlpatterns =[
    path('',views.filter,name='filter'),
   
    path('find', views.find , name='find')
]