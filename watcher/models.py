
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Cat(models.Model):
    name = models.TextField()
    home = models.ForeignKey('Location')
    backup_home = models.ForeignKey('Location', related_name='friendly_cats')
    hunting_grounds = models.ManyToManyField(
        'Location',
        related_name='annoying_cats',
        related_query_name='getoffmylawn'
    )
    parent = models.ForeignKey(
        'Cat',
        null=True,
        blank=True,
        related_name='kittens')


class Location(models.Model):
    name = models.TextField()
    blob = models.TextField()
