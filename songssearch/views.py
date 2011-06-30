from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context
from models import *
from django.template.loader import get_template
from django.utils import simplejson
#from admin import *


def index(request):

    song_list= Song.objects.all()
    sl= Song.objects.all()
    result=sl
    '''if request.method == "POST":
        sl = song_list.filter(title__icontains = request.POST['songtitle'])
	result = sl
	html = result'''
    if request.method == "POST":
        songs = Song.objects.filter(title__icontains = request.POST['songtitle'])
	result = "<div class=\"search_result\">"
	for song in songs:
	    result = result +  "<div class=\"query\"> "
	    result = result +  "<h3>" + song.title  + "</h3>"
            groups = SongsSimilar.objects.filter(song = song)
            for group in groups:
                similar = SongsSimilar.objects.filter(group = group.group) 
                for s in similar:
                    songinfo = Song.objects.get(id = s.song_id )
                    result = result +  "<i><h4>" + s.song.artist + " - " + s.song.title + ", (" + s.song.year + ")"  + "</h4></i>" 
            result = result +  "</div>"
        result = result +  "</div>"
    
    context= {'song_list':result}
    return render_to_response('index.html', context,
                               context_instance=RequestContext(request))

def search(request):
    if request.method == "GET":
        songs = Song.objects.filter(title__icontains = request.GET['text'])
	result = "<div class=\"search_result\">"
	for song in songs:
	    result = result +  "<div class=\"query\"> "
	    result = result +  "<h3>" + song.title  + "</h3>"
            groups = SongsSimilar.objects.filter(song = song)
            for group in groups:
                similar = SongsSimilar.objects.filter(group = group.group) 
                for s in similar:
                    songinfo = Song.objects.get(id = s.song_id )
                    result = result +  "<i><h4>" + s.song.artist + " - " + s.song.title + ", (" + s.song.year + ")"  + "</h4></i>" 
            result = result +  "</div>"
        result = result +  "</div>"
	html = result
        return HttpResponse(html, mimetype='application/javascript')

