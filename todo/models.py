import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model): 
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    created_at = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(
        User ,
        on_delete=models.CASCADE,
    )