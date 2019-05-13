from django.urls import path
from . import views
from django.db import models
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('projects/', views.project_list, name="project_list"),
    path('projects/<slug:slug>', views.project_detail, name='project_detail'),
    path('resume/', views.resume, name="resume"),

]
