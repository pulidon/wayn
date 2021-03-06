# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string
import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from payuconnector.connector import Suscripcion
from .models import Usuario, Evaluacion, Vino, Plan, Prospecto, Direcciones_ip, Article



class Puntaje:
	pk = ''
	nombre = ''
	cepa = ''
	tipo = ''
	origen = ''
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
	coincidencia = 0

# Create your views here.
# Vista del Home
def index(request):
	return redirect('lanzamiento')
	# send_mail('test', 'body of the message', 'contacto@wayn.com.co', ['nicolaspulido89@hotmail.com', 'georgeladinog@gmail.com'])
	# return render(request, 'waynapp/index.html')

#Vistal del test
def test(request):
	return render(request, 'waynapp/test.html')

# vista del registro
def registro(request):
	if request.method == 'POST':
		usuario = User()
		evaluacion = Evaluacion()
		usuario.name = request.POST['name']
		usuario.username = request.POST['email']
		usuario.email = request.POST['email']
		usuario.password = request.POST['password']
		usuario.save()
		evaluacion.usuario = usuario
		evaluacion.cuerpo = request.POST['cuerpo']
		evaluacion.frutos_rojos = request.POST['frutos_rojos']
		evaluacion.frutos_negros = request.POST['frutos_negros']
		evaluacion.astringencia = request.POST['astringencia']
		evaluacion.citrico = request.POST['citrico']
		evaluacion.fruta_hueso = request.POST['fruta_hueso']
		evaluacion.fruta_tropical = request.POST['fruta_tropical']
		evaluacion.aroma_floral = request.POST['aroma_floral']
		evaluacion.aroma_herbal = request.POST['aroma_herbal']
		evaluacion.tierra = request.POST['tierra']
		usuario.save()
		evaluacion.save()
		login(request,usuario)
		return render(request, 'waynapp/plan.html')
	else:
		return render(request, 'waynapp/registro.html')
	return render(request, 'waynapp/registro.html')

# vista del plan
def plan(request):
	return render(request, 'waynapp/plan.html')

# vista del balancevinos
def balancevinos(request):
	if request.method == 'POST':
		try:
			plan=Plan.objects.get(usuario=request.user)
			plan.usuario = request.user
			plan.plan = request.POST['plan']
			plan.balance = request.POST['balance']
			plan.sugerencia = ''
			plan.save()
			return redirect('match')
		except Plan.DoesNotExist:
			plan = Plan()
			plan.usuario = request.user
			plan.plan = request.POST['plan']
			plan.balance = request.POST['balance']
			plan.sugerencia = ''
			plan.save()
			return redirect('match')
	else:
		return render(request, 'waynapp/balancevinos.html')
	return render(request, 'waynapp/balancevinos.html')

