import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Company(models.Model):

    company_name = models.CharField(max_length=50)
    date_of_addition = models.DateTimeField('with us since')
    def __str__(self):
        return self.company_name
    def is_new(self):
        return self.date_of_addition>= timezone.now() - datetime.timedelta(days=7)
