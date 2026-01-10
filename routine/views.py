from django.shortcuts import render

# Create your views here.
def routine_list(request):
    context = {
        'title': 'Class Routine',
        'page': 'routine'
    }
    return render(request, 'routine/routine_list.html', context)