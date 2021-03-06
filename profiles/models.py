from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username
