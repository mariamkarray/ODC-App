from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.base_user import BaseUserManager
from phone_field import PhoneField
# whenever we save a new user, a signal is sent to perform another task (create profile)
from django.db.models.signals import post_save
# recieving signals 
from django.dispatch import receiver

from courses.models import Course, Skill

# students
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    joined_courses = models.ManyToManyField(Course, blank=True)
    email = models.EmailField()
    phone_number =  PhoneField(blank=True, null = True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    skills = models.ManyToManyField(Skill, blank=True, null = True)
    def __str__(self):
        return f"{str(self.first_name)} {str(self.last_name)}"

class StudentProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    PROGRESS_CHOICES = (
        ('ATTENDED', 'Attended'),
        ('FAILED INTERVIEW', 'Failed Interview.'),
        ('PASSED INTERVIEW', 'Passed Interview.'),
        ('NOT INVITED', 'Not Invited.'),
        ('REJECTED', 'Rejected'),
        ('CRITERIA NOT MET', 'Criteria not met.')
    )
    progress = models.CharField(max_length=50, choices=PROGRESS_CHOICES)
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}'s progress in the {self.course.name} course"

'''
class User(AbstractUser):
    # choice field 
    class Role(models.TextChoices):
        # choice = "what is stored in the database", 'human readable in the dropdown'
        ADMIN = "ADMIN", 'Admin'
        STUDENT = "STUDENT", 'Student'
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.ADMIN)



# filtering students
class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)

class Student(User):
    base_role = User.Role.STUDENT
    student = StudentManager()

    class Meta:
        proxy = True

@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)
        
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True, null = True)
    phone_num =  PhoneField(blank=True, null = True)
    joined_courses = models.ManyToManyField(Course, blank=True, null = True)
    skills = models.ManyToManyField(Skill, blank=True, null = True)

    def __str__(self):
        return "student: " + str(self.user.username)
        '''