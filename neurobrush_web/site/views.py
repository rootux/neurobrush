# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404


def start(request):
    template = loader.get_template('start.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))	

def sockets(request):
    template = loader.get_template('sockets.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

