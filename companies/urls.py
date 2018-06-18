from django.urls import path
from . import views


urlpatterns = [

    path('',views.index,name='index'),
    path('<int:company_id>/', views.company_inside, name='placeholder'),
    path('companies',views.all_companies, name = 'all companies'),
    path('users',views.users, name = 'all users'),
    path('new_company', views.add_new_company, name ='add new company'),
    path('delete_company',views.remove_company, name='delete company'),
    path('delete_user',views.remove_user, name = 'delete user'),
    path('new_user', views.add_new_user, name = 'add new user')


]