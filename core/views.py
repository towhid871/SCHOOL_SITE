# core/views.py
from django.views.generic import TemplateView

from django.shortcuts import render

# def home(request):
#     context = {
#         'title': 'Home - School Management System',
#         'page': 'home'
#     }
#     return render(request, 'home.html', context)

# def about(request):
#     context = {
#         'title': 'About Us - School Management System',
#         'page': 'about'
#     }
#     return render(request, 'about.html', context)

# def contact(request):
#     context = {
#         'title': 'Contact Us - School Management System',
#         'page': 'contact'
#     }
#     return render(request, 'contact.html', context)



# def admission(request):
#     context = {
#         'title': 'Admission - Open for Enrollment',
#         'page': 'admission'
#     }
#     return render(request, 'admission.html', context)




class HomePageView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home | School Management System'
        context['page'] = 'home'
        return context
    

class AboutPageView(TemplateView):
    template_name = 'about.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us | School Management System'
        context['page'] = 'about'
        return context
    

class ContactPageView(TemplateView):
    template_name = 'contact.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us | School Management System'
        context['page'] = 'contact'
        return context


class AdmissionPageView(TemplateView):
    template_name = 'admission.html'
    context_object_name = 'admission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Admission | School Management System'
        context['page'] = 'admission'
        return context
    

