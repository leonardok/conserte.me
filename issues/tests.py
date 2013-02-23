"""
Tests for Issues

Information about testing in Django can be found at:
https://docs.djangoproject.com/en/dev/topics/testing/
https://docs.djangoproject.com/en/dev/topics/testing/overview/

To run the tests:
./manage.py test issues.APITest
"""

from django.test import TestCase
from django.test.client import Client


class APITest(TestCase):
    c = Client()

    def test_api_issue_creation(self):
        """ POST to create an issue """

	import simplejson
	data = {"issue": {'name': 'test issue', 'description': 'test description', 'latitude': '50', 'longitude': '30'}}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	
        response = self.c.post('/api/issues/', simplejson.dumps(data), headers)
        print response
        self.assertEqual(response.status_code, 200)

    def test_api_issue_get(self):
        response = self.c.get('/api/issues/')
        self.assertEqual(response.status_code, 200)

    def test_api_issue_get_all(self):
        response = self.c.get('/api/issues/')
        self.assertEqual(response.status_code, 200)