# vista del match
def match(request):
	lista_vinos = Vino.objects.order_by('pk')
	evaluacion = Evaluacion.objects.get(usuario=request.user)
	plan = Plan.objects.get(usuario=request.user)
	lista_puntajes = []
	for vino in lista_vinos:
		puntaje = Puntaje()
		puntaje.pk = vino.pk
		puntaje.nombre = vino.nombre
		puntaje.cepa = vino.cepa
		puntaje.tipo = vino.tipo
		puntaje.origen = vino.origen
		if vino.tipo == "Tinto":
			puntaje.cuerpo = abs(evaluacion.cuerpo - vino.cuerpo)
			puntaje.frutos_rojos = abs(evaluacion.frutos_rojos - vino.frutos_rojos)
			puntaje.frutos_negros = abs(evaluacion.frutos_negros - vino.frutos_negros)
			puntaje.astringencia = abs(evaluacion.astringencia - vino.astringencia)
			puntaje.citrico = 0
			puntaje.fruta_hueso = 0
			puntaje.fruta_tropical = 0
			puntaje.aroma_floral = abs(evaluacion.aroma_floral - vino.aroma_floral)
			puntaje.aroma_herbal = abs(evaluacion.aroma_herbal - vino.aroma_herbal)
			puntaje.tierra = abs(evaluacion.tierra - vino.tierra)
		elif vino.tipo == "Blanco":
			puntaje.cuerpo = abs(evaluacion.cuerpo - vino.cuerpo)
			puntaje.frutos_rojos = 0
			puntaje.frutos_negros = 0
			puntaje.astringencia = 0
			puntaje.citrico = abs(evaluacion.citrico - vino.citrico)
			puntaje.fruta_hueso = abs(evaluacion.fruta_hueso - vino.fruta_hueso)
			puntaje.fruta_tropical = abs(evaluacion.fruta_tropical - vino.fruta_tropical)
			puntaje.aroma_floral = abs(evaluacion.aroma_floral - vino.aroma_floral)
			puntaje.aroma_herbal = abs(evaluacion.aroma_herbal - vino.aroma_herbal)
			puntaje.tierra = 0
		puntaje.total = puntaje.cuerpo + puntaje.frutos_rojos + puntaje.frutos_negros + puntaje.astringencia + puntaje.citrico + puntaje.fruta_hueso + puntaje.fruta_tropical + puntaje.aroma_floral + puntaje.aroma_herbal + puntaje.tierra
		if vino.tipo == "Tinto":
			puntaje.coincidencia = 100-((puntaje.cuerpo + puntaje.frutos_rojos + puntaje.frutos_negros + puntaje.astringencia + puntaje.citrico + puntaje.fruta_hueso + puntaje.fruta_tropical + puntaje.aroma_floral + puntaje.aroma_herbal + puntaje.tierra)/7)
		elif vino.tipo == "Blanco":
			puntaje.coincidencia = 100-((puntaje.cuerpo + puntaje.frutos_rojos + puntaje.frutos_negros + puntaje.astringencia + puntaje.citrico + puntaje.fruta_hueso + puntaje.fruta_tropical + puntaje.aroma_floral + puntaje.aroma_herbal + puntaje.tierra)/6)
		lista_puntajes.append(puntaje)
	lista_puntajes.sort(key=lambda puntaje: puntaje.total,reverse=False)
	if plan.balance == '2 TINTOS ':
		sugerencia = sugerencias(2,0,lista_puntajes)
	elif plan.balance == '1 TINTO 1 BLANCO ':
		sugerencia = sugerencias(1,1,lista_puntajes)
	elif plan.balance == '2 BLANCOS ':
		sugerencia = sugerencias(1,2,lista_puntajes)
	elif plan.balance == '3 TINTOS ':
		sugerencia = sugerencias(3,0,lista_puntajes)
	elif plan.balance == '2 TINTOS 1 BLANCO ':
		sugerencia = sugerencias(2,1,lista_puntajes)
	elif plan.balance == '1 TINTOS 2 BLANCOS ':
		sugerencia = sugerencias(1,2,lista_puntajes)
	elif plan.balance == '3 BLANCOS ':
		sugerencia = sugerencias(0,3,lista_puntajes)
	elif plan.balance == '4 TINTOS ':
		sugerencia = sugerencias(4,0,lista_puntajes)
	elif plan.balance == '3 TINTOS 1 BLANCO ':
		sugerencia = sugerencias(3,1,lista_puntajes)
	elif plan.balance == '2 TINTOS 2 BLANCOS ':
		sugerencia = sugerencias(2,2,lista_puntajes)
	elif plan.balance == '1 TINTOS 3 BLANCOS ':
		sugerencia = sugerencias(1,3,lista_puntajes)
	elif plan.balance == '4 BLANCOS ':
		sugerencia = sugerencias(0,4,lista_puntajes)
	plan.sugerencia = [ {'pk' : vino.pk} for vino in sugerencia ]
	plan.save()
	context = {
		'sugerencia':sugerencia,
		'lista_puntajes':lista_puntajes
	}
	return render(request, 'waynapp/match.html', context)

# vista perfil del vino
def perfilvino(request,pk):
	vino = Vino.objects.get(pk=pk)
	context = {
		'vino':vino
	}
	return render(request, 'waynapp/perfil_vino.html', context)

