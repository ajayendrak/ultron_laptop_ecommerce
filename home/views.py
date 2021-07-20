from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .forms import ContactInfoForm
from .models import ContactInfo
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.html')



def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        r_info = ContactInfo(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        print(r_info)
        r_info.save()
        messages.success(request, 'Your message has been sent.')
    return render(request, 'contactus.html')

    



    
def test(request):
    return render(request, 'test.html')

