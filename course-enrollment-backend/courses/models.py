from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
    )
    course_location = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    course_content = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    teacher_id = models.IntegerField(
        null=False,
        blank=False,
    )

    user = models.ManyToManyField(to=User, related_name='courses')
