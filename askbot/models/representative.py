from django.db import models

class Representative(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        app_label = 'askbot'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        # stub
        return '/'

    def get_avatar_url(self, arg1):
        # stub
        return '/'

    def get_profile_url(self):
        # stub
        return '/'
