from django.db import models

# Create your models here.

class AddTaskModel(models.Model):
    Title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default = " incompleted")
    