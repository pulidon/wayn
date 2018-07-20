# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Usuario, Evaluacion, Vino, Plan, Maridaje, Prospecto, Direcciones_ip

# Modificaciones a las vistas del panel de administracion
class EvaluacionInline(admin.TabularInline):
	model = Evaluacion

class VinoAdmin(admin.ModelAdmin):
	list_display = (
		'nombre',
		'cepa'
		)

class PlanAdmin(admin.ModelAdmin):
	list_display = (
		'usuario',
		'plan',
		'balance'
		)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Evaluacion)
admin.site.register(Vino, VinoAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Maridaje)
admin.site.register(Prospecto)
admin.site.register(Direcciones_ip)
