# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.execute("ALTER TABLE leads_leads MODIFY sf_lead_id varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL")

    def backwards(self, orm):
        db.execute("ALTER TABLE leads_leads MODIFY sf_lead_id varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL")

    models = {
        u'leads.leads': {
            'Meta': {'object_name': 'Leads'},
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
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 17, 0, 0)'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_of_installation': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'ecommerce': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email_logs': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'emails_received': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'emails_sent': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name_optional': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'google_comment': ('django.db.models.fields.TextField', [], {}),
            'google_rep_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'google_rep_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lead_owner': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'no_of_calls_inbound': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'no_of_calls_outbound': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'regalix_comment': ('django.db.models.fields.TextField', [], {}),
            'sf_lead_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'type_1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_2': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_3': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_4': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_5': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 17, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'url_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_3': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_4': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_5': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['leads']