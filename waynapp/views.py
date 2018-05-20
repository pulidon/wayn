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
