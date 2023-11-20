import uuid
from django.db import models


class TeacherManager(models.Manager):
    pass


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    objects = TeacherManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
