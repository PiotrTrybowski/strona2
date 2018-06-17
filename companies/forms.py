from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CompanyForm(forms.Form):
    company_name = forms.CharField(label= 'company name', max_length=50)
    date_of_addition = forms.DateField(label= 'added when')

class UserDeleteForm(forms.Form):
    company_name = forms.CharField(label='x', max_length=50)
