from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	super_category = models.ForeignKey('self', blank=True, null=True)

	def __unicode__(self):
		return self.name



class Issue(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	

	latitude  = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	longitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)

	category = models.ForeignKey(Category, null=True, blank=True)

	def _unicode_(self):
		return self.name



