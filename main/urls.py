from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home),
    url(r'^home/$', views.main_home),
    url(r'^edit-profile-info/$', views.edit_profile_info),
    url(r'^team/$', views.team),
    url(r'^feedback/create/$', views.create_feedback),
    url(r'^feedback/create/(?P<lead_id>\d+)/$', views.create_feedback),
    url(r'^feedback/list/$', views.list_feedback),
    url(r'^feedback/view/Goog-(?P<id>\d+)/$', views.view_feedback),
    url(r'^create-feedback-from-lead-status$', views.create_feedback_from_lead_status),
    url(r'^feedback/(?P<id>\d+)/comment/$', views.comment_feedback),
    # url(r'^feedback/(?P<id>\d+)/resolve/$', views.resolve_feedback),
    url(r'^feedback/(?P<id>\d+)/reopen/$', views.reopen_feedback),
    url(r'^resources/$', views.resources),
    # url(r'^new_resources/$', views.new_resources),
    url(r'^get-inbound-locations$', views.get_inbound_locations),
    url(r'^get-notifications$', views.get_notifications),
    url(r'^get-started/$', views.get_started),
    url(r'^portal/feedback$', views.create_portal_feedback),
    url(r'^sales-tasks/$', views.sales_tasks),
    # url(r'^contacts/$', views.get_contacts),
    url(r'^top-30-cms/$', views.top_30_cms),
    # url(r'^user/master-data$', views.master_data_upload),
    url(r'^user/migrate-user-data$', views.migrate_user_data),
    url(r'^user/failed-records$', views.download_failed_records),
    url(r'^feedback/list/wpp$', views.list_feedback_wpp),
    url(r'^feedback/list/picasso$', views.list_feedback_picasso),
    url(r'^reps/details-download$', views.rep_details_download),
    url(r'^reps/details-upload$', views.rep_details_upload),
    url(r'^upload/file-handling$', views.upload_file_handling),
    url(r'^upload/migrate-data$', views.migrate_table_data),
    url(r'^picasso/$', views.picasso_home),
    url(r'^export-feedback/$', views.export_feedback),
    url(r'^report-a-bug/$', views.report_a_bug),
    url(r'^resources/rlsa-limitations/$', views.rlsa_limitations),

    # getting all regalix ids
    url(r'^user/email/$', views.get_regalix_emails),
    url(r'^assign-feedback/$', views.assign_feedback),

    # Notification Manager
    url(r'^notifications/$', views.notification_manager),

)
