from rest_framework.views import exception_handler
from rest_framework.response import Response
from .logging import logger
def common_exception_handler(exc, context):
    res=exception_handler(exc, context)
    logger.error('系统错误:请求地址是：%s,请求的视图类是:%s,错误对象是: %s'  %(context['request'].path,str(context['view']),str(exc)))
    if res:
        return Response({'code':888, 'msg':res.data['detail']})
    else:
        return Response({'code':999, 'msg':'服务器异常，请联系管理员'})




























