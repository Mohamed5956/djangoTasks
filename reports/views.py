from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

# Create your views here.
def list_students(req):
    return  HttpResponseRedirect('/student/')

def list_staff(req):
    return  HttpResponseRedirect('/staff/')

def links(req):
    return render(req,'report/links.html')