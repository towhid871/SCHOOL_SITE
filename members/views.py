from django.shortcuts import render

# Create your views here.


# views.py
def member_list(request):
    context = {
        'title': 'Members List',
        'page': 'members'
    }
    return render(request, 'members/member_list.html', context)

