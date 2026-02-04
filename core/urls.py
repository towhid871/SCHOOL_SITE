from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from .views import(
    HomePageView,
    AboutPageView,
    ContactPageView,
    AdmissionPageView,
    
)


urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('admission/', AdmissionPageView.as_view(), name='admission'),

    path('members/', include('members.urls')),
    path('routine/', include('routine.urls')),
    path('notice/', include('notice.urls')),

]

    # path('', admin.site.urls),  # Redirect root URL to admin)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


