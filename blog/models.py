from django.conf import settings
from django.db import models
from django.utils import timezone
from hashlib import sha256


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thumbnail = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    event_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class User(models.Model):
    is_club_account = models.BooleanField()
    is_admin_account = models.BooleanField()
    name = models.CharField(max_length=200)
    join_date = models.DateField()
    email = models.CharField(max_length=200)
    hashed_pwd = models.CharField(max_length=50, blank=False, null=False)

<<<<<<< HEAD
    def create_user(self, club_account, admin_account):
        self.join_date = timezone.now()
        self.is_club_account = club_account
        self.is_admin_account = admin_account
        
    def update_credientials(self, iemail, ipwd):
        self.email = iemail
        self.hashed_pwd = sha256(ipwd)

=======
>>>>>>> main

class AttendanceLog(models.Model):
    attendance_id = models.CharField(max_length=200)
    post_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)


class Preference(models.Model):
    preference_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    value = models.CharField(max_length=200)


class Announcement(models.Model):
    announcement_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    post_id = models.CharField(max_length=200)
    is_club_announcement = models.BooleanField()
    is_admin_announcement = models.BooleanField()
<<<<<<< HEAD
    header = models.CharField(max_length=50)
=======
    header= models.CharField(max_length=50)
>>>>>>> main
    message = models.CharField(max_length=200)

