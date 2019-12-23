#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'BY'
__mtime__ = '2019/12/4'
"""
from rest_framework import serializers

from myshop.settings import local_url_host
from products_app.models import Products, Category


class ProductsSerializer(serializers.ModelSerializer):
    product_img_url = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ('product_id', 'product_img_url', 'product_name', 'product_price', 'product_uprice')

    @staticmethod
    def get_product_img_url(obj):
        return local_url_host + obj.product_img_url.name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_pid', 'category_name')


class ProductsAllSerializer(serializers.ModelSerializer):
    product_img_url = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = "__all__"

    @staticmethod
    def get_product_img_url(obj):
        return local_url_host + obj.product_img_url.name
