from django.urls import path
from . import views
from django.db import models
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('projects/', views.project_list, name="project_list"),
    path('projects/<slug:slug>', views.project_detail, name='project_detail'),
    path('art/', views.art_list, name="art_list"),
    path('art/<slug:slug>', views.art_detail, name='art_detail'),


]
