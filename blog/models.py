from enum import unique
from tabnanny import verbose
from wsgiref.validate import validator
from django.db import models
from django.forms import DateTimeField
from django.core.validators import MinLengthValidator
# Create your models here.
class Tags(models.Model):
    captions = models.CharField(max_length=20)
    def get_tags(self):
        return f"{self.captions}"
    def __str__(self):
        return self.get_tags()
    class Meta:
        verbose_name_plural = "tags"
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def full_name(self):
        return f"{self.first_name} {self.last_name} "
        
    def __str__(self):
        return self.full_name()
        
    
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    excerpt = models.CharField(max_length = 200)
    image_name = models.ImageField(upload_to = "posts/")
    date_d = models.DateTimeField(auto_now=True)
    content = models.TextField(validators = [MinLengthValidator(10)])
    slug = models.SlugField(unique=True , db_index=True)
    author = models.ForeignKey(Author, related_name='blogs', on_delete= models.SET_NULL , null=True)
    tags = models.ManyToManyField(Tags)
    
        