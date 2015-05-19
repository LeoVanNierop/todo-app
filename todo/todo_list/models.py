from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    list = models.ForeignKey(List)
    task_description = models.Charfield(max_length=200)
    deadline = models.DateTimeField(blank=True)
    finished = models.BooleanField(default=false)
    
    def __unicode__(self):
        return "task: " + self.task_description
    

class List(models.Model):
    user = models.OneToOneField(User) 
    
    def __unicode__(self):
        return "ToDo list for: " + self.user.username


