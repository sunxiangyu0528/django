from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View


# def index(request):
#     """
#
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         return HttpResponse("<h1>hello,GET</h1>")
#     else:
#         return HttpResponse("<h1>hello,post</h1>")


class IndexView(View):
    """
    主页类视图
    """

    def get(self, request):
        return HttpResponse("<h1>hello,GET</h1>")

    def post(self, request):
        return HttpResponse("<h1>hello,post</h1>")

    def put(self, request):
        return HttpResponse("<h1>hello,put</h1>")

    def delete(self, request):
        return render(request,'demo.html')