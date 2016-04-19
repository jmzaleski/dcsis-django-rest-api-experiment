from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    
    
    def get_absolute_url(self):
        print self.first_name, self.last_name
        #return reverse('whattocallit', kwargs={'first_name':self.first_name})
        #return reverse('person-details', args=[self.first_name])
        #return reverse('person-details', kwargs={'first_name':self.first_name})
        return reverse('person_details')