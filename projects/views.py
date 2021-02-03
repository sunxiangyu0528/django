import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from projects.models import Projects
from projects.serializer import ProjectSerrializers


class ProjectDetial(View):
    def get_object(self, pk):

        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # 1.校验前端传的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
        projects = self.get_object(pk)
        # 将模型类转化为字典
        serializer = ProjectSerrializers(instance=projects)

        return JsonResponse(serializer.data)


class ProjectList(View):
    def get_object(self, pk):

        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request):
        # 如果返回的是列表数据，那么需要添加many =true这个参数
        projects = Projects.objects.all()
        serializer = ProjectSerrializers(instance=projects, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        # 数据库新增数据
        json_data = request.body.decode("utf-8")
        python_data = json.loads(json_data, encoding="utf-8")
        serializer = ProjectSerrializers(data=python_data)
        # 1校验前端输入的数据
        # 调用序列化器对象的is_valid方法，开始校验前端参数
        # 如果校验成功，则返回true，校验失败，返回false
        # raise_exception=True,那么较远失败之后，会抛出异常
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        # serializer.validated_data
        # 校验成功之后的数据，可以使用validated_data熟悉来获取
        project = Projects.objects.create(**python_data)

        serializer = ProjectSerrializers(project)
        return JsonResponse(serializer.data, status=201)

        # # 2向数据库新增数据
        projects = Projects.objects.create(data=python_data)
        serializer_add = ProjectSerrializers(instance=projects)
        return JsonResponse(serializer_add.data, status=201)

    def delete(self, request, pk):

        project = self.get_object(pk)
        project.delete()
        return JsonResponse(None, safe=False, status=404)

    def put(self, request, pk):
        project=self.get_object(pk)
        json_data = request.body.decode("utf-8")
        python_data = json.loads(json_data, encoding="utf-8")
        serializer = ProjectSerrializers(data=python_data)
        # 更新项目
        serializer.is_valid()
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        # serializer.validated_data
        #创建序列化器是，如果同时给instance传参，那么调用sava方法，会自动调用序列化器中的update
        serializer.save()
        # project.name=serializer.validated_data["name"]