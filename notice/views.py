from django.shortcuts import render

# Create your views here.
def notice_list(request):
    context = {
        'title': 'Notices',
        'page': 'notice'
    }
    return render(request, 'notice/notice_list.html', context)