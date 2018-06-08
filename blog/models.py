from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    #objects = models.Manager() #the default manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'), ('published','Published'),
    )
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)#Automatically set the field to now when the object is first created
    updated = models.DateTimeField(auto_now=True)#to be set up to now only automatically updated when calling Model.save().
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    author = models.ForeignKey(User, related_name='blog_blogs')
    published = PublishedManager()#our custom manager

    def __str__(self):
        return self.title

    #返回 URLc
    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs = {'author_name':self.author.username,'blog_title':self.title})

    class Meta:
        unique_together = (("author", "title"),)
        ordering = ['-publish']




