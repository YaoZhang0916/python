# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "login/index.html")

def register(request):
    errors = User.objects.register(request.POST)
    if errors:
        for tag,i in errors.iteritems():
            messages.error(request, i, extra_tags=tag)
        return redirect("/")
    else:
        pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt().encode())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                                   email=request.POST['email'], password=pwHash)
        messages.success(request, "Registered Successfully")
        return redirect("/")

def login(request):
    errors = User.objects.login(request.POST)
    if errors:
        for i in errors:
            print i
            messages.error(request, i)
        return redirect("/")
    else:
        request.session['user_id']=User.objects.get(email=request.POST['email']).id
        request.session['name'] = User.objects.get(email=request.POST['email']).first_name
        print request.session['name']
        return redirect('/appointments')

def logout(request):
    request.session.clear()
    return redirect('/')