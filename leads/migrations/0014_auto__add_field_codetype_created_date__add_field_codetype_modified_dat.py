# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CodeType.created_date'
        db.add_column('code_types', 'created_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'CodeType.modified_date'
        db.add_column('code_types', 'modified_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'RegalixTeams.created_date'
        db.add_column('regalix_teams', 'created_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'RegalixTeams.modified_date'
        db.add_column('regalix_teams', 'modified_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Location.created_date'
        db.add_column('locations', 'created_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Location.modified_date'
        db.add_column('locations', 'modified_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Timezone.created_date'
        db.add_column('timezone', 'created_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Timezone.modified_date'
        db.add_column('timezone', 'modified_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Team.created_date'
        db.add_column('teams', 'created_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Team.modified_date'
        db.add_column('teams', 'modified_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, default=datetime.datetime(2015, 1, 19, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CodeType.created_date'
        db.delete_column('code_types', 'created_date')

        # Deleting field 'CodeType.modified_date'
        db.delete_column('code_types', 'modified_date')

        # Deleting field 'RegalixTeams.created_date'
        db.delete_column('regalix_teams', 'created_date')

        # Deleting field 'RegalixTeams.modified_date'
        db.delete_column('regalix_teams', 'modified_date')

        # Deleting field 'Location.created_date'
        db.delete_column('locations', 'created_date')

        # Deleting field 'Location.modified_date'
        db.delete_column('locations', 'modified_date')

        # Deleting field 'Timezone.created_date'
        db.delete_column('timezone', 'created_date')

        # Deleting field 'Timezone.modified_date'
        db.delete_column('timezone', 'modified_date')

        # Deleting field 'Team.created_date'
        db.delete_column('teams', 'created_date')

        # Deleting field 'Team.modified_date'
        db.delete_column('teams', 'modified_date')


    models = {
        u'leads.codetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'CodeType', 'db_table': "'code_types'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'leads.leads': {
            'Meta': {'object_name': 'Leads'},
            'appointment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'call_recordings': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'code_1': ('django.db.models.fields.TextField', [], {}),
            'code_2': ('django.db.models.fields.TextField', [], {}),
            'code_3': ('django.db.models.fields.TextField', [], {}),
            'code_4': ('django.db.models.fields.TextField', [], {}),
            'code_5': ('django.db.models.fields.TextField', [], {}),
            'comment_1': ('django.db.models.fields.TextField', [], {}),
            'comment_2': ('django.db.models.fields.TextField', [], {}),
            'comment_3': ('django.db.models.fields.TextField', [], {}),
            'comment_4': ('django.db.models.fields.TextField', [], {}),
            'comment_5': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 19, 0, 0)'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_of_installation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dials': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ecommerce': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email_logs': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'emails_received': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'emails_sent': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'first_contacted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name_optional': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'google_comment': ('django.db.models.fields.TextField', [], {}),
            'google_rep_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'google_rep_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lead_owner_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lead_sub_status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'no_of_calls_inbound': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'no_of_calls_outbound': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'regalix_comment': ('django.db.models.fields.TextField', [], {}),
            'rescheduled_appointment': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sf_lead_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'type_1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_2': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_3': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_4': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_5': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 19, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'url_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_3': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_4': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_5': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'leads.location': {
            'Meta': {'ordering': "['location_name']", 'object_name': 'Location', 'db_table': "'locations'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'flag_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True'}),
            'time_zone': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['leads.Timezone']", 'symmetrical': 'False'})
        },
        u'leads.regalixteams': {
            'Meta': {'ordering': "['team_name']", 'object_name': 'RegalixTeams', 'db_table': "'regalix_teams'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['leads.Location']", 'symmetrical': 'False'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'process_type': ('django.db.models.fields.CharField', [], {'default': "'TAG'", 'max_length': '50'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'leads.team': {
            'Meta': {'ordering': "['team_name']", 'object_name': 'Team', 'db_table': "'teams'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'leads.timezone': {
            'Meta': {'ordering': "['zone_name']", 'object_name': 'Timezone', 'db_table': "'timezone'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_value': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'zone_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['leads']