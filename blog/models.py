from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Project(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    url = models.URLField(max_length=250)
    github = models.URLField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
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
        """Returns the url to access the home page."""
        return reverse('index')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
