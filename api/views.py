from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from blog.models import Post, Project, Art
from django.utils import timezone

# This will return a list of books
@api_view(["GET"])
def art_list(request):
    artifacts = Art.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/art_list.html', {'artifacts': artifacts})