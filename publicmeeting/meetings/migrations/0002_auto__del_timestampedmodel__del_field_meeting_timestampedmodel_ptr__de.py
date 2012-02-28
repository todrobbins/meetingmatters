# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'TimestampedModel'
        db.delete_table('meetings_timestampedmodel')

        # Deleting field 'Meeting.timestampedmodel_ptr'
        db.delete_column('meetings_meeting', 'timestampedmodel_ptr_id')

        # Deleting field 'Meeting.slug'
        db.delete_column('meetings_meeting', 'slug')

        # Adding field 'Meeting.id'
        db.add_column('meetings_meeting', 'id', self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True), keep_default=False)

        # Adding field 'Meeting.created_datetime'
        db.add_column('meetings_meeting', 'created_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 2, 28, 10, 53, 10, 907229), blank=True), keep_default=False)

        # Adding field 'Meeting.updated_datetime'
        db.add_column('meetings_meeting', 'updated_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 2, 28, 10, 53, 18, 966185), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'TimestampedModel'
        db.create_table('meetings_timestampedmodel', (
            ('created_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('meetings', ['TimestampedModel'])

        # Adding field 'Meeting.timestampedmodel_ptr'
        db.add_column('meetings_meeting', 'timestampedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['meetings.TimestampedModel'], unique=True, primary_key=True), keep_default=False)

        # Adding field 'Meeting.slug'
        db.add_column('meetings_meeting', 'slug', self.gf('django.db.models.fields.SlugField')(blank=True, default='', max_length=50, db_index=True), keep_default=False)

        # Deleting field 'Meeting.id'
        db.delete_column('meetings_meeting', 'id')

        # Deleting field 'Meeting.created_datetime'
        db.delete_column('meetings_meeting', 'created_datetime')

        # Deleting field 'Meeting.updated_datetime'
        db.delete_column('meetings_meeting', 'updated_datetime')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 10, 53, 18, 975334)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 10, 53, 18, 974783)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'meetings.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'attending_meetings'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'begin_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'speaking_meetings'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1023'}),
            'updated_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'venue_additional': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'venue_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'meetings.meetingtag': {
            'Meta': {'object_name': 'MeetingTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['meetings']