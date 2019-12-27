#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'BY'
__mtime__ = '2019/12/4'
"""
from django.urls import path

from .views.goods_view import *
from .views.cart_view import *

urlpatterns = [
    path('goods', index, name='index'),
    path('products', QueryProducts.as_view(), name='query_products'),
    path('category', QueryCategory.as_view(), name='query_category'),
    path('category_goods', QueryCategoryProducts.as_view(), name='query_category_goods'),
    path('detail', GoodsDetailView.as_view(), name='good_detail'),
    path('cart', CartView.as_view(), name='cart'),

]
