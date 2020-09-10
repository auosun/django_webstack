from django.shortcuts import render
from webstack.models import Menu,Website

def indexView(request):
    menus = Menu.objects.all().order_by('-weight')
    websites = Website.objects.all().order_by('-weight')

    return render(request, 'index.html',{"menus":menus,"websites":websites})

