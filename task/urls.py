# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'task'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('index', views.index, name='index')
]