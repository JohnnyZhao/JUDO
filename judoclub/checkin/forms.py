from django.contrib.auth.models import User
from checkin.models import UserProfile
from django import forms
from django.forms import ModelForm

class JudoUserForm(ModelForm):
    class Meta:
       model = User  


class JudoUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
