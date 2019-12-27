#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'BY'
__mtime__ = '2019/12/4'
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('reg', UserRegViews.as_view(), name='reg'),
    path('login', UserLoginView.as_view(), name="login"),
    path('userinfo', UserInfoView.as_view(), name="userinfo")

]
