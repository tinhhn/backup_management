"""backup_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('backup/total/', views.total_backups, name='total_backups'),
    path('backup/success/', views.success_backups, name='success_backups'),
    path('backup/missing/', views.missing_backups, name='missing_backups'),
    path('backup/warning/', views.warning_backups, name='warning_backups'),
    path('backup-detail/<str:backup_name>', views.backup_detail, name='backup-detail'),
    path('backup/report/pdf', views.report_pdf, name='report_pdf'),
    path('backup/report/png', views.report_png, name='report_png'),
    path('backup/report/webpage', views.report_webpage, name='report_webpage'),
    path('generate_report/', views.generate_report, name='generate_report'),
]


