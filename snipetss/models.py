from __future__ import unicode_literals

from django.db import models

class MyPhoto(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/%d/', null=True, max_length=255)

class Flag(models.Model):
    score = models.CharField(max_length=255)
    
# Create your models here.
class Snippet(models.Model):
    timecreated = models.DateTimeField(auto_now_add=True)
    drivername = models.CharField(max_length=100, blank=True, default='')
    score = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
   
   
    class Meta:
        ordering = ('timecreated',)


    def __unicode__(self):
     	return self.drivername


