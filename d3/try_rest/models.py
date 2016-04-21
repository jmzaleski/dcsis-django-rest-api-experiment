from __future__ import unicode_literals

from django.db import models

#fact is, i don't know what these are for
#LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

from django.core.urlresolvers import reverse

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    employee_number = models.CharField(max_length=10)
    
    
    def get_absolute_url(self):
        print self.first_name, self.last_name
        return reverse('employee_details') #name in url
    class Meta:
        ordering = ('employee_number',)