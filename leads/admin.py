from django.contrib import admin
from leads.models import (Leads, Timezone, RegalixTeams, TreatmentType, WPPLeads,
                          Location, Team, CodeType, Language, LeadForm,
                          LeadFormAccessControl, TimezoneMapping, PicassoLeads, PicassoLeadGroupType, BlackListedCID,
                          BuildsBoltEligibility, WhiteListedAuditCID, LeadHistory #ArgosProcessTimeTracker
                          )
from leads.forms import LocationForm, LeadFormAccessControlAdminForm, TimezoneMappingForm, LeadHistoryForm
from lib.admin_helpers import CustomAdmin


class LeadsAdmin(admin.ModelAdmin):
    list_display = ('google_rep_name', 'lead_owner_name', 'lead_owner_email', 'first_name', 'last_name',
                    'company', 'lead_status', 'team', 'type_1', 'date_of_installation', 'appointment_date', 'language', 'tat')

    search_fields = ['customer_id', 'lead_owner_name']
    list_filter = ('language', )

    readonly_fields = ['google_rep_name', 'lead_owner_name', 'lead_owner_email', 'first_name', 'last_name',
                       'company', 'lead_status', 'team', 'type_1', 'date_of_installation', 'appointment_date', 'first_contacted_on', 'tat']

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(LeadsAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Leads, LeadsAdmin)


class WPPLeadsAdmin(admin.ModelAdmin):
    list_display = ('google_rep_name', 'lead_owner_name', 'first_name', 'last_name',
                    'company', 'lead_status', 'team', 'customer_id', 'ref_uuid','is_build_eligible' )

    search_fields = ['customer_id', 'lead_owner_name']

    list_filter = ('type_1', )

    readonly_fields = ['google_rep_name', 'lead_owner_name', 'lead_owner_email', 'first_name', 'last_name',
                       'company', 'team', 'type_1', 'is_build_eligible']

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(WPPLeadsAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(WPPLeads, WPPLeadsAdmin)


class TimezoneAdmin(admin.ModelAdmin):
    list_display = ('zone_name', 'time_value')

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(TimezoneAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Timezone, TimezoneAdmin)


class TimezoneMappingAdmin(admin.ModelAdmin):
    form = TimezoneMappingForm
    list_display = ('standard_timezone', 'daylight_timezone')

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(TimezoneMappingAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(TimezoneMapping, TimezoneMappingAdmin)


class RegalixTeamsAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'location_list', 'process_type', 'team_lead_list', 'team_manager_list', 'is_active')
    filter_horizontal = ('location', 'program', 'ldap', 'team_lead', 'team_manager')

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(RegalixTeamsAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(RegalixTeams, RegalixTeamsAdmin)


class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ('location_name', 'timezone_list', 'ds_timezone_list', 'daylight_start', 'daylight_end', 'primary_language',
                    'secondary_language_list', 'flag_image', 'phone', 'is_active')
    filter_horizontal = ('time_zone', 'ds_time_zone', 'language')

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(LocationAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Location, LocationAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'belongs_to', 'is_active',)
    list_filter = ('is_active', 'belongs_to')

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(TeamAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)
admin.site.register(Team, TeamAdmin)


class CodeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(CodeTypeAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(CodeType, CodeTypeAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language_name', 'is_active',)

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(LanguageAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Language, LanguageAdmin)


class LeadFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(LeadFormAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(LeadForm, LeadFormAdmin)


class LeadFormAccessControlAdmin(admin.ModelAdmin):
    form = LeadFormAccessControlAdminForm
    list_display = ('lead_form', 'program_list', 'location_list', 'rep_list',)
    filter_horizontal = ('programs', 'target_location', 'google_rep')

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(LeadFormAccessControlAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(LeadFormAccessControl, LeadFormAccessControlAdmin)


class TreatmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(TreatmentTypeAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(TreatmentType, TreatmentTypeAdmin)


class PicassoLeadsAdmin(admin.ModelAdmin):
    list_display = ('google_rep_name', 'lead_owner_name', 'customer_id', 'company', 'lead_status', 'code_1', 'type_1', 'team', 'picasso_objective', 'pod_name', 'is_build_eligible',)
    search_fields = ['customer_id', ]
    list_filter = ('lead_status', 'is_build_eligible')

    def get_readonly_fields(self, request, obj=None):
        return CustomAdmin.get_readonly_status(request, self.readonly_fields, obj)

    def has_add_permission(self, request):
        return CustomAdmin.get_permission_status(request)

    def has_delete_permission(self, request, obj=None):
        return CustomAdmin.get_permission_status(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = CustomAdmin.get_view_status(request, extra_context)
        return super(PicassoLeadsAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(PicassoLeads, PicassoLeadsAdmin)

admin.site.register(PicassoLeadGroupType)

class BlackListedCIDAdmin(admin.ModelAdmin):
    list_display = ('cid','active')

admin.site.register(BlackListedCID, BlackListedCIDAdmin)

class WPPBoltEligibilityAdmin(admin.ModelAdmin):
    list_display = ('cid','url', 'domain', 'bolt_eligible', 'last_assessed_date')

admin.site.register(BuildsBoltEligibility, WPPBoltEligibilityAdmin)

class WhiteListedAuditCIDAdmin(admin.ModelAdmin):
    list_display = ('external_customer_id','opportunity_type')

admin.site.register(WhiteListedAuditCID, WhiteListedAuditCIDAdmin)
# admin.site.register(ArgosProcessTimeTracker)


class LeadHistoryAdmin(admin.ModelAdmin):
    list_display = ('lead_id','modified_by','action_type','modifications','image_guid','original_image_name','image_link','previous_owner','current_owner')

admin.site.register(LeadHistory, LeadHistoryAdmin)