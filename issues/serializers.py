from django.forms import widgets
from rest_framework import serializers
from issues import models

class IssueSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Issue
		fields = ('id', 'name')
