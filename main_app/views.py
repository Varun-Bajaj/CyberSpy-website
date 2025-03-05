from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index_page(request):
    

    return render(request,"index.html")