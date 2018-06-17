from django.shortcuts import render
from django.http import HttpResponse
from . import views
from django.template import loader
from .models import Company
from .forms import CompanyForm, UserDeleteForm
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User, UserManager
from django.forms import ModelForm



def index(request):

    return render(request,'home.html')

def users(request):
    users_list = User.objects.all()
    context = {
        'users_list':users_list,
    }
    return render(request,'users.html',context)

def add_new_company(request):

    return render(request, 'add_new_company.html')

def all_companies(request):
    our_companies = Company.objects.order_by('-date_of_addition')
#    template = loader.get_template('companies/index.html')

    context = {
        'our_companies':our_companies,
    }
    form = CompanyForm(request.POST or None)
    form.is_valid()

    form2 = UserDeleteForm(request.POST or None)
    form2.is_valid()
    if request.method == 'POST' and 'x' in request.POST:
        print(form2)
    if request.method == 'POST' and 'add company' in request.POST:
        print(form)

        company_name = form.cleaned_data['company_name']
        date_of_addition = form.cleaned_data['date_of_addition']
        #print(company_name,date_of_addition)
        new_company = Company(
            company_name=company_name,
            date_of_addition=date_of_addition, )
        new_company.save()
    return render(request, 'index.html', context)

def company_inside(request, company_id):
    return HttpResponse("You're looking at company %s" % company_id)
