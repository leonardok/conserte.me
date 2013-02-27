from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
import simplejson as json
import urllib2
import logging

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	super_category = models.ForeignKey('self', blank=True, null=True)

	def __unicode__(self):
		return self.name



class Comment(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	comment = models.TextField()

	issue = models.ForeignKey('Issue', blank=True, null=True)

	def __unicode__(self):
		return self.comment


class City(models.Model):
	name = models.CharField(max_length=50)
	state = models.ForeignKey('State', blank=False, null=False)

	def __unicode__(self):
		return self.name


class State(models.Model):
	name = models.CharField(max_length=10)
	long_name = models.CharField(max_length=50)
	country = models.ForeignKey('Country', blank=False, null=False)

	def __unicode__(self):
		return self.name


class Country(models.Model):
	name = models.CharField(max_length=10)
	long_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


class Follower(models.Model):
	email = models.CharField(max_length=100, blank=False, null=False)
	issue = models.ForeignKey('Issue', blank=False, null=False)

	def __unicode__(self):
		return self.email



class Issue(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	owner_email = models.CharField(max_length=200, default="", blank=True)
	owner_receive_email = models.BooleanField(default=True)

	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)

	page_hits = models.IntegerField(default=0)
	
	open = models.BooleanField(default=True)

	latitude  = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	longitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)

	category = models.ForeignKey(Category, null=True, blank=True)
	city = models.ForeignKey(City, null=False, blank=False)

	def __unicode__(self):
		return self.name


	def new_issue_email(self):
		logging.debug('Sending email')
		plaintext = get_template('issues/email_new_issue.txt')

		context = Context({ 'issue': self})
		text_content = plaintext.render(context)
		send_mail('Novo problema cadastrado', text_content, 'avisos@conserte.me',
				    settings.MANAGERS, fail_silently=False)



	def save(self, *args, **kwargs):
		self.name = self.name.capitalize()
		self.description = str(self.description).capitalize()

		if self.latitude and self.longitude:
			url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&latlng=" + str(self.latitude) + "," + str(self.longitude)
			jsondata = json.load(urllib2.urlopen(url))
			logging.debug(url)

			logging.debug(jsondata['results'][0]['address_components'][0]['types'])

			for address_component in jsondata['results'][0]['address_components']:
				# logging.debug(address_component)
				if ('locality' in address_component['types']):
					city_long = address_component['long_name']
					logging.debug('Found city: ' + str(city_long))
				elif ('administrative_area_level_1' in address_component['types']):
					state_short = address_component['short_name']
					state_long = address_component['long_name']
					logging.debug('Found state: ' + str(state_short))
				elif ('country' in address_component['types']):
					country_short = address_component['short_name']
					country_long = address_component['long_name']
					logging.debug('Found country: ' + str(country_long))

			p, created = Country.objects.get_or_create(name=str(country_short), long_name=str(country_long))
			s, created = State.objects.get_or_create(name=str(state_short), long_name=str(state_long), country=p)
			c, created = City.objects.get_or_create(name=city_long, state=s)

			self.city = c
		
		super(Issue, self).save(*args, **kwargs)

