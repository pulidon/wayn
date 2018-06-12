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
	cafe = models.CharField(max_length=100, null=False)
	frutos = models.CharField(max_length=100, null=False)
	te = models.CharField(max_length=100, null=False)
	jugo = models.CharField(max_length=100, null=False)
	olor = models.CharField(max_length=100, null=False)
	tierra = models.CharField(max_length=100, null=False)
	estilo = models.CharField(max_length=100, null=False)


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
