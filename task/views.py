from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import User


def add(request):
  template = loader.get_template('User.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  z = request.POST['age']
  member = User(name=x, lastname=y, age=z)
  member.save()
  return HttpResponseRedirect(reverse('add'))