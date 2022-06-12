from django.middleware.csrf import CsrfViewMiddleware
from django.utils.deprecation import MiddlewareMixin

class CORSMiddele(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Methods'] = 'DELETE'
            response['Access-Control-Allow-Headers']='Content-Type'
        response['Access-Control-Allow-Origin'] = '*'
        return response