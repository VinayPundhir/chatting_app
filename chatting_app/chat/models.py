from __future__ import unicode_literals

from django.db import models


class UserData(models.Model):
    image = models.ImageField(upload_to="pictures")
    name = models.CharField(max_length=20)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    color = models.CharField(max_length=20, default="white")


class FriendRequest(models.Model):
    name = models.CharField(max_length=20)
    Request = models.CharField(max_length=20)


class Friend(models.Model):
    name = models.CharField(max_length=20)
    friend_name = models.CharField(max_length=20)


class ChatData(models.Model):
    name = models.CharField(max_length=20)
    friend_name = models.CharField(max_length=20)
    msg = models.CharField(max_length=254, default="")
    image = models.ImageField(upload_to="pictures", default="cht2.jpeg")
    num = models.IntegerField()


class MessageTracker(models.Model):
    name = models.CharField(max_length=5)
    num = models.IntegerField()


class Active(models.Model):
    name = models.CharField(max_length=30)


class Channel(models.Model):
    channel_name = models.CharField(max_length=40)
    name = models.CharField(max_length=20)
    friend_name = models.CharField(max_length=20)
