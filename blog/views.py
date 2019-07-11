from django.shortcuts import render
from django.utils import timezone
from .models import Post, Project, Art, Images
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, ProjectForm
from django.views import generic 
from django.urls import reverse, reverse_lazy

from django.shortcuts import render
from taggit.models import Tag


# def index(request):
#     return render(request, "build/index.html")

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    response = render(request, 'blog/post_detail.html', {
        'post': post
    })
    return response

def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/project_list.html', {'projects': projects})

def project_detail(request, slug):

    project = Project.objects.get(slug=slug)
    # Get all images
	# images = project.images.all()
    response = render(request, 'blog/project_detail.html', {
        "project": project })
    return response

def art_list(request):
    artifacts = Art.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/art_list.html', {'artifacts': artifacts})

def art_detail(request, slug):
    artifact = Art.objects.get(slug=slug)
    response = render(request, 'blog/art_detail.html', {
        "artifact": artifact
    })
    return response
