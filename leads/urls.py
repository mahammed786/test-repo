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
    url(r'^get-lead/(?P<cid>[\w -]+)/(?P<feedback_type>[A-Za-z]+)$', views.get_lead),
    url(r'^lead-summary/$', views.get_lead_summary),
    # url(r'^lead-summary/(?P<lid>[0-9]+)$', views.get_lead_summary),
    url(r'^lead-summary/(?P<lid>[0-9]+)/(?P<page>[0-9]+)$', views.get_lead_summary),
    url(r'^create-chat/$', views.create_chat_message),
    url(r'^create-teams/$', views.create_teams),
    url(r'^create-locations/$', views.create_locations),
    url(r'^create-codetypes/$', views.create_codetypes),
    url(r'^agency-intro-form/$', views.agency_introduction_form),
    url(r'^download-agency-csv/$', views.download_agency_csv),
    url(r'^get-chat/$', views.get_chat_message_by_lead),
    url(r'^lead-summary-by-user/$', views.get_lead_status_by_ldap),
    # url(r'^agency/(?P<agency_name>[\w -]+)/(?P<pid>[\w -][^/]+)$', views.agent_bulk_upload),
    url(r'^agency-form/$', views.agent_bulk_upload),
    url(r'^get-timezones/$', views.get_timezones),
    url(r'^agency-lead-form/$', views.agency_lead_form),
    url(r'^leads-summary-by-cid/$', views.get_lead_status_by_cid),
    url(r'^wpp-lead-form/$', views.wpp_lead_form),
    url(r'^wpp-lead-summary/$', views.get_wpp_lead_summary),
    url(r'^get-lead-by-lid/(?P<lid>[\w]+)/(?P<feedback_type>[A-Za-z]+)$', views.get_lead_by_lid),
    url(r'^pagination-leads-summary/$', views.get_pagination_lead_summary),
    url(r'^get-wpp-lead-summary-by-treatment/$', views.get_wpp_lead_summary_by_treatment),
    url(r'^lead-history/(?P<lid>[\w]+)$', views.lead_history),
    url(r'^priority-check/$', views.priority_check),
    url(r'^check-url-priority/$', views.check_url_priority),
    url(r'^report-team/$', views.report_team),
    url(r'^picasso-lead-form/$', views.picasso_lead_form),
    url(r'^picasso-lead-summary/$', views.get_picasso_lead_summary),
    # picasso build wpp form
    url(r'^picasso-build-form/$', views.picasso_build_wpp_form),
    url(r'^picasso-build-form/(?P<ref_id>[\w]+)$', views.picasso_build_wpp_form),
    url(r'^get-eligible-picasso-lead/(?P<cid>[\w -]+)$', views.get_eligible_picasso_leads),
    url(r'^get-eligible-picasso-lead-by-lid/(?P<lid>[\w]+)$', views.get_eligible_picasso_lead_by_lid), #searh_leads
    url(r'^searh-leads/$', views.searh_leads),
)
