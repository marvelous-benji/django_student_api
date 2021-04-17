from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=30,unique=True,blank=False)
    subject_class = models.CharField(max_length=15,blank=False)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Subject('{self.teacher.username}','{self.subject_name}')"
