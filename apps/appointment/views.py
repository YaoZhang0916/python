
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import User,Appointments
from django.contrib import messages
import bcrypt

def home(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "You need to log in or register first.", extra_tags = 'login')
        return redirect('/')
    context = {
        "name": request.session["name"],
        'appointments': User.objects.get(id=request.session['user_id']).tasks.all(),
        'all_appointments': Appointments.objects.exclude(users = request.session['user_id'])
    }
    return render(request, 'appointment/appointments.html', context)

def updateAppointment(request, appointments_id):
    errors = Appointments.objects.validator(request.POST)
    if errors:
        for tag,i in errors.iteritems():
            messages.error(request, i, extra_tags=tag)
        return redirect("/appointment")
    else:
        u=User.objects.get(id=request.session['user_id'])
        u.tasks=request.POST['task']
        u.date =request.POST['date']
        u.status = request.POST['status']
        u.time  = request.POST['time']
        u.save()
        return redirect('/appointments')

def addAppointment(request):
    errors = Appointments.objects.validator(request.POST)
    if errors:
        for tag,i in errors.iteritems():
            messages.error(request, i, extra_tags=tag)
        return redirect("/appointment")
    else:
        u=User.objects.get(id=request.session['user_id'])
        u.save()
        appointment=Appointments.objects.create(task=request.POST['task'], data=request.POST['data'],
                                   time=request.POST['time'], status=request.POST['status'])
        appointment.save()
        return redirect('/appointments')

def deleteAppointment(request, appointments_id):
    Appointments.objects.get(id=request.session['user_id']).delete()
    messages.success(request, "Successfully deleted")
    return redirect("/appointment")