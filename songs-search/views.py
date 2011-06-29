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
    if request.method == "POST":
        sl = song_list.filter(title__icontains = request.POST['songtitle'])
	result = sl
	html = result
    
    context= {'song_list':sl}
    return render_to_response('index.html', context,
                               context_instance=RequestContext(request))

def search(request):
    song_list= Song.objects.all()
    sl= Song.objects.all()
    if request.method == "GET":
        sl = song_list.filter(title__icontains = request.GET['songtitle'])
	result = sl
	html = result
        return HttpResponse(html, mimetype='application/javascript')

