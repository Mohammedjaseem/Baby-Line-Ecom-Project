from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from Admin_App.models import product_model, subcategory_model,category_model

# Create your views here.
def index(request):
    product = {
        'main_category': category_model.objects.all(),
        'category': subcategory_model.objects.all(),
        'products' : product_model.objects.all()
    }
    return render(request, 'Shop_templates/index.html', product)