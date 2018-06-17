from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import views
from django.template import loader
from .models import Company
from .forms import CompanyForm, UserDeleteForm
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User, UserManager
from django.forms import ModelForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.forms.models import modelformset_factory

def index(request):
    return render(request, 'home.html')


def users(request):
    users_list = User.objects.all()
    context = {
        'users_list': users_list,
    }
    return render(request, 'users.html', context)


def add_new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return HttpResponseRedirect('users')
    else:
        form = UserCreationForm()
    return render(request, 'add_new_user.html', {'form': form})


def add_new_company(request):
    return render(request, 'add_new_company.html')


def all_companies(request):
    our_companies = Company.objects.order_by('-date_of_addition')
    #    template = loader.get_template('companies/index.html')

    context = {
        'our_companies': our_companies,
    }
    form = CompanyForm(request.POST or None)
    form.is_valid()
    if request.method == 'POST' and 'add company' in request.POST:
        print(form)

        company_name = form.cleaned_data['company_name']
        date_of_addition = form.cleaned_data['date_of_addition']
        # print(company_name,date_of_addition)
        new_company = Company(
            company_name=company_name,
            date_of_addition=date_of_addition, )
        new_company.save()

    return render(request, 'index.html', context)


def company_inside(request, company_id):
    return HttpResponse("You're looking at company %s" % company_id)


def remove_company(request):
    req = request.POST
    company = req.get('company_id')
    company_to_delete = Company.objects.get(id=company)
    company_to_delete.delete()
    return render(request, 'delete_company.html')


def remove_user(request):
    req = request.POST
    user = req.get('user_id')
    user_to_delete = User.objects.get(id=user)
    user_to_delete.delete()
    return render(request, 'delete_user.html')
