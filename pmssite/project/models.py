from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Project model
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start_date = models.DateField(default=datetime.now, blank=True)
    end_date = models.DateField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Task model
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
