from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:company_id>/', views.company_inside, name='placeholder'),
    path('companies',views.all_companies, name = 'all companies'),
]