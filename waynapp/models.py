# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	evaluacion = models.CharField(max_length=100, null=False)
#direccion
#referenciapayu

class Evaluacion(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	cuerpo = models.IntegerField(null=True)
	frutos_rojos = models.IntegerField(null=True)
	frutos_negros = models.IntegerField(null=True)
	astringencia = models.IntegerField(null=True)
	citrico = models.IntegerField(null=True)
	fruta_hueso = models.IntegerField(null=True)
	fruta_tropical = models.IntegerField(null=True)
	aroma_floral = models.IntegerField(null=True)
	aroma_herbal = models.IntegerField(null=True)
	tierra = models.IntegerField(null=True)

class Maridaje(models.Model):
	nombre = models.CharField(max_length=100, null=True)
	imagen = models.FileField(upload_to='static')
	pass

	def __str__ (self):
		return self.nombre

class Vino(models.Model):
	nombre = models.CharField(max_length=50, null=True)
	cepa = models.CharField(max_length=30, null=True)
	tipo = models.CharField(max_length=30, null=True)
	origen = models.CharField(max_length=30, null=True)
	cuerpo = models.IntegerField(null=True)
	frutos_rojos = models.IntegerField(null=True)
	frutos_negros = models.IntegerField(null=True)
	astringencia = models.IntegerField(null=True)
	citrico = models.IntegerField(null=True)
	fruta_hueso = models.IntegerField(null=True)
	fruta_tropical = models.IntegerField(null=True)
	aroma_floral = models.IntegerField(null=True)
	aroma_herbal = models.IntegerField(null=True)
	tierra = models.IntegerField(null=True)
	imagen = models.FileField(upload_to='static')
	notas_de_cata = models.TextField(null=True)
	maridajes = models.ManyToManyField(Maridaje)

class Plan(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	plan = models.CharField(max_length=300, null=True)
	balance = models.CharField(max_length=300, null=True)
	sugerencia = models.CharField(max_length=300, null=True)


class Prospecto(models.Model):
	email = models.CharField(max_length=300, null=False)
	referrer_code = models.CharField(max_length=6, null=False)
	referral_code = models.CharField(max_length=6, null=True)

class Direcciones_ip(models.Model):
	direccion = models.CharField(max_length=20, null=False)
	conteo = models.IntegerField(max_length=5, null=False)

class Article(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField(max_length=2000)
