from django.db import models
import datetime

class Song(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) 
    artist = models.CharField(max_length=200)
    year = models.CharField(max_length=200)	
    similar_songs = models.ManyToManyField("self") 
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.datetime.now())
    
    class Meta:
       ordering = ['title',]
        #verbose_name_plural = 'Studies'

    def __unicode__(self):
       return self.title

    #def get_absolute_url(self):
       #return '%s/' % (self.slug)
