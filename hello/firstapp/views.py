from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import User

def index(request):
    people = User.objects.all()
    return render(request, "index.html", {"people": people})

    # збереження даних в БД
def create(request):
    if request.method == "POST":
        klient = User()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")

# змінення даних у БД
def edit(request, id):
    try:
        person = User.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Клієнт не знайдений</h2>")

# видалення даних із БД
def delete(request, id):
    try:
        person = User.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Клієнт не знайдений</h2>")












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