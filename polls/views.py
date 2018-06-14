from django.shortcuts import render
from django.http import HttpResponse
from . import views
from django.template import loader
from .models import Company
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def all_companies(request):
    our_companies = Company.objects.order_by('-date_of_addition')
#    template = loader.get_template('polls/index.html')
    context = {
        'our_companies':our_companies,
    }
    return render(request,'polls/index.html',context)

def company_inside(request, company_id):
    return HttpResponse("You're looking at company %s" % company_id)