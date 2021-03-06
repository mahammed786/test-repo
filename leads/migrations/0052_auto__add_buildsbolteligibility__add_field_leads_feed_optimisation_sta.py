# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Leads.feed_optimisation_status'
        db.add_column(u'leads_leads', 'feed_optimisation_status',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Leads.feed_optimisation_sub_status'
        db.add_column(u'leads_leads', 'feed_optimisation_sub_status',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Leads.number_of_products'
        db.add_column(u'leads_leads', 'number_of_products',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Leads.additional_description'
        db.add_column(u'leads_leads', 'additional_description',
                      self.gf('django.db.models.fields.CharField')(max_length=3000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Leads.area_tobe_improved'
        db.add_column(u'leads_leads', 'area_tobe_improved',
                      self.gf('django.db.models.fields.CharField')(max_length=3000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Leads.shopping_feed_link'
        db.add_column(u'leads_leads', 'shopping_feed_link',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Leads.business_type'
        db.add_column(u'leads_leads', 'business_type',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Leads.authcase_id'
        db.add_column(u'leads_leads', 'authcase_id',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Leads.feed_optimisation_status'
        db.delete_column(u'leads_leads', 'feed_optimisation_status')

        # Deleting field 'Leads.feed_optimisation_sub_status'
        db.delete_column(u'leads_leads', 'feed_optimisation_sub_status')

        # Deleting field 'Leads.number_of_products'
        db.delete_column(u'leads_leads', 'number_of_products')

        # Deleting field 'Leads.additional_description'
        db.delete_column(u'leads_leads', 'additional_description')

        # Deleting field 'Leads.area_tobe_improved'
        db.delete_column(u'leads_leads', 'area_tobe_improved')

        # Deleting field 'Leads.shopping_feed_link'
        db.delete_column(u'leads_leads', 'shopping_feed_link')

        # Deleting field 'Leads.business_type'
        db.delete_column(u'leads_leads', 'business_type')

        # Deleting field 'Leads.authcase_id'
        db.delete_column(u'leads_leads', 'authcase_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'leads.agencydetails': {
            'Meta': {'object_name': 'AgencyDetails', 'db_table': "'agency_details'"},
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'appointment_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'google_rep': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leads.Language']", 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leads.Location']"}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leads.Timezone']"})
        },
        u'leads.blacklistedcid': {
            'Meta': {'object_name': 'BlackListedCID'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'modified_by_user'", 'null': 'True', 'blank': 'True', 'to': u"orm['auth.User']"}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        u'leads.buildsbolteligibility': {
            'Meta': {'object_name': 'BuildsBoltEligibility', 'db_table': "'builds_bolt_eligibility'"},
            'bolt_eligible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_assessed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'leads.chatmessage': {
            'Meta': {'object_name': 'ChatMessage', 'db_table': "'chat_message'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leads.Leads']"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'leads.codetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'CodeType', 'db_table': "'code_types'"},
            'avg_setup_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'leads.contactperson': {
            'Meta': {'object_name': 'ContactPerson', 'db_table': "'contact_person'"},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leads.AgencyDetails']"}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'person_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'leads.language': {
            'Meta': {'object_name': 'Language', 'db_table': "'languages'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'leads.leadform': {
            'Meta': {'object_name': 'LeadForm', 'db_table': "'lead_forms'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'leads.leadformaccesscontrol': {
            'Meta': {'object_name': 'LeadFormAccessControl', 'db_table': "'lead_form_controls'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'google_rep': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leads.LeadForm']", 'unique': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['leads.Team']", 'null': 'True', 'blank': 'True'}),
            'target_location': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['leads.Location']", 'null': 'True', 'blank': 'True'})
        },
        u'leads.leads': {
            'Meta': {'object_name': 'Leads'},
            'additional_description': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'appointment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'appointment_date_in_ist': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'area_tobe_improved': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'authcase_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'business_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_of_installation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dials': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ecommerce': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email_logs': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'emails_received': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'emails_sent': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'eto_ldap': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'feed_optimisation_status': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'feed_optimisation_sub_status': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'first_contacted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name_optional': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gcss': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'google_comment': ('django.db.models.fields.TextField', [], {}),
            'google_rep_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'google_rep_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lead_owner_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lead_sub_status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'no_of_calls_inbound': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'no_of_calls_outbound': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'number_of_products': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'regalix_comment': ('django.db.models.fields.TextField', [], {}),
            'rescheduled_appointment': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rescheduled_appointment_in_ist': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sf_lead_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'shopping_feed_link': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'tat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'type_1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_2': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_3': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_4': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_5': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'url_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_3': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_4': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_5': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wpp_treatment_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'leads.location': {
            'Meta': {'ordering': "['location_name']", 'object_name': 'Location', 'db_table': "'locations'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'daylight_end': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'daylight_start': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'ds_time_zone': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'daylight_timezone'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['leads.Timezone']"}),
            'flag_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['leads.Language']", 'symmetrical': 'False'}),
            'location_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'primary_language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'primary_language'", 'to': u"orm['leads.Language']"}),
            'time_zone': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'standard_timezone'", 'symmetrical': 'False', 'to': u"orm['leads.Timezone']"})
        },
        u'leads.picassoleadgrouptype': {
            'Meta': {'object_name': 'PicassoLeadGroupType'},
            'group_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'leads.picassoleads': {
            'Meta': {'object_name': 'PicassoLeads'},
            'additional_notes': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'code_1': ('django.db.models.fields.TextField', [], {}),
            'comment_1': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)'}),
            'crop_email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_of_installation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_tat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'google_comment': ('django.db.models.fields.TextField', [], {}),
            'google_rep_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'google_rep_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_cid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'is_build_eligible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_selector': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lead_owner_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'market_selector': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'my_advitiser_email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'my_cases_alias': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picasso_objective': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'picasso_type': ('django.db.models.fields.CharField', [], {'default': "'PICASSO'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pod_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ref_uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'regalix_comment': ('django.db.models.fields.TextField', [], {}),
            'sf_lead_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'tat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'treatment_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type_1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'url_1': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'leads.regalixteams': {
            'Meta': {'ordering': "['team_name']", 'object_name': 'RegalixTeams', 'db_table': "'regalix_teams'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ldap': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ldap'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['leads.Location']", 'symmetrical': 'False'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'process_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'program': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['leads.Team']", 'null': 'True', 'blank': 'True'}),
            'team_lead': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team_lead'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'team_manager': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team_manager'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'team_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'leads.sfdcusers': {
            'Meta': {'object_name': 'SfdcUsers', 'db_table': "'sfdc_users'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'leads.team': {
            'Meta': {'ordering': "['team_name']", 'object_name': 'Team', 'db_table': "'teams'"},
            'belongs_to': ('django.db.models.fields.CharField', [], {'default': "'TAG'", 'max_length': '50'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'picasso_lead_group_type': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['leads.PicassoLeadGroupType']", 'null': 'True', 'blank': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'leads.timezone': {
            'Meta': {'ordering': "['zone_name']", 'object_name': 'Timezone', 'db_table': "'timezone'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_value': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'zone_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'leads.timezonemapping': {
            'Meta': {'ordering': "['standard_timezone']", 'unique_together': "(('standard_timezone', 'daylight_timezone'),)", 'object_name': 'TimezoneMapping', 'db_table': "'timezone_mapping'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'daylight_timezone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ds_timezone'", 'unique': 'True', 'to': u"orm['leads.Timezone']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'standard_timezone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'std_timezone'", 'unique': 'True', 'to': u"orm['leads.Timezone']"})
        },
        u'leads.treatmenttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'TreatmentType', 'db_table': "'treatment_type'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'leads.wppleads': {
            'Meta': {'object_name': 'WPPLeads'},
            'additional_notes': ('django.db.models.fields.TextField', [], {'default': "''"}),
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
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)'}),
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
            'is_ab_test': ('django.db.models.fields.CharField', [], {'default': "'YES'", 'max_length': '255', 'null': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'is_build_eligible': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'is_nominated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lead_owner_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lead_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lead_sub_status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'mockup_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'mockup_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'no_of_calls_inbound': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'no_of_calls_outbound': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_optional': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ref_uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'regalix_comment': ('django.db.models.fields.TextField', [], {}),
            'rescheduled_appointment': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rescheduled_appointment_in_ist': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sf_lead_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'stage_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'stage_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'tat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'treatment_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type_1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_2': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_3': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_4': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_5': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 8, 23, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'url_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_3': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_4': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_5': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['leads']