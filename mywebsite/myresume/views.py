from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader


def home(request):
    return render(request, 'myresume/intro.html')


def intro(request):
    return render(request, 'myresume/intro.html')


def resume(request):
    return render(request, 'myresume/resume.html')


def education(request):
    return render(request, 'myresume/education.html')


def projects(request):
    return render(request, 'myresume/projects.html')


def experience(request):
    return render(request, 'myresume/experience.html')


def goals(request):
    return render(request, 'myresume/goals.html')