import logging

from django.shortcuts import render, HttpResponse

# Create your views here.
from utils.logging import logger
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from utils.response import APIResponse
from rest_framework.views import View


def test(request):
    print(request.method)
    logger.error('报错啦')
    res = HttpResponse('ok')
    #
    # if request.method == 'OPTIONS':
    #     res['Access-Control-Allow-Methods']='DELETE'
    #     # res['Access-Control-Allow-Headers']='Content-Type'
    # res['Access-Control-Allow-Origin'] = '*'
    return res

class TestView(APIView):
    def get(self, request):
        print('我执行了')
        # raise Exception('我出错了')
        # raise APIException('我出错了')
        # return Response('okok')
        # return APIResponse(token='xxx')


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .models import Banner
from .serializer import BannerSerializer
from django.conf import settings

class BannerView(GenericViewSet, ListModelMixin):
    queryset = Banner.objects.all().filter(is_delete=False, is_show=True)[:settings.BANNER_COUNT]
    serializer_class = BannerSerializer
