# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from collect import collectData
from getlatestdata import getlatest
import json

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

def collect(request):
    collectData(request)
    return HttpResponse(status=200)

def getLatestData(request):
    data = getlatest(request)
    response = HttpResponse(json.dumps(data))
    response['Access-Control-Allow-Origin'] = '*'
    return HttpResponse(json.dumps(data))