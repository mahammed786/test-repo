from django.conf.urls import patterns, url
from representatives import views

urlpatterns = patterns(
    '',
    url(r'^users/$', views.users),
    url(r'^add-edit-user/$', views.add_edit_user),
    url(r'^add-edit-user/(?P<id>\d+)/$', views.add_edit_user),
    url(r'^schedule/$', views.plan_schedule),
    url(
        r'^schedule/(?P<plan_month>\d+)-(?P<plan_day>\d+)-(?P<plan_year>\d+)/(?P<process_type>\w+)/(?P<team_id>\d+)/$',
        views.plan_schedule
    ),
    url(r'^availability/$', views.availability_list),
    url(
        r'^availability/(?P<avail_month>\d+)-(?P<avail_day>\d+)-(?P<avail_year>\d+)/(?P<process_type>\w+)/(?P<location_id>\d+)/(?P<time_zone>\w+)/$',
        views.availability_list
    ),
    url(r'^check-and-add/$', views.check_and_add_appointment),
    url(r'^copy-appointment/(?P<plan_month>\d+)-(?P<plan_day>\d+)-(?P<plan_year>\d+)/(?P<team_id>\d+)/$', views.copy_appointment_to_next_week),
    url(r'^export-appointments/$', views.export_appointments),
    # export appointments with schedule appointments
    url(r'^export-total-appointments/$', views.export_appointments_with_schedule_appointments),
    # manager view
    url(r'^total-appointments/$', views.total_appointments),
    url(
        r'^total-appointments/(?P<plan_month>\d+)-(?P<plan_day>\d+)-(?P<plan_year>\d+)/$',
        views.total_appointments
    ),
    url(r'^appointments-calender/$', views.appointments_calendar),
    url(r'^rep-details/$', views.tat_details),
    url(r'^rep-details/(?P<plan_month>\d+)-(?P<plan_day>\d+)-(?P<plan_year>\d+)/$', views.tat_details),

    url(r'^bolt-rep-details/$', views.bolt_tat_details),
    url(r'^bolt-rep-details/(?P<plan_month>\d+)-(?P<plan_day>\d+)-(?P<plan_year>\d+)/$', views.bolt_tat_details),


)
