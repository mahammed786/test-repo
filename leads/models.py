import os
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


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
    appointment_date_in_ist = models.DateTimeField(blank=True, null=True)

    # Rescheduled Appointments
    rescheduled_appointment = models.DateTimeField(blank=True, null=True)
    rescheduled_appointment_in_ist = models.DateTimeField(blank=True, null=True)
    eto_ldap = models.CharField(max_length=100, blank=True, null=True, default='')

    dials = models.IntegerField(default=0)
    lead_sub_status = models.CharField(max_length=100, null=True)

    tat = models.IntegerField(default=0)

    created_date = models.DateTimeField(default=datetime.utcnow())
    updated_date = models.DateTimeField(default=datetime.utcnow(), auto_now=True)

    sf_lead_id = models.CharField(max_length=50, unique=True)
    wpp_treatment_type = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    gcss = models.CharField(max_length=50, blank=True, null=True)

    # New fields for Argos Project
    feed_optimisation_status = models.CharField(max_length=300, blank=True, null=True)
    feed_optimisation_sub_status = models.CharField(max_length=300, blank=True, null=True)
    number_of_products = models.CharField(max_length=100, blank=True, null=True)
    additional_description = models.CharField(max_length=3000, blank=True, null=True)
    area_tobe_improved = models.CharField(max_length=3000, blank=True, null=True)
    shopping_feed_link = models.CharField(max_length=1000, blank=True, null=True)
    business_type = models.CharField(max_length=100, blank=True, null=True)
    authcase_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Leads"


# Create your models here.
class WPPLeads(models.Model):
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

    # Rescheduled Appointments
    rescheduled_appointment = models.DateTimeField(blank=True, null=True)
    rescheduled_appointment_in_ist = models.DateTimeField(blank=True, null=True)

    dials = models.IntegerField(default=0)
    lead_sub_status = models.CharField(max_length=100, null=True)

    tat = models.IntegerField(default=0)

    created_date = models.DateTimeField(default=datetime.utcnow())
    updated_date = models.DateTimeField(default=datetime.utcnow(), auto_now=True)

    sf_lead_id = models.CharField(max_length=50, unique=True)
    treatment_type = models.CharField(max_length=100, blank=True, null=True)
    additional_notes = models.TextField(default='')
    mockup_url = models.CharField(max_length=255, null=True)
    mockup_password = models.CharField(max_length=255, null=True)
    stage_url = models.CharField(max_length=255, null=True)
    stage_password = models.CharField(max_length=255, null=True)
    is_ab_test = models.CharField(max_length=255, null=True, default='YES')
    is_nominated = models.BooleanField(default=False)
    ref_uuid = models.CharField(max_length=100, blank=True, null=True)

    is_build_eligible = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = "WPP Leads"


class Timezone(models.Model):
    zone_name = models.CharField(max_length=20, unique=True)
    time_value = models.CharField(max_length=6)

    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    # Validate fields
    def clean(self):
        # Time zone value format should be Ex: +0:00 or -0:00.
        if self.time_value == '':
            raise ValidationError('Please enter Timezone value.')

        if "+" not in self.time_value:
            if "-" not in self.time_value:
                raise ValidationError('Timezone value format shoud be starts with + or - symbol.')

        if ":" not in self.time_value:
            raise ValidationError('Timezone value format shoud be +hh:mm or -hh:mm')

        if len(self.time_value.split(":")) > 2:
            raise ValidationError('value should be hh:mm formate.')

        if len(self.time_value.split(":")) == 2:
            hh = self.time_value.split(":")[0]
            mm = self.time_value.split(":")[1]
            if hh[0] not in ['+', '-']:
                raise ValidationError('In timezone value + or - symbol should be first character')

            if len(hh[1:]) == 0:
                raise ValidationError('Please enter hours')

            if len(mm) == 0:
                raise ValidationError('Please enter minutes')

            try:
                hh = int(hh[1:])
                if hh > 13:
                    raise ValidationError('Hours should be less than 14')
            except Exception:
                raise ValidationError('Hours should be in numeric and less than 14')

            try:
                mm = int(mm)
                if mm > 59:
                    raise ValidationError('Minutes should be less than 60')
            except Exception:
                raise ValidationError('Minutes should be in numeric and less than 60')

    def __str__(self):              # __unicode__ on Python 2
        return self.zone_name

    class Meta:
        db_table = 'timezone'
        ordering = ['zone_name']


