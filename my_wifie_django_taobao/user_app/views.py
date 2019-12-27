from django.shortcuts import render
from rest_framework.views import APIView, Response
from user_app.models import UserModel

# Create your views here.
from user_app.user_serializers import UserSerializer


class UserRegViews(APIView):
    """
    用户注册
    """

    def post(self, request, format=None):
        return_data = {}
        try:
            data = request.data
            user_name = data.get("regName", None)
            password = data.get("regPasswd", None)
            if user_name is None:
                raise Exception("用户名丢失！")
            if password is None:
                raise Exception("密码丢失！")
            user_count = UserModel.objects.filter(user_name=user_name).count()
            if user_count > 0:
                raise Exception("用户名已存在！")
            user_model = UserModel(user_name=user_name, password=password)
            user_model.save()
            return_data = {
                "regName": user_name,
                "regPasswd": password,
                "status": 1
            }
        except Exception as e:
            return_data = {
                "error_msg": str(e),
                "status": -1
            }
        finally:
            return Response(return_data)


class UserLoginView(APIView):
    """
    用户登陆
    """

    def post(self, request, format=None):
        return_data = {}
        try:
            data = request.data
            user_name = data.get("loginName", None)
            password = data.get("loginPawd", None)
            if user_name is None:
                raise Exception("用户名丢失！")
            if password is None:
                raise Exception("密码丢失！")

            user_list = UserModel.objects.filter(user_name=user_name, password=password)
            if user_list.count() != 1:
                raise Exception("用户名或密码错误！")
            user = user_list[0]
            return_data = {
                "user_name": user.user_name,
                "user_id": user.id,
                "status": 1
            }
        except Exception as e:
            return_data = {
                "error_msg": str(e),
                "status": -1
            }
        finally:
            return Response(return_data)


class UserInfoView(APIView):
    """
    获取用户信息
    """

    def get(self, request, format=None):
        user_id = request.GET.get("uId")
        if user_id is None:
            raise Exception("uId 丢失")

        user_obj = UserModel.objects.get(id=user_id)

        user_info = UserSerializer(user_obj, many=False).data

        return Response(user_info)
