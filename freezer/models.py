from django.db import models
from datetime import datetime, timedelta

#################################
#   Hierarchy of dependence     #
#################################
#
#   NOTES:
#           - TOP:          Highly dependent models (basal nodes)
#           - BOTTOM:       Least dependent models (terminal nodes)
#
#           - THEREFORE:    If the database needs to be reconstructed, we start by populating
#                           the least dependent fields first
#
# lvl.1          lesson_________________tutor
#                |           __|__
#                |          |     |
# lvl.2    student   location    subject
#

#################################
#          Core models          #
#################################

class location(models.Model):
	postcode		= models.CharField(max_length=7,unique=True)
	area			= models.CharField(max_length=250)

class university(models.Model):
	name		= models.CharField(max_length=100,unique=True)

class degree(models.Model):
	name		= models.CharField(max_length=100,unique=True)

class subject(models.Model):
	SUBJECT_CHOICES = (
		(u'PHY', u'Physics'),
		(u'BIO', u'Biology'),
		(u'CHEM', u'Chemistry'),
		(u'MATH', u'Mathematics'),
	)

	BOARD_CHOICES = (
		(u'AQA', u'AQA'),
		(u'EDX', u'Edexcel'),
		(u'OCR', u'OCR'),
		(u'WJEC', u'WJEC'),
		(u'CIE', u'Cambridge International Examinations)'),
		(u'CCEA', u'CCEA'),
		(u'ICAAE', u'ICAAE'),
	)

	KEYSTAGE_CHOICES = (
		(u'KS3Y7', u'Year 7'),
		(u'KS3Y8', u'Year 8'),
		(u'KS3Y9', u'Year 9'),
		(u'GCSEY10', u'Year 10'),
		(u'GCSEY11', u'Year 11'),
		(u'AS', u'Year 12'),
		(u'A2', u'Year 13'),
		(u'GCSE', u'GCSE'),
	)

	subject         = models.CharField(max_length=4, choices=SUBJECT_CHOICES)
	examboard       = models.CharField(max_length=10, choices=BOARD_CHOICES,null=True)
	keystage        = models.CharField(max_length=10, choices=KEYSTAGE_CHOICES)

### Use form to prompt students to enter subject, board and keystage
### If the combo already exist then don't enter into subject tables
### Else insert new subject entry
### Get the ID of the entry as part of student record entry

class student(models.Model):
	firstname       = models.CharField(max_length=50)      # e.g. Hyuk-Jin
	lastname        = models.CharField(max_length=50)
	# Implement Autocompletion and furture implementation of school table
	address			= models.CharField(max_length=250)
	school          = models.CharField(max_length=100)      # e.g. St. Mary
	expired         = models.BooleanField()      # e.g. TRUE // FALSE

	location_key    = models.ForeignKey(location)

	def __unicode__(self):
		return "%s %s: %s" % (self.firstname, self.lastname, self.school)


class tutor(models.Model):
	firstname       = models.CharField(max_length=50)      # Andrew
	lastname        = models.CharField(max_length=50)      # Brockman
	email    		= models.EmailField(max_length=255)
	phone	    	= models.CharField(max_length=11, null=True)
	trained         = models.BooleanField(default=0)      # e.g. TRUE // FALSE field used by us
	university_key  = models.ForeignKey(university)
	degree_key      = models.ForeignKey(degree)
	location_key    = models.ForeignKey(location)
	subject_key     = models.ManyToManyField(subject)

	def __unicode__(self):
		return "%s %s: %s" % (self.firstname, self.lastname, self.university_key)



class lesson(models.Model):
	vacancy         = models.NullBooleanField()      # open=FALSE, occupied=TRUE, expired=NULL
	date            = models.DateField()
	starttime       = models.TimeField()
	endtime         = models.TimeField()

	subject_key     = models.ForeignKey(subject)
	location_key    = models.ForeignKey(location)
	student_key     = models.ForeignKey(student)
	tutor_key       = models.ForeignKey(tutor)

#	def __unicode__(self):
#		return "%s %s: %s" % (self.subject, self.lastname, self.university_key)
