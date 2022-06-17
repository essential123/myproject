from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from .models import User
from utils.response import APIResponse
from rest_framework.exceptions import APIException

def home(request):
    return render(request,'home.html')


class UserView(ViewSet):

    # /user/check_mobile---->post请求
    @action(methods=['POST'], detail=False, )
    def check_mobile(self, request):
        mobile = request.data.get('mobile')
        # res=User.objects.filter(mobile=mobile).first()
        try:
            User.objects.get(mobile=mobile)

        except Exception as e:
            # return APIResponse(is_exist=False)
            raise APIException('该手机号不存在')

        return APIResponse(is_exist=True)