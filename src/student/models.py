import uuid
from django.db import models


class StudentManager(models.Manager):
    pass


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = StudentManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
