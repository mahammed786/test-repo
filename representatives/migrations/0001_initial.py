# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GoogeRepresentatives'
        db.create_table('google_representatives', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('role', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('user_supporting_region', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('team', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('supervisor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 17, 0, 0))),
        ))
        db.send_create_signal(u'representatives', ['GoogeRepresentatives'])

        # Adding model 'RegalixRepresentatives'
        db.create_table('regalix_representatives', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('supervisor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('team', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('role', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 17, 0, 0))),
        ))
        db.send_create_signal(u'representatives', ['RegalixRepresentatives'])

        # Adding model 'Availability'
        db.create_table('availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('availability_count', self.gf('django.db.models.fields.IntegerField')()),
            ('booked_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_in_utc', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'representatives', ['Availability'])

        # Adding model 'ScheduleLog'
        db.create_table('schedule_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('availability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['representatives.Availability'])),
            ('availability_count', self.gf('django.db.models.fields.IntegerField')()),
            ('booked_count', self.gf('django.db.models.fields.IntegerField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'representatives', ['ScheduleLog'])


    def backwards(self, orm):
        # Deleting model 'GoogeRepresentatives'
        db.delete_table('google_representatives')

        # Deleting model 'RegalixRepresentatives'
        db.delete_table('regalix_representatives')

        # Deleting model 'Availability'
        db.delete_table('availability')

        # Deleting model 'ScheduleLog'
        db.delete_table('schedule_log')


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
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
        u'representatives.availability': {
            'Meta': {'object_name': 'Availability', 'db_table': "'availability'"},
            'availability_count': ('django.db.models.fields.IntegerField', [], {}),
            'booked_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_in_utc': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'representatives.googerepresentatives': {
            'Meta': {'object_name': 'GoogeRepresentatives', 'db_table': "'google_representatives'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 17, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'supervisor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_supporting_region': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'representatives.regalixrepresentatives': {
            'Meta': {'object_name': 'RegalixRepresentatives', 'db_table': "'regalix_representatives'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 17, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'supervisor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'representatives.schedulelog': {
            'Meta': {'object_name': 'ScheduleLog', 'db_table': "'schedule_log'"},
            'availability': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['representatives.Availability']"}),
            'availability_count': ('django.db.models.fields.IntegerField', [], {}),
            'booked_count': ('django.db.models.fields.IntegerField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['representatives']