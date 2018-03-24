# -*- coding: UTF-8 -*-
"""Five URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view.index, name = 'home'),
    url(r'^home/$', view.index, name = 'home'),
    url(r'^home2/$', view.index),
    url(r'^regist/$', view.regist, name = 'regist'),
    url(r'^login/$', view.login, name = 'login'),
    url(r'^info/$', view.checkinfo, name = 'info'),
    url(r'^showbook/$', view.ShowBook, name='ShowBook'),
    url(r'^showsubscribedbook/$', view.ShowSubscribedBook, name='ShowSubscribedBook'),
    url(r'^showfavoredbook/$', view.ShowFavoredBook, name='ShowFavoredBook'),
    url(r'^BookArrival/$', view.ShowArrivalMessage, name='ShowArrivalMessage'),
    url(r'^logout/$', view.logout, name='logout'),
    url(r'^abc/$', view.abc, name='abc'),
    url(r'^myfavor/$', view.myfavor),
    url(r'^searchclass/$', view.searchclass),
    url(r'^notify/$', view.notify),
    url(r'^registbooks/$', view.regiestbooks),
    url(r'^changeinfo/$', view.modifypersonalinfo),
    url(r'^logout/$', view.logout),
    url(r'^bookform/$', view.showbooklist),
    url(r'^modifysubscribe/$', view.modifysubscribe),
    url(r'^lbforum/', include('lbforum.urls')),
    url(r'^attachments/', include('lbattachment.urls')),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)