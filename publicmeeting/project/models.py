#from django.contrib.gis.db import models
from django.db import models

from .utils import slugify_uniquely

class TimestampedModel (models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


class Meeting (TimestampedModel):
    title = models.CharField(max_length=1023)
    """The title of the meeting"""

    slug = models.SlugField(blank=True)
    """The meeting slug"""

    description = models.TextField(null=True, blank=True)
    """The meeting description, potentially including the agenda."""

    begin_time = models.DateTimeField(null=True, blank=True)
    """When does the meeting start.  NULL means TBD."""

    end_time = models.DateTimeField(null=True, blank=True)
    """When does the meeting end.  NULL means ???."""

    venue_name = models.TextField(null=True, blank=True)
    """The name or address of the venue.  NULL means TBD."""

#    venue_location = models.PointField(null=True, blank=True)
#    """The geographical location of the venue.  NULL means TBD."""

    venue_additional = models.TextField(null=True, blank=True)
    """Additional information about the venue, such as room number."""

    speakers = models.ManyToManyField('auth.User', related_name='speaking_meetings', blank=True)
    attendees = models.ManyToManyField('auth.User', related_name='attending_meetings', blank=True)
    """Who is attending and/or speaking at the meeting"""

#    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_uniquely(self.title, Meeting)

        return super(Meeting, self).save(*args, **kwargs)


class MeetingTag (models.Model):
    text = models.CharField(max_length=255)
    """The tag text"""
