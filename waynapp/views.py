# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Usuario, Vino


class Puntaje:
	nombre = ''
	cepa = ''
	tipo = ''
	origen =
	cuerpo = 0
	frutos_rojos = 0
	frutos_negros = 0
	astringencia = 0
	citrico = 0
	fruta_hueso = 0
	fruta_tropical = 0
	aroma_floral = 0
	aroma_herbal = 0
	tierra = 0
	total = 0

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
		usuario.name = request.POST['name']
		usuario.username = request.POST['email']
		usuario.email = request.POST['email']
		usuario.password = request.POST['password']
		usuario.save()
		return render(request, 'waynapp/plan.html')
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
	lista_vinos = Vino.objects.order_by('pk')
	test_cuerpo = 60
	test_frutos_rojos = 90
	test_frutos_negros = 20
	test_astringencia = 25
	test_citrico = 0
	test_fruta_hueso = 0
	test_fruta_tropical = 0
	test_aroma_floral = 50
	test_aroma_herbal = 50
	test_tierra = 50
	lista_puntajes = []
	for vino in lista_vinos:
		puntaje = Puntaje()
		puntaje.nombre = vino.nombre
		puntaje.cepa = vino.cepa
		puntaje.tipo = vino.tipo
		puntaje.origen = vino.origen
		puntaje.cuerpo = abs(test_cuerpo - vino.cuerpo)
		puntaje.frutos_rojos = abs(test_frutos_rojos - vino.frutos_rojos)
		puntaje.frutos_negros = abs(test_frutos_negros - vino.frutos_negros)
		puntaje.astringencia = abs(test_astringencia - vino.astringencia)
		puntaje.citrico = abs(test_citrico - vino.citrico)
		puntaje.fruta_hueso = abs(test_fruta_hueso - vino.fruta_hueso)
		puntaje.fruta_tropical = abs(test_fruta_tropical - vino.fruta_tropical)
		puntaje.aroma_floral = abs(test_aroma_floral - vino.aroma_floral)
		puntaje.aroma_herbal = abs(test_aroma_herbal - vino.aroma_herbal)
		puntaje.tierra = abs(test_tierra - vino.tierra)
		puntaje.total = puntaje.cuerpo + puntaje.frutos_rojos + puntaje.frutos_negros + puntaje.astringencia + puntaje.citrico + puntaje.fruta_hueso + puntaje.fruta_tropical + puntaje.aroma_floral + puntaje.aroma_herbal + puntaje.tierra
		lista_puntajes.append(puntaje)
	lista_puntajes.sort(key=puntaje.total,reverse=True)
	context = {
		'lista_puntajes':lista_puntajes
	}
	return render(request, 'waynapp/match.html', context)

# vista del checkout
def	checkout(request):
	return render(request, 'waynapp/checkout.html')

# vista del confirmacion
def	confirmacion(request):
	return render(request, 'waynapp/confirmacion.html')
