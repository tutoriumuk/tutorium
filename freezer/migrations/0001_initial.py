# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'location'
        db.create_table('freezer_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=7)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('freezer', ['location'])

        # Adding model 'university'
        db.create_table('freezer_university', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('freezer', ['university'])

        # Adding model 'degree'
        db.create_table('freezer_degree', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('freezer', ['degree'])

        # Adding model 'subject'
        db.create_table('freezer_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('examboard', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('keystage', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('freezer', ['subject'])

        # Adding model 'student'
        db.create_table('freezer_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('expired', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('location_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freezer.location'])),
        ))
        db.send_create_signal('freezer', ['student'])

        # Adding model 'tutor'
        db.create_table('freezer_tutor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=11, null=True)),
            ('trained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('zone', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('university_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freezer.university'], null=True)),
            ('degree_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freezer.degree'], null=True)),
            ('location_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freezer.location'], null=True)),
        ))
        db.send_create_signal('freezer', ['tutor'])

        # Adding M2M table for field subject_key on 'tutor'
        m2m_table_name = db.shorten_name('freezer_tutor_subject_key')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm['freezer.tutor'], null=False)),
            ('subject', models.ForeignKey(orm['freezer.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'subject_id'])

        # Adding model 'lesson'
        db.create_table('freezer_lesson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vacancy', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('starttime', self.gf('django.db.models.fields.TimeField')()),
            ('endtime', self.gf('django.db.models.fields.TimeField')()),
            ('subject_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freezer.subject'])),
            ('location_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freezer.location'])),
            ('student_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freezer.student'])),
            ('tutor_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freezer.tutor'])),
        ))
        db.send_create_signal('freezer', ['lesson'])


    def backwards(self, orm):
        # Deleting model 'location'
        db.delete_table('freezer_location')

        # Deleting model 'university'
        db.delete_table('freezer_university')

        # Deleting model 'degree'
        db.delete_table('freezer_degree')

        # Deleting model 'subject'
        db.delete_table('freezer_subject')

        # Deleting model 'student'
        db.delete_table('freezer_student')

        # Deleting model 'tutor'
        db.delete_table('freezer_tutor')

        # Removing M2M table for field subject_key on 'tutor'
        db.delete_table(db.shorten_name('freezer_tutor_subject_key'))

        # Deleting model 'lesson'
        db.delete_table('freezer_lesson')


    models = {
        'freezer.degree': {
            'Meta': {'object_name': 'degree'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'freezer.lesson': {
            'Meta': {'object_name': 'lesson'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'endtime': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['freezer.location']"}),
            'starttime': ('django.db.models.fields.TimeField', [], {}),
            'student_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['freezer.student']"}),
            'subject_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['freezer.subject']"}),
            'tutor_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['freezer.tutor']"}),
            'vacancy': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'freezer.location': {
            'Meta': {'object_name': 'location'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '7'})
        },
        'freezer.student': {
            'Meta': {'object_name': 'student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'expired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'location_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['freezer.location']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'freezer.subject': {
            'Meta': {'object_name': 'subject'},
            'examboard': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keystage': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'freezer.tutor': {
            'Meta': {'object_name': 'tutor'},
            'degree_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['freezer.degree']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'location_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['freezer.location']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True'}),
            'subject_key': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['freezer.subject']", 'null': 'True', 'symmetrical': 'False'}),
            'trained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'university_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['freezer.university']", 'null': 'True'}),
            'zone': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'})
        },
        'freezer.university': {
            'Meta': {'object_name': 'university'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['freezer']