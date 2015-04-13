from django.conf.urls import url, patterns
import views

urlpatterns = patterns(
    '',
    url(r'^lead-form/$', views.lead_form),
    url(r'^bundle-lead-form/$', views.bundle_lead_form),
    url(r'^leads-list/$', views.leads_list),
    url(r'^leads-report/$', views.leads_report),
    url(r'^thankyou/$', views.thankyou),
    url(r'^lead_error/$', views.lead_error),
    url(r'^day-light-changes/$', views.day_light_changes),
    url(r'^manage-leads/$', views.manage_leads),
    url(r'^upload-leads/$', views.upload_leads),
    url(r'^migrate-leads/$', views.migrate_leads),
    url(r'^get-lead/(?P<cid>[\w -]+)$', views.get_lead),
    url(r'^lead-summary/$', views.get_lead_summary),
    url(r'^lead-summary/(?P<lid>[0-9]+)$', views.get_lead_summary),
    url(r'^create-chat/$', views.create_chat_message),
    url(r'^create-teams/$', views.create_teams),
    url(r'^create-locations/$', views.create_locations),
    url(r'^create-codetypes/$', views.create_codetypes),
    url(r'^agency-form/$', views.agency_form),
    url(r'^download-agency-csv/$', views.download_agency_csv),
    url(r'^get-chat/$', views.get_chat_message_by_lead),
    url(r'^lead-summary-by-user/$', views.get_lead_status_by_ldap),
    url(r'^agency/(?P<agency_name>[\w -]+)/(?P<pid>[\w -][^/]+)$', views.agent_bulk_upload),
    url(r'^get-timezones/$', views.get_timezones),
    url(r'^agency-lead-form/$', views.agency_lead_form),
    url(r'^leads-summary-by-cid/$', views.get_lead_status_by_cid),
    url(r'^wpp-lead-form/$', views.wpp_lead_form),
    url(r'^wpp-lead-summary/$', views.get_wpp_lead_summary),
)
