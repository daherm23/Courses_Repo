# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

def index (request): 

	context = {
		"courses": Course.objects.all() 
		}

	return render(request, "courses/index.html", context)

def create (request):
	print "create function" 

	result = Course.objects.basic_validator(request.POST)
	if len(result):
		for error in result:
			messages.info(request, error)  #check platform 
	else: 
		Course.objects.create(Name=request.POST['name'], Desc=request.POST['desc'])
		return redirect('/')

def destroy(request, number): 

	 context = {
	 	"course": Course.objects.get(id = number)
	 }
	 return render(request,'courses/destroy.html', context)

def delete(request, number):
    b = Course.objects.get(id=number)
    b.delete()
    return redirect('/')
