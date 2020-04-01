from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import get_user_model
from .models import IPModel
import json
import requests
import datetime

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    context = {'name':"Jatin Goel"}
    return render(request,"home.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form' : form
    }
    ip = get_client_ip(request)
    print(ip)
    client_key = "6LdExeUUAAAAAJhCnEynp-PtxjDD6XWk_9SyRWGS"
    secret_key = "6LdExeUUAAAAAInueMBMkEl5-mOXObn__HTxw7T7"
    captcha_data = {
        "secret" : secret_key,
        "response":client_key
    }
    r = requests.post("https://www.google.com/recaptcha/api/siteverify",data=captcha_data)
    response = json.loads(r.text)
    verify = response['success']
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        ip_log = IPModel.objects.create(ip=ip,date=datetime.date.today())
        ip_register_count = IPModel.objects.filter(ip=ip,date=datetime.date.today()).count()
        if(ip_register_count >= 3):
            context['recaptcha'] = True
        new_user = User.objects.create(username=username,email=email,password=password)
        print(new_user)
        
    return render(request,"auth/register.html",context)
