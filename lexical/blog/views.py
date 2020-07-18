from datetime import datetime
#from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Product

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'base.html')

def neuro(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'blog/neuro.html')

def psycho(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'blog/psycho.html')

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

# view of models.py
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
    'title' : obj.title,
    'description' : obj.description,
    'price' : obj.price,
    'summary' : obj.summary,
    'featured' : obj.featured
    }
    return render(request, 'blog/detail.html', context)