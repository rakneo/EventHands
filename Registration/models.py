from django.db import models
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

event_choices = (('1', 'Science Quiz'),
           ('2', 'Science Model'),
           ('3', 'Paper Presentation'),
           ('4', 'Spell bee'),
           ('5', 'connections'),
           ('6', 'Poster Painting'),
           ('7', 'Short Film'))


class RegisterDesk(models.Model):
    candidate_name = models.CharField(max_length=250)
    candidate_college = models.CharField(max_length=250)
    candidate_email = models.CharField(max_length=150)
    candidate_contact_no = models.CharField(max_length=12)
    events_enrolling = MultiSelectField(choices=event_choices, max_choices=5)



    def get_absolute_url(self):
        return reverse('success')

    def __str__(self):
        return str(self.candidate_name)


class EventList(models.Model):
    events = models.CharField(max_length=200)
    thumb_url = models.CharField(max_length=5000, default=' ')
    event_isStarted = models.BooleanField(default=False)
    event_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.events)


class PaperPresentation(models.Model):
    topic = models.CharField(max_length=250)

    def __str__(self):
        return str(self.topic)



