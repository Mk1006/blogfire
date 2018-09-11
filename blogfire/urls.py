"""brandstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from blogger import views as core_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^blogfire.org/$', core_views.index, name='index'),

    url(r'^$', core_views.home, name='home'),
    url(r'^blogger/$', core_views.bloggerprofile, name='blogger'),
    url(r'^blogger/edit/', core_views.edit_bloggerprofile, name='edit_bloggerprofile'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
    url(r'^register/$', core_views.register, name='register'),
    url(r'^bloggerpicsave/', core_views.profile_picUploadSave, name='bloggerpicsave'),
]

    
    
