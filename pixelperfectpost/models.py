from django.db import models
from django.urls import reverse



class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d', null=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
       return reverse('pixelperfectpost:details',args=[self.id,self.slug])


    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    media =  models.FileField(upload_to='sevices/%Y/%m/%d', null=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
       return reverse('pixelperfectpost:details',args=[self.id,self.slug])


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    video = models.FileField(upload_to='works/%Y/%m/%d', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
       return reverse('pixelperfectpost:details',args=[self.id,self.slug])


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Customer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, null=True)
    extension = models.CharField(max_length=10, default=None)
    number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)








