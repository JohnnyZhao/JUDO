# Create your views here.
from django.shortcuts import render_to_response as render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from checkin.models import UserProfile, UserCheckin, Course, UserHonor, StudentCourse
from checkin.forms import JudoUserForm, JudoUserProfileForm, CourseForm, StudentCourseForm, UserAwardForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from common import render_json
SUCCESS = 1
FAIL = 0

def create_user(request):
    if request.method == "GET":
        user_form = UserCreationForm()
        context = RequestContext(request, {'user_form': user_form})
    else:
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            context = RequestContext(request, {'user_form': user_form, 'person': user})
        else:
            context = RequestContext(request, {'user_form': user_form})
    return render('checkin/create_user.html', context)
#problem here
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "GET":
        user_form = PasswordChangeForm(user=user)
    if request.method == "POST":
        user_form = PasswordChangeForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        else:
            print user_form
    context = RequestContext(request, {"person":user, "user_form": user_form})
    return render('checkin/update_user.html', context)
            
def delete_user(request, user_id):
    result = {"status": FAIL}
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        result["status"] = SUCCESS
    except User.DoesNotExist as e:
        print e
    return render_json(result)


def create_userprofile(request, user_id):
    try:
        profile = UserProfile.objects.get(user__id=user_id)
        return redirect('update_userprofile', user_id=user_id)
    except Exception as e:
        print e
        user = get_object_or_404(User, id=user_id)
        if request.method == "GET":
            user_profile_form = JudoUserProfileForm(initial={"user": user})
        else:
            user_profile_form = JudoUserProfileForm(request.POST)
            if user_profile_form.is_valid():
                user_profile = user_profile_form.save()
        context = RequestContext(request, {'profile_form': user_profile_form, "person": user})
        return render('checkin/create_user_profile.html', context)

def update_userprofile(request, user_id):
    profile = get_object_or_404(UserProfile, user__id=user_id)
    if request.method == "GET":
        profile_form = JudoUserProfileForm(instance=profile)
    if request.method == "POST":
        profile_form = JudoUserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save()
    context = RequestContext(request, {"profile": profile, "profile_form": profile_form})
    return render('checkin/update_user_profile.html', context)

def create_student_course(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "GET":
        student_course_form = StudentCourseForm(initial={'student': user})
        context = RequestContext(request, {'student_course_form': student_course_form})
    else:
        student_course_form = StudentCourseForm(request.POST)
        if student_course_form.is_valid():
            student_course = student_course_form.save()
            context = RequestContext(request, {'student_course_form': student_course_form, 'student_course': student_course})
        else:
            context = RequestContext(request, {'student_course_form': student_course_form})
    return render('checkin/create_student_course.html', context)

def update_student_course(request, studentcourse_id):
    student_course = get_object_or_404(StudentCourse, id=studentcourse_id)
    student_course_form = StudentCourseForm(request.POST, instance=student_course) 
    if request.method == "GET":
        student_course_form = StudentCourseForm(instance=student_course)
    if request.method == "POST":
        student_course_form = StudentCourseForm(request.POST, instance=student_course)
        if student_course_form.is_valid():
            student_course = student_course_form.save()
    context = RequestContext(request, {"student_course": student_course, "student_course_form": student_course_form})
    return render('checkin/update_student_course.html', context)

def delete_student_course(request, studentcourse_id):
    result = {"status": FAIL}
    try:
        student_course = StudentCourse.objects.get(id=studentcourse_id)
        student_course.delete()
        result["status"] = SUCCESS
    except StudentCourse.DoesNotExist as e:
        print e
    return render_json(result)

def create_course(request):
    if request.method == "GET":
        course_form = CourseForm()
        context = RequestContext(request, {'course_form': course_form})
    else:
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course = course_form.save()
            context = RequestContext(request, {'course_form': course_form, 'course': course})
        else:
            context = RequestContext(request, {'course_form': course_form})
    return render('checkin/create_course.html', context)

def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "GET":
        course_form = CourseForm(instance=course)
    if request.method == "POST":
        course_form = CourseForm(request.POST, instance=course)
        if course_form.is_valid():
            course = course_form.save()
    context = RequestContext(request, {"course": course, "course_form": course_form})
    return render('checkin/update_course.html', context)

def delete_course(request, course_id):
    result = {"status": FAIL}
    try:
        course = Course.objects.get(id=course_id)
        course.delete()
        result["status"] = SUCCESS
    except Course.DoesNotExist as e:
        print e
    return render_json(result)

def create_user_award(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "GET":
        user_award_form = UserAwardForm(initial={"user": user})
    else:
        user_award_form = UserAwardForm(request.POST)
        if user_award_form.is_valid():
            user_award = user_award_form.save()
    context = RequestContext(request, {'user_award_form': user_award_form, 'person': user})
    return render('checkin/create_user_award.html', context)

def update_user_award(request, award_id):
    user_award = get_object_or_404(UserHonor, id=award_id)
    if request.method == "GET":
        user_award_form = UserAwardForm(instance=user_award)
    if request.method == "POST":
        user_award_form = UserAwardForm(request.POST, instance=user_award)
        if user_award_form.is_valid():
            user_award = user_award_form.save()
    context = RequestContext(request, {"user_award": user_award, "user_award_form": user_award_form})
    return render('checkin/update_user_award.html', context)

def delete_user_award(request, award_id):
    result = {"status": FAIL}
    try:
        user_award = UserHonor.objects.get(id=award_id)
        user_award.delete()
        result["status"] = SUCCESS
    except UserHonor.DoesNotExist as e:
        print e
    return render_json(result)

def checkin(request, user_id, course_id):
    result {"status": FAIL}
    checkin_time = request.GET.get("checkin_time")
    try:
        user = User.objects.get(id=user_id)
        course = User.objects.get(id=course_id)
    except User.DoesNotExist as e:
        pass
    except Course.DoesNotExist as e:
        pass
    try:
        checkin = Checkin(user=user, course=course, time=checkin_time)
        checkin.save()
        result["status"] = SUCCESS
    except:
        pass

# multiple choices for checkin_date and checkin_course        
def checkin_history(request):
    checkin_date = request.GET.get('checkin_date')
    checkin_course = request.GET.get('checkin_course')
    # datetime.date
    checkin = UserCheckin.objects.filter(time=checkin_date, course=checkin_course)
    context = RequestContext(request, {'checkin': checkin})
    return render('checkin/history.html', context)

