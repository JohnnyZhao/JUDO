from django.contrib.auth.models import User
from checkin.models import UserProfile, Course, StudentCourse, UserHonor
from django import forms
from django.forms import ModelForm

class JudoUserForm(ModelForm):
    class Meta:
        model = User  


class JudoUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile

class CourseForm(ModelForm):
    class Meta:
        model = Course

class StudentCourseForm(ModelForm):
    class Meta:
        model = StudentCourse
 

class UserAwardForm(ModelForm):
    class Meta:
        model = UserHonor 
