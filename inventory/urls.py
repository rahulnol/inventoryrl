from django.contrib import admin
from django.urls import path
from MyNetApp import views
from django.views.generic import TemplateView
from django.conf.urls import include,re_path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupView.as_view(),name = 'show_signup_page'),
    path('login/',TemplateView.as_view(template_name='pages/login.html')),
    path('dashboard/',TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('hardware/',TemplateView.as_view(template_name='hardware.html'),name='hardware'),
    path('software/',TemplateView.as_view(template_name='software.html'),name='software'),
    path('location/',TemplateView.as_view(template_name='location.html'),name='location'),
    path('report/',TemplateView.as_view(template_name='report.html')),
    path('members/',TemplateView.as_view(template_name='members.html'),name='member'),
    path('addhardware/',TemplateView.as_view(template_name='add_hardware.html')),
    path('addsoftware/',TemplateView.as_view(template_name='add_software.html')),
    path('addLocation/',TemplateView.as_view(template_name='add_location.html')),
    path('addmember/',TemplateView.as_view(template_name='add_member.html')),
    path('assignHardware/',TemplateView.as_view(template_name='assign_hardware.html')),
    path('detailHardware/',TemplateView.as_view(template_name='detail_hardware.html')),
    path('accounts/',include('django.contrib.auth.urls')),
    #path('validatelogin/',views.ValidateLogin.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)