from datetime import datetime
from django.db import models


# Create your models here.
class Leads(models.Model):
    # ref_google_rep_user = models.ForeignKey(User)
    google_rep_name = models.CharField(max_length=255)
    google_rep_email = models.CharField(max_length=255)

    ecommerce = models.IntegerField(default=0)
    lead_owner_name = models.CharField(max_length=255, null=False)
    lead_owner_email = models.CharField(max_length=255, null=False)
    company = models.CharField(max_length=255)
    lead_status = models.CharField(max_length=50)
    country = models.CharField(max_length=255)

    customer_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    first_name_optional = models.CharField(max_length=50)
    last_name_optional = models.CharField(max_length=100)
    phone_optional = models.CharField(max_length=100)
    email_optional = models.CharField(max_length=100)

    date_of_installation = models.DateTimeField(blank=True, null=True)

    time_zone = models.CharField(max_length=75)

    regalix_comment = models.TextField()
    google_comment = models.TextField()

    code_1 = models.TextField()
    url_1 = models.CharField(max_length=255)
    type_1 = models.CharField(max_length=150)
    comment_1 = models.TextField()

    code_2 = models.TextField()
    url_2 = models.CharField(max_length=255)
    type_2 = models.CharField(max_length=150)
    comment_2 = models.TextField()

    code_3 = models.TextField()
    url_3 = models.CharField(max_length=255)
    type_3 = models.CharField(max_length=150)
    comment_3 = models.TextField()

    code_4 = models.TextField()
    url_4 = models.CharField(max_length=255)
    type_4 = models.CharField(max_length=150)
    comment_4 = models.TextField()

    code_5 = models.TextField()
    url_5 = models.CharField(max_length=255)
    type_5 = models.CharField(max_length=150)
    comment_5 = models.TextField()

    no_of_calls_inbound = models.CharField(max_length=150)
    no_of_calls_outbound = models.CharField(max_length=150)
    emails_sent = models.CharField(max_length=150)
    emails_received = models.CharField(max_length=150)
    call_recordings = models.CharField(max_length=150)
    email_logs = models.CharField(max_length=150)
    team = models.CharField(max_length=100)
    is_active = models.IntegerField(default=1)

    appointment_date = models.DateTimeField(blank=True, null=True)
    first_contacted_on = models.DateTimeField(blank=True, null=True)

    #Rescheduled Appointments
    rescheduled_appointment = models.DateTimeField(blank=True, null=True)

    dials = models.IntegerField(default=0)
    lead_sub_status = models.CharField(max_length=100, null=True)

    created_date = models.DateTimeField(default=datetime.utcnow())
    updated_date = models.DateTimeField(default=datetime.utcnow(), auto_now=True)

    sf_lead_id = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Leads"


class Timezone(models.Model):
    zone_name = models.CharField(max_length=20)
    time_value = models.CharField(max_length=6)

    def __str__(self):              # __unicode__ on Python 2
        return self.zone_name

    class Meta:
        db_table = 'timezone'
        ordering = ['zone_name']


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    time_zone = models.ManyToManyField(Timezone)

    def __str__(self):              # __unicode__ on Python 2
        return self.location_name

    class Meta:
        db_table = 'locations'
        ordering = ['location_name']


class RegalixTeams(models.Model):
    team_name = models.CharField(max_length=100)
    location = models.ManyToManyField(Location)
    process_type = models.CharField(max_length=50, choices=(
        ('TAG', 'TAG'),
        ('MIGRATION', 'MIGRATION'),
        ('SHOPPING', 'SHOPPING'),
    ), default='TAG')

    def __str__(self):              # __unicode__ on Python 2
        return self.team_name

    class Meta:
        db_table = 'regalix_teams'
        ordering = ['team_name']
        verbose_name_plural = "Regalix Teams"


class Team(models.Model):
    """ Team/Program information """
    team_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.team_name

    class Meta:
        db_table = 'teams'
        ordering = ['team_name']
