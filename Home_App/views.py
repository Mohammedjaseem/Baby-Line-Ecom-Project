from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static
from Accounts_App.forms import NewUserForm



def index(request):
    form = NewUserForm()
    context = {
        'form': form
        }
    return render(request, 'home/index.html', context)
