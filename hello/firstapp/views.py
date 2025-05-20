from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import User

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")  # отримати значення поля Ім'я
        age = request.POST.get("age")  # значення поля Вік
        output = "<h2>Користувач</h2><h3>Ім'я - {0}, Вік – {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponseRedirect("/about")


def show_users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})

def details(request):
    return HttpResponsePermanentRedirect("/")

def m304(request):
    return HttpResponseNotModified()

def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")

def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")

def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")

def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")

def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")

def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")