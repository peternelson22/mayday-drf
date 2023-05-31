
from django.db import models

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER)
    dob = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
