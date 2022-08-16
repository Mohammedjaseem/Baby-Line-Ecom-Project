from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static
from Accounts_App.forms import NewUserForm
from Accounts_App.forms import profile_register



def index(request):
    return render(request, 'home/index2.html')

def register(request):
    form = NewUserForm()
    context = {
        'form': form
        }
    return render(request, 'home/register.html', context)