# vista del checkout
def checkout(request,discountcode=''):
	if request.method == 'POST':
		# usuario =
		# plan =
		# tarjeta =
		# suscripcion =
		# cargos =
		data_suscripcion = {
			# "plan" : request.POST.get('plancode')
			# "cargos" : request.POST.get('charges')
			"firstName" : request.POST.get('firstName'),
			"lastName" : request.POST.get('lastName'),
			"email" : request.POST.get('email'),
			"telephone" : request.POST.get('telephone'),
			"address" : request.POST.get('address'),
			"address2" : request.POST.get('address2'),
			"save-info" : request.POST.get('save-info'),
			"paymentMethod" : request.POST.get('paymentMethod'),
			"cc-name" : request.POST.get('cc-name'),
			"cc-number" : request.POST.get('cc-number'),
			"cc-expiration" : request.POST.get('cc-expiration'),
			"cc-cvv" : request.POST.get('cc-cvv')
		}
		# realizar suscripcion en PayU
		suscripcion = Suscripcion()
		datasuscripcion = suscripcion.Post()
		context = {'data':data_suscripcion}
		return render(request, 'waynapp/confirmacion.html',context)
	elif request.method == 'GET':
		plan = '3 Botellas de vino'
		planvalue = '155700'
		shipping = '9000'
		# discountcode = 'WAYN20'
		discount = '-20000'
		total = '98000'
		context = {
			"plan" : plan,
			"planvalue" : planvalue,
			"shipping" : shipping,
			"discount" : discount,
			"total" : total
		}

		if discountcode != '':
			context.update({"discountcode" : discountcode})

		# try:
		# 	context.update({"discountcode" : 'CODIGO REMITIDO'})
		# except KeyError:
		# 	context.update({"discountcode" : 'CODIGO ORIGINAL'})


		return render(request, 'waynapp/checkout.html',context)
	return render(request, 'waynapp/checkout.html')

# vista para procesar descuentos
def descuento(request):
	if request.method == 'POST':
		discountcode = request.POST.get('applydiscount')
		#ver validez del cupon
		return redirect('checkout',discountcode)
	else:
		return redirect('checkout')
# vista del confirmacion
def confirmacion(request):
	return render(request, 'waynapp/confirmacion.html')

# Vistas campaña de prelanzamiento con referidos
def lanzamiento(request,referral_code=None):
	if request.method == 'POST':
		ip = request.META.get('HTTP_X_FORWARDED_FOR')
		# ip = request.META.get('REMOTE_ADDR')
		try:
			prospecto = Prospecto.objects.get(email=request.POST.get('email'))
			referrer_code = prospecto.referrer_code
			return redirect('referir_amigo',referrer_code)
		except Prospecto.DoesNotExist:
			try:
				direccion_ip = Direcciones_ip.objects.get(direccion=ip)
				if direccion_ip.conteo < 5:
					direccion_ip.conteo += 1
				else:
					return render(request, 'waynapp/lanzamiento.html')
				direccion_ip.save()
			except Direcciones_ip.DoesNotExist:
				direccion_ip = Direcciones_ip()
				direccion_ip.direccion = ip
				direccion_ip.conteo = 0
				direccion_ip.save()
			prospecto = Prospecto()
			prospecto.email = request.POST.get('email')
		if referral_code == None :
			prospecto.referrer_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
			referrer_code = prospecto.referrer_code
			prospecto.save()
			mailtemplate = get_template('correo_bienvenida.html')
			html = mailtemplate.render()
			msg = EmailMultiAlternatives('Hola! Mira lo fácil que es ganar buen vino', '', 'Wayn <contacto@wayn.com.co>', [prospecto.email])
			msg.attach_alternative(html, "text/html")
			msg.send()
			# send_mail('Bienvenido a Wayn!!', html, 'contacto@wayn.com.co', [prospecto.email])
			return redirect('referir_amigo',referrer_code)
		else:
			prospecto.referrer_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
			prospecto.referral_code = referral_code
			referrer_code = prospecto.referrer_code
			prospecto.save()
			mailtemplate = get_template('correo_bienvenida.html')
			html = mailtemplate.render()
			msg = EmailMultiAlternatives('Hola! Mira lo fácil que es ganar buen vino', '', 'Wayn <contacto@wayn.com.co>', [prospecto.email])
			msg.attach_alternative(html, "text/html")
			msg.send()
			# send_mail('Bienvenido a Wayn!!', html, 'contacto@wayn.com.co', [prospecto.email])
			return redirect('referir_amigo',referrer_code)
	else:
		return render(request, 'waynapp/lanzamiento.html')
	return render(request, 'waynapp/lanzamiento.html')

