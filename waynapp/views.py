# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# Vista del Home
def index(request):
	return render(request, 'waynapp/index.html')
#Vistal del test
def test(request):
	return render(request, 'waynapp/test.html')

# vista del registro
def registro(request):
	return render(request, 'wayn/registro.html')

# vista del plan
def	plan(request):
	return render(request, 'wayn/plan.html')

# vista del balancevinos
def	balancevinos(request):
	return render(request, 'wayn/balancevinos.html')

# vista del match
def	match(request):
	return render(request, 'wayn/match.html')

# vista del checkout
def	checkout(request):
	return render(request, 'wayn/checkout.html')

# vista del confirmacion
def	confirmacion(request):
	return render(request, 'wayn/confirmacion.html')
