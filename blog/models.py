from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thumbnail = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    event_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    tag1 = 'study session'
    tag2 = 'gym session'
    tag3 = 'campus event'
    tag4 = 'club event'
    tag5 = 'important'
    tag_choices = [
        (tag1, 'study session'),
        (tag2, 'gym session'),
        (tag3, 'campus event'),
        (tag4, 'club event'),
        (tag5, 'important'),
    ]
    tag = models.CharField(max_length=15, blank=True, null=True, choices=tag_choices)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