class TimezoneMapping(models.Model):
    standard_timezone = models.ForeignKey(Timezone, related_name="std_timezone", unique=True)
    daylight_timezone = models.ForeignKey(Timezone, related_name="ds_timezone", unique=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        db_table = 'timezone_mapping'
        ordering = ['standard_timezone']
        unique_together = ('standard_timezone', 'daylight_timezone')
        verbose_name_plural = "Timezone Mapping"


class Language(models.Model):
    """ Language model """

    language_name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.language_name

    class Meta:
        db_table = 'languages'
        verbose_name_plural = 'Languages'


class Location(models.Model):

    def get_flag_image(instance, flag_filename):
        """ Dynamic location flag image path """

        ext = flag_filename.split('.')[-1]

        if instance.location_name:
            filename = "%s.%s" % (instance.location_name.replace(' ', '-'), ext)
        else:
            filename = flag_filename
        return os.path.join('country_flag/', filename)

    location_name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=50, null=True, default=None, blank=True)
    time_zone = models.ManyToManyField(Timezone, related_name="standard_timezone", limit_choices_to={'is_active': True})
    ds_time_zone = models.ManyToManyField(Timezone, related_name="daylight_timezone", blank=True, null=True, limit_choices_to={'is_active': True})
    daylight_start = models.DateTimeField(blank=True, null=True, default=None)
    daylight_end = models.DateTimeField(blank=True, null=True, default=None)
    primary_language = models.ForeignKey(Language, related_name="primary_language", null=False, blank=False, default=1)
    language = models.ManyToManyField(Language)
    flag_image = models.ImageField(upload_to=get_flag_image, null=True, max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def timezone_list(self):
        return ", ".join(["%s (UTC %s)" % (t.zone_name, t.time_value) for t in self.time_zone.all()])

    def ds_timezone_list(self):
        return ", ".join(["%s (UTC %s)" % (t.zone_name, t.time_value) for t in self.ds_time_zone.all()])

    def secondary_language_list(self):
        return ", ".join(["%s" % (l.language_name) for l in self.language.all()])

    @property
    def flag_filename(self):
        return os.path.basename(self.flag_image.name)

    def clean(self):
        # Either email or google_id. Both cannot be empty.
        if self.location_name == '':
            raise ValidationError('Please enter location name.')

        if self.daylight_start or self.daylight_end:
            if not self.daylight_start:
                raise ValidationError('Please enter daylight start date.')
            if not self.daylight_end:
                raise ValidationError('Please enter daylight end date.')
            elif self.daylight_start >= self.daylight_end:
                raise ValidationError('Daylight start date should be less than daylight end date.')

        image = self.flag_image
        if image:
            try:
                img = Image.open(image)

                w, h = img.size

                # validate dimensions
                max_width = 200
                max_height = 200
                if w > max_width or h > max_height:
                    raise ValidationError(
                        _('Please use an image that is smaller or equal to '
                          '%s x %s pixels.' % (max_width, max_height)))

                # validate content type
                img_ext = image.name.split('.')[1]
                if img_ext not in ['png']:
                    raise ValidationError(_('Image is not in PNG format. Please use a PNG image.'))

                return image
            except Exception:
                if self.flag_filename:
                    if not os.path.isfile(os.path.join('country_flag/', self.flag_filename)):
                        self.flag_image.delete()
                        return image

    def __str__(self):              # __unicode__ on Python 2
        return self.location_name

    class Meta:
        db_table = 'locations'
        ordering = ['location_name']
        verbose_name_plural = 'Target Location'


class PicassoLeadGroupType(models.Model):
   group_type = models.CharField(max_length=100, blank=True, null=True)
   is_active = models.BooleanField(default=True)

   def __str__(self):
       return self.group_type


class Team(models.Model):
    """ Team/Program information """
    picasso_lead_group_type = models.ForeignKey(PicassoLeadGroupType,blank=True,null=True,default=None)
    team_name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    belongs_to = models.CharField(max_length=50, blank=False, choices=(
        ('TAG', 'TAG'),
        ('WPP', 'WPP'),
        ('PICASSO', 'PICASSO'),
        ('TAG-WPP', 'TAG-WPP'),
        ('TAG-PICASSO', 'TAG-PICASSO'),
        ('WPP-PICASSO', 'WPP-PICASSO'),
        ('ALL', 'ALL')), default='TAG'
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.team_name

    class Meta:
        db_table = 'teams'
        ordering = ['team_name']
        verbose_name_plural = "Programs"


class CodeType(models.Model):
    """ Code Types list """

    name = models.CharField(max_length=100, unique=True)
    avg_setup_time = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'code_types'
        ordering = ['name']
        verbose_name_plural = "Code Types"


class RegalixTeams(models.Model):

    def default_team_lead(self):
        try:
            lead_owner = User.objects.get(email=settings.DEFAULT_LEAD_OWNER_EMAIL)
        except ObjectDoesNotExist:
            lead_owner = User.objects.create(
                email=settings.DEFAULT_LEAD_OWNER_EMAIL,
                username=settings.DEFAULT_LEAD_OWNER_EMAIL,
                first_name=settings.DEFAULT_LEAD_OWNER_FNAME,
                last_name=settings.DEFAULT_LEAD_OWNER_LNAME
            )
        return lead_owner

    team_name = models.CharField(max_length=100, unique=True)
    location = models.ManyToManyField(Location, limit_choices_to={'is_active': True})
    program = models.ManyToManyField(Team, blank=True, null=True, limit_choices_to={'is_active': True})
    ldap = models.ManyToManyField(User, blank=True, null=True, related_name="ldap")
    process_type = models.CharField(max_length=50, blank=False, choices=(
        ('TAG', 'TAG'),
        ('SHOPPING', 'SHOPPING'),
        ('WPP', 'WPP'),
        ('MIGRATION', 'MIGRATION'),)
    )
    team_lead = models.ManyToManyField(User, related_name="team_lead")
    team_manager = models.ManyToManyField(User, related_name="team_manager")
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def location_list(self):
        return ", ".join(["%s" % (l.location_name) for l in self.location.all()])

    def team_lead_list(self):
        return ", ".join(["%s %s" % (usr.first_name, usr.last_name) for usr in self.team_lead.all()])

    def team_manager_list(self):
        return ", ".join(["%s %s" % (usr.first_name, usr.last_name) for usr in self.team_manager.all()])

    def __str__(self):              # __unicode__ on Python 2
        return self.team_name

    class Meta:
        db_table = 'regalix_teams'
        ordering = ['team_name']
        verbose_name_plural = "Regalix Teams"


class ChatMessage(models.Model):
    """ Chat Message Model """

    lead = models.ForeignKey(Leads, null=False)
    user_id = models.CharField(max_length=255, null=False)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'chat_message'
        verbose_name_plural = 'Chat Message'


class AgencyDetails(models.Model):
    """ Agency Details """

    google_rep = models.ForeignKey(User)
    agency_name = models.CharField(max_length=255, null=False)
    location = models.ForeignKey(Location, null=False)
    timezone = models.ForeignKey(Timezone, null=False)
    language = models.ForeignKey(Language, null=True, blank=True)
    appointment_date = models.DateTimeField(default=datetime.utcnow())

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        db_table = 'agency_details'
        verbose_name_plural = 'Agency Details'


class ContactPerson(models.Model):
    """ Contact Persons """

    contact_person = models.CharField(max_length=255, null=False)
    contact_email = models.EmailField(max_length=255, null=False, unique=True)
    contact_phone = models.CharField(max_length=255, null=False)
    agency = models.ForeignKey(AgencyDetails)
    person_id = models.CharField(max_length=255, null=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        db_table = 'contact_person'
        verbose_name_plural = 'Contact Person'


class LeadForm(models.Model):
    """ Lead Form Names """
    name = models.CharField(max_length=255, null=False, unique=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lead_forms'
        verbose_name_plural = 'Lead Forms'


class LeadFormAccessControl(models.Model):
    """ Lead Form Access Control """

    lead_form = models.ForeignKey(LeadForm, unique=True)
    programs = models.ManyToManyField(Team, blank=True, null=True)
    target_location = models.ManyToManyField(Location, blank=True, null=True)
    google_rep = models.ManyToManyField(User, blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def program_list(self):
        return ", ".join(["%s" % (p.team_name) for p in self.programs.all()])

    def location_list(self):
        return ", ".join(["%s" % (l.location_name) for l in self.target_location.all()])

    def rep_list(self):
        return ", ".join(["%s" % (r.get_full_name()) for r in self.google_rep.all()])

    # def __str__(self):
    #     return self.lead_form

    class Meta:
        db_table = 'lead_form_controls'
        verbose_name_plural = 'Lead Form Access Controls'


class SfdcUsers(models.Model):
    """ SFDC Users List """

    user_id = models.CharField(max_length=255, null=False)
    full_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        db_table = 'sfdc_users'
        verbose_name_plural = 'SFDC Users'


class TreatmentType(models.Model):
    """ Treatment Type List """

    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'treatment_type'
        ordering = ['name']
        verbose_name_plural = "Treatment Types"


class PicassoLeads(models.Model):
    google_rep_name = models.CharField(max_length=255)
    google_rep_email = models.CharField(max_length=255)

    lead_owner_name = models.CharField(max_length=255, null=False)
    lead_owner_email = models.CharField(max_length=255, null=False)
    company = models.CharField(max_length=255)
    lead_status = models.CharField(max_length=50)
    country = models.CharField(max_length=255)

    customer_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    date_of_installation = models.DateTimeField(blank=True, null=True)

    regalix_comment = models.TextField()
    google_comment = models.TextField()

    code_1 = models.TextField()
    url_1 = models.CharField(max_length=255)
    type_1 = models.CharField(max_length=150)
    comment_1 = models.TextField()

    team = models.CharField(max_length=100)
    is_active = models.IntegerField(default=1)

    tat = models.IntegerField(default=0)

    created_date = models.DateTimeField(default=datetime.utcnow())
    updated_date = models.DateTimeField(default=datetime.utcnow(), auto_now=True)

    sf_lead_id = models.CharField(max_length=50, unique=True)
    additional_notes = models.TextField(default='')
    picasso_objective = models.CharField(max_length=255, null=True, blank=True)
    internal_cid = models.CharField(max_length=50, null=True)
    pod_name = models.CharField(max_length=50)
    treatment_type = models.CharField(max_length=100, blank=True, null=True)
    is_build_eligible = models.BooleanField(default=False)
    ref_uuid = models.CharField(max_length=100, blank=True, null=True)
    estimated_tat = models.DateTimeField(blank=True, null=True)
    crop_email = models.CharField(max_length=100, default='')
    my_advitiser_email = models.CharField(max_length=100, default='', blank=True, null=True)
    my_cases_alias = models.CharField(max_length=100, default='', blank=True, null=True)
    market_selector = models.CharField(max_length=100, default='', blank=True, null=True)
    language_selector = models.CharField(max_length=100, default='', blank=True, null=True)
    picasso_type = models.CharField(max_length=100, default='PICASSO', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Picasso Leads"


class BlackListedCID(models.Model):
    cid = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    modified_by = models.ForeignKey(User, related_name='modified_by_user',default='', blank=True, null=True)
    created_date = models.DateTimeField(default=datetime.utcnow())
    modified_date = models.DateTimeField(default=datetime.utcnow(), auto_now=True)


# New feature for builds similar to Picasso Bolt
class BuildsBoltEligibility(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    cid = models.CharField(max_length=20)
    url = models.CharField(max_length=500, blank=True, null=True)
    domain = models.CharField(max_length=150, blank=True, null=True)
    bolt_eligible = models.BooleanField(default=True)
    last_assessed_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'builds_bolt_eligibility'
        verbose_name_plural = 'Builds Bolt Eligibility'


class WhiteListedAuditCID(models.Model):
    external_customer_id = models.CharField(max_length=50, unique=True)
    opportunity_type = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.utcnow())
    modified_date = models.DateTimeField(default=datetime.utcnow(), auto_now=True)
