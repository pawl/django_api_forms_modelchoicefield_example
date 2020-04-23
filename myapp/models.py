from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    publications = models.ManyToManyField(Song)
