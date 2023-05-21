from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *


# Create your views here.
def index(req):
    staff = {'staff': Staff.objects.all()}
    return render(req, 'staff/list.html', staff)


def create(req):
    if req.method == 'GET':
        return render(req, 'staff/insert.html')
    else:
        print(req.POST)
        Staff.objects.create(
            firstName=req.POST['firstName'],
            lastName=req.POST['lastName'],
            email=req.POST['email'],
            password=req.POST['password'],
            country=req.POST['country'],
            city=req.POST['city']
        )
        return render(req, 'staff/list.html')


def update(req, id):
    if req.method == 'GET':
        staff = {'staff': Staff.objects.get(id=id)}
        return render(req, 'staff/update.html', staff)
    else:
        Staff.objects.filter(id=id).update(
            firstName=req.POST['firstName'],
            lastName=req.POST['lastName'],
            email=req.POST['email'],
            password=req.POST['password'],
            country=req.POST['country'],
            city=req.POST['city']
        )
        return index(req)

@login_required()
def delete(req, id):
    Staff.objects.filter(id=id).delete()
    print(id)
    return index(req)
