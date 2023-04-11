from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey 

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title
    

class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                related_name = 'courses',
                                on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self) -> str:
        return self.title
    

class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name= 'modules',
                               on_delete=  models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title


'''adding creating polymorphic models/content
content model is a module containing multiple content'''

class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name= 'contents',
                               on_delete= models.CASCADE)
    content_type = models.ForeignKey(ContentType, 
                                     on_delete= models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
