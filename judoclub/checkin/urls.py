from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('checkin.views',
    url(r'^create_user/$', 'create_user', name='create_user'),
    url(r'^update_user/(?P<user_id>[\d]+)/$', 'update_user', name='update_user'),
    url(r'^delete_user/(?P<user_id>[\d]+)/$', 'delete_user', name='delete_user'),

    url(r'^create_userprofile/(?P<user_id>[\d]+)/$', 'create_userprofile', name='create_userprofile'),
    url(r'^update_userprofile/(?P<profile_id>[\d]+)/$', 'update_userprofile', name='update_userprofile'),

  #  url(r'^create_user_award/(?P<user_id>[\d]+)/$', 'create_user_award', name='create_user_award'),
  #  url(r'^update_user_award/(?P<user_id>[\d]+)/$', 'update_user_award', name='update_user_award'),
  #  url(r'^delete_user_award/(?P<user_id>[\d]+)/$', 'delete_user_award', name='delete_user_award'),


    url(r'^create_course/$', 'create_course', name='create_course'),
    url(r'^update_course/(?P<course_id>[\d]+)/$', 'update_course', name='update_course'),
    url(r'^delete_course/(?P<course_id>[\d]+)/$', 'delete_course', name='delete_course'),

    url(r'^create_student_course/$', 'create_student_course', name='create_student_course'),
    url(r'^update_student_course/(?P<studentcourse_id>[\d]+)/$', 'update_student_course', name='update_student_course'),
    url(r'^delete_student_course/(?P<studentcourse_id>[\d]+)/$', 'delete_student_course', name='delete_student_course'),

    url(r'^checkin/(?P<user_id>[\d]+)/(?P<course_id>[\d]+)/$', 'checkin', name='checkin'),
    url(r'^checkin/history/$', 'checkin_history', name='checkin_history'),
)

