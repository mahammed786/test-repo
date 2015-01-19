from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home),
    url(r'^home$', views.main_home),
    url(r'^add-manager-info/$', views.add_manager_info),
    url(r'^team/$', views.team),
    url(r'^feedback/create/$', views.create_feedback),
    url(r'^feedback/create/(?P<lead_id>\d+)/$', views.create_feedback),
    url(r'^feedback/list/$', views.list_feedback),
    url(r'^feedback/view/Goog-(?P<id>\d+)/$', views.view_feedback),
    url(r'^create-feedback-from-lead-status$', views.create_feedback_from_lead_status),
    url(r'^feedback/(?P<id>\d+)/comment/$', views.comment_feedback),
    url(r'^feedback/(?P<id>\d+)/resolve/$', views.resolve_feedback),
    url(r'^feedback/(?P<id>\d+)/reopen/$', views.reopen_feedback),
    # url(r'^report/$', views.report),
    # url(r'^contacts/$', views.get_contacts),
    # url(r'^top-30-cms/$', views.top_30_cms),
)
