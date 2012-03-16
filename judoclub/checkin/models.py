from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

CARD_CHOICES = ( 
    ('A', 'Anual'),
    ('B', 'SixMonth'),
    ('C', 'OneMonth'),
    ('D', 'Count'),
)

GROUP_CHOICES = (
    ('1', 'Kid'),
    ('2', 'Teenager'),
    ('3', 'Adult'),
)

class CustomerUserManager(models.Manager):
    def get_coaches(self):
        coach_profiles = UserProfile.objects.filter(is_coach=True)
        return coach_profiles

    def get_students(self):
        student_profiles = UserProfile.objects.filter(is_coach=False)
        return student_profiles

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(default=0, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    height = models.IntegerField(default=0, blank=True)
    weight = models.IntegerField(default=0, blank=True)
    mother = models.CharField(max_length=50, blank=True, null=True)
    father = models.CharField(max_length=50, blank=True, null=True)
    is_coach = models.BooleanField(default=False)
    objects = CustomerUserManager()

class Course(models.Model):
    group = models.CharField(max_length=1, choices=GROUP_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    card_type = models.CharField(max_length=1, choices=CARD_CHOICES)
    price = models.IntegerField()
    coach = models.ForeignKey(User)
        
class StudentCourse(models.Model):
    student = models.ForeignKey(User)
    join_date = models.DateField()
    introducer = models.CharField(max_length=50, blank=True, null=True)
    leave_date = models.DateField()
    leave_reason = models.CharField(max_length=500, blank=True, null=True)
    course = models.ForeignKey(Course)

class UserCheckin(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField()
    checkin = models.BooleanField(default=False)

class UserHonor(models.Model):
    user = models.ForeignKey(User)
    honor = models.CharField(max_length=100)
    time = models.DateField()





