from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    date_of_addition = models.DateTimeField('with us since')

