# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^test', views.test, name='test'),
	url(r'^registro', views.registro, name='registro'),
	url(r'^plan', views.plan, name='plan'),
	url(r'^balancevinos', views.balancevinos, name='balancevinos'),
	url(r'^match', views.match, name='match'),
	url(r'^perfilvino/(?P<pk>\d+)/$', views.perfilvino, name='perfilvino'),
	url(r'^checkout', views.checkout, name='checkout'),
	url(r'^confirmacion', views.confirmacion, name='confirmacion'),
	#urls para campaña de prelanzamiento
	url(r'^lanzamiento/(?P<referral_code>\d+)$', views.lanzamiento, name='lanzamiento'),
	url(r'^referir_amigo', views.referir_amigo, name='referir_amigo'),
]
