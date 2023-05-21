from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from staff.models import Staff
# from student.models import Student
from .forms import *


# Create your views here.
def mylogin(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {"form": form}
        return render(request, 'auth/login.html', context)
    else:
        context = {}
        email = request.POST['email']
        password = request.POST['password']
        user = Staff.objects.filter(email=email, password=password)
        auth_user = authenticate(email=email, password=password)
        # print(request.POST['email'],request.POST['password'])
        if (len(user) == 1 and auth_user):
            request.session["firstName"] = user[0].firstName
            request.session["login"] = True
            # login(request, auth_user)
            return HttpResponseRedirect('/staff/')

        elif (len(user) == 1):
            request.session["firstName"] = user[0].firstName
            request.session["login"] = True
            return HttpResponseRedirect('/staff/')

        else:
            context['message'] = "*Wrong Email or Password"
            context['form'] = LoginForm()
            return render(request, 'auth/login.html', context)


@require_http_methods(['GET', 'POST'])
def myregister(request):
    context = {}
    if request.method == 'GET':
        form = RegisterForm()
        context["form"] = form
        return render(request, 'auth/register.html', context)
    else:
        email = request.POST['email']
        user_exists = Staff.objects.filter(email=email).exists()
        if user_exists:
            form = RegisterForm()
            context["form"] = form
            context["email_message"] = "Email already exists"
            return render(request, 'auth/register.html', context)
        else:
            Staff.objects.create(
                firstName=request.POST["firstName"],
                lastName=request.POST["lastName"],
                email=request.POST["email"],
                password=request.POST["password"],
                country=request.POST["country"],
                city=request.POST["city"]
            )
            return HttpResponseRedirect('/staff/')
