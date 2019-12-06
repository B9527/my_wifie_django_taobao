#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'BY'
__mtime__ = '2019/12/4'
"""
from django.urls import path

from .views import goods_view

urlpatterns = [
    path('goods', goods_view.index, name='index'),
    path('', goods_view.QueryProducts.as_view(), name='query_products'),
    path('category', goods_view.QueryCategory.as_view(), name='query_category'),
    path('category_goods', goods_view.QueryCategoryProducts.as_view(), name='query_category_goods'),
]
