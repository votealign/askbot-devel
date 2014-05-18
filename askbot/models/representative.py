from django.db import models

class Representative(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        app_label = 'askbot'

    def __unicode__(self):
        return self.name
