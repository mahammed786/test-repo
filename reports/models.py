import os
from django.db import models
from uuid import uuid4
from leads.models import Location, Team, Language
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from jsonfield2 import JSONField


class LeadSummaryReports(models.Model):
    """ Users additional information """
    code_type = models.CharField(max_length=100)
    total_leads = models.IntegerField(max_length=10, default=0)
    win = models.FloatField(max_length=10, default=0)
    implemented = models.IntegerField(max_length=10, default=0)
    in_queue = models.IntegerField(max_length=10, default=0)
    in_progress = models.IntegerField(max_length=10, default=0)
    tat_implemented = models.IntegerField(max_length=10, default=0)
    tat_first_contacted = models.IntegerField(max_length=10, default=0)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)


class Region(models.Model):
    """ Region with Location mapping information """

    name = models.CharField(max_length=100, unique=True)
    location = models.ManyToManyField(Location)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def location_list(self):
        return ", ".join(["%s" % (l.location_name) for l in self.location.all()])

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        db_table = 'regions'
        ordering = ['name']
        verbose_name_plural = "Region"


class QuarterTargetLeads(models.Model):
    """ Program by Location mapping in a Quarter
        Set Target Leads for each Program by Location
    """

    YEAR_CHOICES = []
    for r in range(2000, (datetime.utcnow().year + 2)):
        YEAR_CHOICES.append((r, r))

    program = models.ForeignKey(Team, null=False, blank=False)
    location = models.ForeignKey(Location, null=False, blank=False)
    quarter = models.CharField(max_length=10, blank=False, choices=(
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),)
    )
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.utcnow().year)
    target_leads = models.IntegerField(default=0)

    class Meta:
        unique_together = ('program', 'location', 'quarter', 'year')
        db_table = 'quarter_target_leads'
        ordering = ['target_leads']
        verbose_name_plural = "Quarter Target Leads"


class CallLogAccountManager(models.Model):
    """ Call Log Response from spreadsheet"""

    username = models.CharField(max_length=100, null=False, blank=False)
    seller_name = models.CharField(max_length=100, null=True, blank=True)
    seller_id = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    alternate_number = models.CharField(max_length=100, null=True, blank=True)
    meeting_time = models.DateTimeField(blank=True, null=True)
    call_status = models.CharField(max_length=100, null=True, blank=True)
    log_time_stamp = models.DateTimeField(blank=True, null=True)
    sheet_row_count = models.IntegerField(max_length=10, default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        db_table = 'call_log_account_manager'
        verbose_name_plural = "Call Log Account Manager"


class CSATReport(models.Model):
    """ CSAT Report data """

    language = models.CharField(max_length=100, blank=True)
    customer_id = models.CharField(max_length=100, null=False)
    cli = models.CharField(max_length=100, null=True, default='')

    q1 = models.IntegerField(max_length=10, default=0)
    q2 = models.IntegerField(max_length=10, default=0)
    q3 = models.IntegerField(max_length=10, default=0)
    q4 = models.IntegerField(max_length=10, default=0)
    q5 = models.IntegerField(max_length=10, default=0)
    sf_lead_id = models.CharField(max_length=50, default=None)
    survey_date = models.DateTimeField(blank=True)

    channel = models.CharField(max_length=10, blank=False, choices=(
        ('PHONE', 'PHONE'),
        ('EMAIL', 'EMAIL')), default='PHONE')
    process = models.CharField(max_length=10, blank=False, choices=(
        ('TAG', 'TAG'),
        ('SHOPPING', 'SHOPPING')), default='TAG')
    category = models.CharField(max_length=10, blank=False, choices=(
        ('MAPPED', 'MAPPED'),
        ('UNMAPPPED', 'UNMAPPPED')), default='UNMAPPPED')

    region = models.CharField(max_length=100, default='')
    lead_owner = models.CharField(max_length=100, default='')
    code_type = models.CharField(max_length=100, default='')
    program = models.CharField(max_length=100, default='')
    mapped_lead_created_date = models.DateTimeField(blank=True, null=True)
    lead_owner_name = models.CharField(max_length=255, null=True)
    lead_owner_email = models.CharField(max_length=255, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        verbose_name_plural = "CSAT Report"


class CSATFilterDetails(models.Model):
    """CSAT Filter details based on rep Details"""

    user = models.OneToOneField(User, related_name='csat_user')
    lead_owners = models.CharField(max_length=255, null=True)
    channel = models.CharField(max_length=10, blank=False, choices=(
        ('PHONE', 'PHONE'),
        ('EMAIL', 'EMAIL'),
        ('BOTH', 'BOTH')), default='PHONE')
    language_category = models.CharField(max_length=11, blank=False, choices=(
        ('English', 'English'),
        ('Non English', 'Non English'),
        ('BOTH', 'BOTH')), default='English')
    tagteam_location = models.CharField(max_length=10, blank=False, choices=(
        ('Bangalore', 'Bangalore'),
        ('Palo Alto', 'Palo Alto')), default='Bangalore')
    process = models.CharField(max_length=10, blank=False, choices=(
        ('TAG', 'TAG'),
        ('SHOPPING', 'SHOPPING'),
        ('BOTH', 'BOTH')), default='TAG')
    agent_language = models.ManyToManyField(Language)
    survey_pin_number = models.CharField(max_length=100, default='')


class MeetingMinutes(models.Model):
    """ Minutes of Meeting Data has to be stored """
    def get_file_path(instance, filename):
        """ Dynamic file path """
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid4(), ext)
        return os.path.join('meeting_minutes/', filename)

    subject_timeline = models.CharField(max_length=255, null=True)
    subject_type = models.CharField(max_length=255, null=True)
    other_subject = models.CharField(max_length=255, null=True)
    meeting_time_in_ist = models.DateTimeField(blank=True)
    google_poc = models.ForeignKey(User, related_name='google_poc', blank=True)
    regalix_poc = models.ForeignKey(User, related_name='regalix_poc', blank=True)
    google_team = models.ForeignKey(Team, null=False, blank=False)
    attendees = models.ManyToManyField(User, related_name="attendees")
    bcc = models.ManyToManyField(User, related_name="bcc")
    key_points = JSONField(default={})
    action_plan = JSONField(default={})
    next_meeting_datetime = models.DateTimeField(blank=True, null=True)
    tenantive_agenda = JSONField(default={})
    region = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    program = models.CharField(max_length=255, null=True)
    program_type = models.CharField(max_length=255, null=True)
    ref_uuid = models.CharField(max_length=100, blank=True, null=True)

    attachment_1 = models.FileField(upload_to=get_file_path, blank=True, null=True)
    attachment_2 = models.FileField(upload_to=get_file_path, blank=True, null=True)
    attachment_3 = models.FileField(upload_to=get_file_path, blank=True, null=True)
    attachment_4 = models.FileField(upload_to=get_file_path, blank=True, null=True)
    attachment_5 = models.FileField(upload_to=get_file_path, blank=True, null=True)

    attached_link_1 = models.CharField(max_length=255, null=True, blank=True)
    attached_link_2 = models.CharField(max_length=255, null=True, blank=True)
    attached_link_3 = models.CharField(max_length=255, null=True, blank=True)
    attached_link_4 = models.CharField(max_length=255, null=True, blank=True)
    attached_link_5 = models.CharField(max_length=255, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        verbose_name_plural = "Meeting Minutes"
