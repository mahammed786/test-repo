from django.db import models
from leads.models import Location


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
