from django.shortcuts import render
from django.views import View

from members.models import Member
from django.views.generic import ListView

# Create your views here.


# views.py
# def member_list(request):
#     context = {
#         'title': 'Members List',
#         'page': 'members'
#     }
#     return render(request, 'members/member_list.html', context)

class MemberListView(ListView):
    template_name = 'members/member_list.html'
    model = Member
    context_object_name = 'members' 

    # def get_queryset(self):
    #     # queryset = Member.objects.filter(member_type = 'faculty')
    #     queryset = Member.objects.all()

    #     member_type = self.request.GET.get('type')
    #     department = self.request.GET.get('department')
    #     if member_type:
    #         queryset = queryset.filter (member_type = member_type)

    #     return queryset

    def get_queryset(self):
        queryset = Member.objects.all()

        member_type = self.request.GET.get('type')     
        if member_type and member_type != 'all':
            queryset = queryset.filter(member_type__iexact=member_type)



        department = self.request.GET.get('department')
        if department and department != 'all':
            queryset = queryset.filter(department__iexact=department)

        return queryset