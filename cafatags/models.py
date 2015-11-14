from django.db import models

class Tags(models.Model):
	name = models.CharField(max_length=4)

	def __unicode__(self):
		return self.name

class Txt(models.Model):
	title = models.CharField(max_length=10)
	tag = models.ForeignKey(Tags)
	subTitle = models.CharField(max_length=16)
	txt = models.TextField(max_length=140)

	def __unicode__(self):
		return self.title

# Create your models here.
