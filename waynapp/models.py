# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
	evaluacion = models.CharField(max_length=100, null=False)
#direccion
#referenciapayu

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
