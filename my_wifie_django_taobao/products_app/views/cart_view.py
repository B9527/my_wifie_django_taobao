#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'BY'
__mtime__ = '2019/12/27'
"""
from rest_framework.views import APIView
from rest_framework.response import Response


class CartView(APIView):
    """
    购物车
    """

    def get(self, request, format=None):
        return_data = [{
            "cart_id": 1,
            "user_id": 1,
            "product_id": 1,
            "product_name": "面膜",
            "product_uprice": 100,
            "product_img_url": "http://127.0.0.1:8000/api_shop/img/shop_image/041.jpg",
            "goods_num": 2,
            "product_num": 2,
            "shop_name": 2

        }]
        return Response(return_data)