# Vistas campaña de prelanzamiento con referidos
def referir_amigo(request,referrer_code):
	try:
		conteo = Prospecto.objects.filter(referral_code=referrer_code).count()
	except Prospecto.DoesNotExist:
		conteo = 0
	referrer_code = referrer_code
	context = {
		'referrer_code' : referrer_code,
		'conteo' : conteo
	}
	return render(request, 'waynapp/referir_amigo.html',context)

# Vista para mostrar el Blog
def blog(request):
	articles_list = Article.objects.order_by('pk')
	context = {'articles_list':articles_list}
	return render(request, 'waynapp/blog.html',context)

# Vista para calcular y enviar correos de hitos
def correos_hitos(request):
	try:
		lista_correos = []
		lista_prospectos = Prospecto.objects.order_by('pk')
		for item in lista_prospectos:
			conteo_referidos = len(Prospecto.objects.filter(referral_code=item.referrer_code))
			if 5 <= conteo_referidos < 10:
				mailtemplate = get_template('correo_1er_hito.html')
				html = mailtemplate.render()
				msg = EmailMultiAlternatives('Alcanzaste tu primera meta!!', '', 'Wayn <contacto@wayn.com.co>', [item.email])
				msg.attach_alternative(html,'text/html')
				# msg.send()
				lista_correos.append([item.email,item.referrer_code,conteo_referidos])
			if 10 <= conteo_referidos < 25:
				mailtemplate = get_template('correo_2do_hito.html')
				html = mailtemplate.render()
				msg = EmailMultiAlternatives('Alcanzaste tu segunda meta!!', '', 'Wayn <contacto@wayn.com.co>', [item.email])
				msg.attach_alternative(html,'text/html')
				# msg.send()
				lista_correos.append([item.email,item.referrer_code,conteo_referidos])
			if 25 <= conteo_referidos < 50:
				mailtemplate = get_template('correo_3er_hito.html')
				html = mailtemplate.render()
				msg = EmailMultiAlternatives('Alcanzaste tu tercera meta!!', '', 'Wayn <contacto@wayn.com.co>', [item.email])
				msg.attach_alternative(html,'text/html')
				# msg.send()
				lista_correos.append([item.email,item.referrer_code,conteo_referidos])
			if 50 <= conteo_referidos:
				mailtemplate = get_template('correo_4to_hito.html')
				html = mailtemplate.render()
				msg = EmailMultiAlternatives('Alcanzaste tu cuarta meta!!', '', 'Wayn <contacto@wayn.com.co>', [item.email])
				msg.attach_alternative(html,'text/html')
				# msg.send()
				lista_correos.append([item.email,item.referrer_code,conteo_referidos])
		response = {
			'success': True,
			'msg': json.dumps(lista_correos),
		}
		return JsonResponse( response )
	except Exception as e:
		print (str(e))

# funcion para las sugerencias
def sugerencias(tintos,blancos,lista_puntajes):
	sugerencias = []
	sugerencias_tinto = []
	sugerencias_blanco = []
	for vino in lista_puntajes:
		if vino.tipo == 'Tinto':
			if len(sugerencias_tinto) < tintos :
				sugerencias_tinto.append(Vino.objects.get(pk=vino.pk))
		elif vino.tipo == 'Blanco':
			if len(sugerencias_blanco) < blancos :
				sugerencias_blanco.append(Vino.objects.get(pk=vino.pk))
	sugerencias = sugerencias_tinto + sugerencias_blanco
	return sugerencias
