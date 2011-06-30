from django.db import models
import datetime

class Song(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) 
    artist = models.CharField(max_length=200, null = True)
    year = models.CharField(max_length=200, null = True)	
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.artist + " - " + self.title + ", (" + self.year + ")"


    #def get_absolute_url(self):
       #return '%s/' % (self.slug)

class SongGroup(models.Model):
    title = models.CharField(max_length=200,null=True)
    similarsongs= models.ManyToManyField(Song, through='SongsSimilar')

    def __unicode__(self):
	if self.title:
            return self.title
        else:
            return self.id


class SongsSimilar(models.Model):
    title = models.CharField(max_length=200,null=True)
    song = models.ForeignKey(Song)
    group = models.ForeignKey(SongGroup)

    def __unicode__(self):
	if self.title:
            return self.title
        else:
            return self.id



