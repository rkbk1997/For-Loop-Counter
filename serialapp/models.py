from django.db import models

# Create your models here.
class StudentName(models.Model):
    name=models.CharField(max_length=300)