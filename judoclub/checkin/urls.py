from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('checkin.views',
    url(r'^create_user/$', 'create_update_user', name='create_user'),
    url(r'^update_user/(?P<update_id>[\d]+)/$', 'create_update_user', name='update_user'),

    url(r'^create_userprofile/$', 'create_update_userprofile', name='create_userprofile'),
    url(r'^update_userprofile/(?P<update_id>[\d]+)/$', 'create_update_userprofile', name='update_userprofile'),

    url(r'^delete_user/(?P<user_id>[\d]+)/$', 'delete_user', name='delete_user'),

    url(r'^create_course/$', 'create_update_course', name='create_course'),
    url(r'^update_course/(?P<update_id>[\d]+)/$', 'create_update_course', name='update_course'),
    url(r'^delete_course/(?P<course_id>[\d]+)/$', 'delete_course', name='delete_course'),

    url(r'^create_student_course/$', 'create_student_course', name='create_student_course'),
    url(r'^update_student_course/(?P<studentcourse_id>[\d]+)/$', 'update_student_course', name='update_student_course'),
    url(r'^delete_student_course/(?P<studentcourse_id>[\d]+)/$', 'delete_student_course', name='delete_student_course'),

    url(r'^checkin/(?P<user_id>[\d]+)/(?P<course_id>[\d]+)/$', 'checkin', name='checkin'),
)

