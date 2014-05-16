from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    return render_to_response("home/index.html",
                              context_instance=RequestContext(request))
def logout(request):
    request.session.items = []
    request.session.modified = True
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    
