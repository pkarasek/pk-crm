from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('sections/', views.sections, name = 'sections'),
    path('companies/', views.companies, name = 'companies'),
    path('companies/addcompany/', views.addcompany, name = 'addcompany'),
    path('users/', views.users, name = 'users'),
    
]