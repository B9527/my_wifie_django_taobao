#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'BY'
__mtime__ = '2019/12/4'
"""
from django.http import HttpResponse
from django.http import JsonResponse

from myshop.settings import local_url_host
from products_app.models import Products, Category, ProductsImage
from django.views import View
from products_app.serializers.products_serializers import ProductsSerializer, CategorySerializer, ProductsAllSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QueryProducts(View):
    def get(self, request):
        products_store_on = Products.objects.filter(is_on=1, is_store=1)
        products_list_on = Products.objects.filter(is_on=1)
        store_serializer = ProductsSerializer(products_store_on, many=True)
        no_store_serializer = ProductsSerializer(products_list_on, many=True)
        return_data = {"main_data": no_store_serializer.data, "home_data": store_serializer.data}
        return JsonResponse(return_data)


class QueryCategoryProducts(View):
    def get(self, request):
        category_id = request.GET.get("mId", None)
        product_name = request.GET.get("name", None)

        products_all = Products.objects.filter(is_on=1)
        if category_id is not None:
            products_all = products_all.filter(category_id=category_id)

        if product_name is not None:
            products_all = products_all.filter(product_name__icontains=product_name)

        products_all_serializer = ProductsSerializer(products_all, many=True)
        return_data = {"cate_goods_data": products_all_serializer.data, "mid": category_id}
        return JsonResponse(return_data)


class QueryCategory(View):
    def get(self, request):
        category_id = request.GET.get("mid")
        category = Category.objects.all()
        category_serializer = CategorySerializer(category, many=True)
        return_data = {"left_data": category_serializer.data, "mid": category_id}
        return JsonResponse(return_data)


class GoodsDetailView(View):
    def get(self, request):
        p_id = request.GET.get("p_id")
        image_url_list = []
        products_one = Products.objects.get(product_id=p_id)
        p_serializer = ProductsAllSerializer(products_one, many=False)
        goods_data = p_serializer.data

        products_image_list = ProductsImage.objects.filter(product_id=p_id)
        for products_image_obj in products_image_list:
            image_url_list.append(local_url_host+products_image_obj.image_url.name)

        if len(image_url_list) == 0:
            image_url_list.append(products_one.product_img_url)
        return_data = {"goods_data": goods_data, "p_id": p_id,
                       'image_url_list': image_url_list}
        return JsonResponse(return_data)
