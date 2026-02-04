from django.shortcuts import render
from django.views.generic import ListView

from routine.models import Routine

# Create your views here.
# def routine_list(request):
#     context = {
#         'title': 'Class Routine',
#         'page': 'routine'
#     }
#     return render(request, 'routine/routine_list.html', context)



class RoutineListView(ListView):
    template_name = 'routine/routine_list.html'
    model = Routine
    context_object_name = 'routines'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class Routine | School Management System'
        context['page'] = 'routine'
        return context