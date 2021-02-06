import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from rest_framework import status, filters
from rest_framework.renderers import JSONRenderer, HTMLFormRenderer
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Projects
from projects.serializer import ProjectSerrializers, ProjectModelSerializer
from utils.pageination import PageNumberPaginationManual


class ProjectDetial(GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    # renderer_classes = [JSONRenderer]
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    # 1必须指定查询级（queryset）
    queryset = Projects.objects.all()
    # 2指定序列化器（serializer_class）
    serializer_class = ProjectModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# 1需要继承GenericAPIView基类
class ProjectList(GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    # 1必须指定查询级（queryset）
    queryset = Projects.objects.all()
    # 2指定序列化器（serializer_class）
    serializer_class = ProjectModelSerializer

    # 3在视图类中制动过滤引擎
    # filter_backends = [filters.OrderingFilter]
    # # 4指定需要排列的字段
    # ordering_fields = ['name', 'tester']
    # # 在视图中指定过滤引擎
    # filter_backends = [DjangoFilterBackend]
    # # 5在视图中指定需要过滤的字段
    # filtersset = ['name']
    # # 在某个视图中指定分页类
    # pagination_class = PageNumberPaginationManual

    # def get_object(self, pk):
    #
    #     try:
    #         return Projects.objects.get(id=pk)
    #     except Projects.DoesNotExist:
    #         raise Http404
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, pk):

        project = self.get_object(pk)
        project.delete()
        return JsonResponse(None, safe=False, status=404)

    def put(self, request, pk):
        project = self.get_object(pk)
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
        # 创建序列化器是，如果同时给instance传参，那么调用sava方法，会自动调用序列化器中的update
        serializer.save()
        # project.name=serializer.validated_data["name"]
