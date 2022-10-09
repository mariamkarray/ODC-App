from email.policy import default
from django.db import models
import datetime
class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    prerequisite_courses = models.ManyToManyField("self", blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    supplier_id = models.ForeignKey('Supplier', on_delete = models.CASCADE, default=None)
    skills_id = models.ManyToManyField('Skill', default=None)
    completed = models.BooleanField(default = False)
    LOCATION_CHOICES = (
        ('GK', 'Greek Campus'),
        ('OTHER', 'Other'),
    )
    location = models.CharField(max_length=6,choices=LOCATION_CHOICES)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, default=None, blank=True)
    to_pay = models.IntegerField(default=None)
    already_paid = models.IntegerField(default=None)
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

