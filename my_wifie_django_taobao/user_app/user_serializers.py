#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'BY'
__mtime__ = '2019/12/26'
"""
from rest_framework import serializers
from user_app.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["user_name", "password"]
