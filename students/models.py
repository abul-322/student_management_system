from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    course = models.CharField(max_length=100)

    age = models.IntegerField(default=0)

    address = models.TextField()

    created_at = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name
