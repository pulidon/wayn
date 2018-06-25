# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Usuario, Evaluacion, Vino, Plan, Maridaje

# Modificaciones a las vistas del panel de administracion
class EvaluacionInline(admin.TabularInline):
	model = Evaluacion

class VinoAdmin(admin.ModelAdmin):

	list_display = (
		'nombre')

class MaridajeAdmin(admin.ModelAdmin):

	list_display = (
		'nombre')

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Evaluacion)
admin.site.register(Vino, VinoAdmin)
admin.site.register(Plan)
admin.site.register(Maridaje, MaridajeAdmin)
