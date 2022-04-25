from django.db import models
from django.contrib.auth.models import User

class Reg(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return str(self.username)

class Year(models.Model):
    date = models.IntegerField(default=0, primary_key=True)
    top_genre = models.CharField(max_length=200)
    def __str__(self):
        return str(self.date)

class Song(models.Model):
    song_name = models.CharField(max_length=200, primary_key=True)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_name

class Rating(models.Model): # each rating is associated to a user and a song, if either is deleted, so is the rating
    user = models.ForeignKey(Reg, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user.username + ' : ' + self.song.song_name + " --> " + str(self.rating))
