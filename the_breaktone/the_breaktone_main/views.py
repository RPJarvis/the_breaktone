from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
def index(request):
    context = RequestContext(request)

    return render_to_response('the_breaktone_main/index.html', {}, context)


def listen(request):
    context = RequestContext(request)

    return render_to_response('wild_humans_main/listen.html', {}, context)