from django.contrib import admin
from reports.models import Region, QuarterTargetLeads, CSATReport, CSATFilterDetails, KickOffProgram, MeetingMinutes, KickoffTagteam
from reports.forms import RegionForm


class RegionAdmin(admin.ModelAdmin):
    form = RegionForm
    list_display = ('name', 'location_list')
    filter_horizontal = ('location',)

admin.site.register(Region, RegionAdmin)


class QuarterTargetLeadsAdmin(admin.ModelAdmin):
    list_display = ('program', 'location', 'quarter', 'year', 'target_leads')

admin.site.register(QuarterTargetLeads, QuarterTargetLeadsAdmin)


class CSATReportAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'language', 'channel', 'category',)
    list_filter = ('category', 'language', 'channel', 'process')

admin.site.register(CSATReport, CSATReportAdmin)


class CSATFilterDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'lead_owners', 'channel', 'language_category', 'tagteam_location', 'process', 'survey_pin_number')
    list_filter = ('channel', 'language_category', 'tagteam_location', 'process')
    filter_horizontal = ('agent_language',)

admin.site.register(CSATFilterDetails, CSATFilterDetailsAdmin)


class MeetingMinutesAdmin(admin.ModelAdmin):
	list_display = ('meeting_audience', 'program', 'program_type', 'google_team', 'subject_timeline', 'other_subject', 'meeting_time_in_ist')

admin.site.register(MeetingMinutes, MeetingMinutesAdmin)

class KickOffProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name',)
admin.site.register(KickOffProgram, KickOffProgramAdmin)

class TagteamKickOffProgramAdmin(admin.ModelAdmin):
    list_display = ('kickoff_program',)
admin.site.register(KickoffTagteam, TagteamKickOffProgramAdmin)