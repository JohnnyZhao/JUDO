# Create your views here.
from django.shortcuts import render_to_response as render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from checkin.models import UserProfile
from checkin.forms import JudoUserForm, JudoUserProfileForm
from django.contrib.auth.forms import UserCreationForm

SUCCESS = 1
FAIL = 0

def create_update_user(request, update_id=None):
    # update_id is a user.id
    if update_id:
        user = get_object_or_404(User, id=update_id)
    else:
        user = None
    user_form = UserCreationForm(instance=user)
    if request.method == "POST":
        user_form = UserCreationForm(request.POST, instance=user)
        if user_form.is_valid():
            user = user_form.save()
            profile_form = JudoUserProfileForm(initial={"user":user})
            context = RequestContext(request, {"user":user, "profile_form": profile_form})
            return render('checkin/create_update_userprofile.html', context)
    context = RequestContext(request, {"user": user, "user_form": user_form})
    return render('checkin/create_update_user.html', context)
            
def delete_user(request, user_id):
    result["status"] = FAIL
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        result["status"] = SUCCESS
    except User.DoesNotExist as e:
        print e
    return render_json(result)

def create_update_userprofile(request, update_id=None):
    # update_id is a user.id
    profile = get_object_or_404(UserProfile, user__id=update_id)
    profile_form = JudoUserProfileForm(request.POST, instance=profile) 
 
def create_student_course(request):
    pass

def update_student_course(request, studentcourse_id):
    pass

def delete_student_course(request, studentcourse_id):
    pass

def create_update_course(request, update_id=None):
    pass

def delete_course(request, course_id):
    pass

def checkin(request, user_id, course_id):
    pass
