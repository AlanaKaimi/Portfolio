from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)
    
    def set_slug(self):
        # If the slug is already set, stop here
        if self.slug:
            return
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0
        # while we can find a record already in the DB with the slug we're trying to use
        while Post.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)        
        self.slug = slug

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

class Project(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=250, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)
    
    def set_slug(self):
        # If the slug is already set, stop here
        if self.slug:
            return
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0
        # while we can find a record already in the DB with the slug we're trying to use
        while Project.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)        
        self.slug = slug

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  


class Images(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

class Art(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)
    
    def set_slug(self):
        # If the slug is already set, stop here
        if self.slug:
            return
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0
        # while we can find a record already in the DB with the slug we're trying to use
        while Art.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)        
        self.slug = slug

    def get_absolute_url(self):
        return reverse('art_detail', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
