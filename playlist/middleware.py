from .models import RequestCount
from django.core.cache import cache

class RequestMiddleware:
    num_req = 0
    def __init__(self, get_response, *args, **kwargs):
        self.get_response = get_response

    def __call__(self,request, *args, **kwargs):
        self.num_req += 1
        print('Hello Middleware count is :', self.num_req)
        RequestCount.objects.filter(pk=1).update(count=self.num_req)
        response = self.get_response(request)
        return response



