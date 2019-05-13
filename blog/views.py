from django.shortcuts import render
from django.utils import timezone
from .models import Post, Project
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, ProjectForm
from django.views import generic
from django.urls import reverse, reverse_lazy

def index(request):
    return render(request, 'index.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/project_list.html', {'projects': projects})

def project_detail(request):
    project = Project.objects.get(slug=slug)
    response = render(request, '/project_detail.html', {
        "project": project
    })
    return response

@login_required
def project(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        projectForm = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())


        if projectForm.is_valid() and formset.is_valid():
            projectForm = projectForm.save(commit=False)
            projectForm.user = request.user
            projectForm.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(projectForm.errors, formset.errors)
    else:
        projectForm = ProjectForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'index.html',
                  {'projectForm': projectForm, 'formset': formset})
