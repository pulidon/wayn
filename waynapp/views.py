# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Usuario

# Create your views here.
# Vista del Home
def index(request):
	return render(request, 'waynapp/index.html')

#Vistal del test
def test(request):
	return render(request, 'waynapp/test.html')

# vista del registro
def registro(request):
	if request.method == 'POST':
		usuario = User()
		if usuario.is_valid():
			usuario.save()
			return render(request, 'waynapp/match')
		else:
			return render(request, 'waynapp/registro.html')
	elif request.method == 'GET':
		return render(request, 'waynapp/registro.html')
	else:
		return render(request, 'waynapp/registro.html')
	return render(request, 'waynapp/registro.html')

# vista del plan
def	plan(request):
	return render(request, 'waynapp/plan.html')

# vista del balancevinos
def	balancevinos(request):
	return render(request, 'waynapp/balancevinos.html')

# vista del match
def	match(request):
	return render(request, 'waynapp/match.html')

# vista del checkout
def	checkout(request):
	return render(request, 'waynapp/checkout.html')

# vista del confirmacion
def	confirmacion(request):
	return render(request, 'waynapp/confirmacion.html')
