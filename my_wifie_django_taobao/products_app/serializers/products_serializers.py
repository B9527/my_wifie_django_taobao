#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'BY'
__mtime__ = '2019/12/4'
"""
from rest_framework import serializers
from products_app.models import Products, Category


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_id', 'product_img_url', 'product_name', 'product_price', 'product_uprice')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_pid', 'category_name')


class ProductsAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
