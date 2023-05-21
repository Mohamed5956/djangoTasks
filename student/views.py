from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from staff.models import *


# Create your views here.
def index(req):
    student = {'students': Student.objects.all()}
    return render(req, 'student/list.html', student)


def create(req):
    if req.method == 'GET':
        context = {'staff': Staff.objects.all()}
        return render(req, 'student/insert.html', context)
    else:
        print(req.POST)
        Student.objects.create(
            firstName=req.POST['firstName'],
            lastName=req.POST['lastName'],
            email=req.POST['email'],
            password=req.POST['password'],
            country=req.POST['country'],
            city=req.POST['city'],
            staff=Staff.objects.get(id=req.POST['staff_id'])
        )
        return index(req)

def update(req, id):
    if req.method == 'GET':
        context = {'student': Student.objects.get(id=id) , 'staff':Staff.objects.all()}

        return render(req, 'student/update.html', context)
    else:
        Student.objects.filter(id=id).update(
            firstName=req.POST['firstName'],
            lastName=req.POST['lastName'],
            email=req.POST['email'],
            password=req.POST['password'],
            country=req.POST['country'],
            city=req.POST['city'],
            staff=Staff.objects.get(id=req.POST['staff_id'])
        )
        return index(req)


def delete(req, id):
    print("HELLO DELETE")
    Student.objects.filter(id=id).delete()
    print(id)
    return index(req)
