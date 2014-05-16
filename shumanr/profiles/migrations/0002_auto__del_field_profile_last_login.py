# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Profile.last_login'
        db.delete_column(u'profiles_profile', 'last_login')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Profile.last_login'
        raise RuntimeError("Cannot reverse this migration. 'Profile.last_login' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Profile.last_login'
        db.add_column(u'profiles_profile', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True),
                      keep_default=False)


    models = {
        u'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['profiles']