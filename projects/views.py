import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from selenium import webdriver
# Create your views here.
from django.views import View
from rest_framework.viewsets import ModelViewSet
from projects.serializer import ProjectsModelSerializer
from projects.models import Projects

class ProjiectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer

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
        # 创建数据
        # 方法一，创建模型类对象
        # one_obj=Projects(name='前程贷测试3',leader='孙翔宇',tester='sunxy',publish_app='sxy',programer='me',desc='一个小测试')
        # one_obj.save()
        # 方法二
        # Projects.objects.create(name='前程贷测试4',leader='孙翔宇',tester='sunxy',publish_app='sxy',programer='me',desc='一个小测试')
        # pass
        # 获取记录
        # Projects.objects.all()
        # 获取单条记录，如果存在多条记录或者查询记录不存在会报出异常
        # ob = Projects.objects.get(id=1)
        # print(ob.name, ob.tester)
        # 获取某一条记录，filter（）或者exclude()
        # startswich以给定字符串结尾的所有记录返回
        # endswich以给定字符串结尾的所有记录返回
        # 将
        # ob=Projects.objects.exclude(id=1)  # id不为1的全部获取到
        # Projects.objects.filter(id=1)  # id为1的全部获取到
        # Projects.objects.filter(name__startswich='1')
        # data=Projects.objects.filter(name__endswich='1')
        # 关联查询
        # Projects.objects.filter()
        # 1.从数据库中获取所有的项目信息
        project_qs = Projects.objects.all()
        # 2.将数据库模型实例转化成字典类型（嵌套字典的列表）
        project_list = []
        for project in project_qs:
            dic = {
                "name": project.name
            }
            project_list.append(dic)
        # JsonResponse第一个参数只能为字典，如果想设置为其他类型，加safe=False
        return JsonResponse(project_list, safe=False)

    def post(self, request):
        """
        如果穿body类型的数据，导入json模块,先转化为字符穿，在转化为json
        request.body.encode('utf-8')--> json.loads()
        :param request:
        :return:
        """
        data = {"name": "sunxiangyu"}
        json_data = request.body.decode('utf-8')
        py_data =json.loads(json_data)
        # return HttpResponse("<h1>hello,post</h1>")
        return JsonResponse(data=data)

    def put(self, request):
        return HttpResponse("<h1>hello,put</h1>")

    def delete(self, request):
        return render(request, 'demo.html')
