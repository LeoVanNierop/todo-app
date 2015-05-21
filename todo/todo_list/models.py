from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ForeignKey(User) 
    listname = models.CharField(max_length=200, default='To do')
    
    def __unicode__(self):
        return listname + " list for: " + self.user.username

class Task(models.Model):
    list = models.ForeignKey(List)
    task_description = models.CharField(max_length=200)
    deadline = models.DateTimeField(blank=True)
    finished = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['deadline']
    
    def __unicode__(self):
        return "task: " + self.task_description
    



