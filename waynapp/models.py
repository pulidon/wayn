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
	nombre = models.CharField(max_length=100, null=False)
#cuerpo-cafe
#astringencia-te
#frutos_rojos-frutos_rojos
#frutos_negros-frutos_negros
#fruta_citrica-fruta_citrica
#fruta_hueso
#fruta_tropical
#aroma

#class Subscripcion(models.Model):
