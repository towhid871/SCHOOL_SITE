# core/views.py
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home - School Management System',
        'page': 'home'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'title': 'About Us - School Management System',
        'page': 'about'
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'title': 'Contact Us - School Management System',
        'page': 'contact'
    }
    return render(request, 'contact.html', context)



def admission(request):
    context = {
        'title': 'Admission - Open for Enrollment',
        'page': 'admission'
    }
    return render(request, 'admission.html', context)