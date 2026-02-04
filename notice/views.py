from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from notice.models import Notice

# Create your views here.
# def notice_list(request):
#     context = {
#         'title': 'Notices',
#         'page': 'notice',
#         'notices': Notice.objects.all()
#     }
#     return render(request, 'notice/notice_list.html', context)



class NoticeListView(ListView):
    template_name = 'notice/notice_list.html'
    model = Notice
    context_object_name = 'notices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notices | School Management System'
        context['page'] = 'notice'
        return context

