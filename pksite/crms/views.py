from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Company
from django.contrib.auth.models import User
from .forms import CompanyNameForm

def index(request):
    if request.user.is_authenticated:
        return redirect("sections/")
    else:
        return redirect("accounts/login/")
    #return HttpResponse('index')
    

def login(request):
    template = loader.get_template('registration/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def sections(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    template = loader.get_template('crms/sections.html')
    context = {
        
        }
    return HttpResponse(template.render(context, request))

def companies(request):
    if not request.user.is_authenticated:
        return redirect("login")
    companies_list = Company.objects.all()
    template = loader.get_template('crms/companies.html')
    context = {
        'companies_list':companies_list
               }
    return HttpResponse(template.render(context, request))

def addcompany(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.method == 'POST':
        form = CompanyNameForm(request.POST)
        if form.is_valid():
            Company.objects.create(company_name = form.data['company_name'])
            template = loader.get_template('crms/addcompany.html')
            context = {}
            return redirect('companies')
    else:
        form = CompanyNameForm()
    template = loader.get_template('crms/addcompany.html')
    context = {}
    return HttpResponse(template.render(context, request))

def users(request):
    if not request.user.is_authenticated:
        return redirect("login")
    users_list = User.objects.all()
    template = loader.get_template('crms/users.html')
    context = {
        
        'users_list':users_list
        
    }
    return HttpResponse(template.render(context, request))