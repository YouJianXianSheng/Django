#！/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:zhangcs
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.Index),
]