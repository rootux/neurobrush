from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from neurobrush_web.site import views

urlpatterns = patterns('',
	url(r'^$', views.start, name='start'),
   # url(r'^$', views.category, name='category')
)