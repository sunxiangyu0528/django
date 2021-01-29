from django.contrib import admin
from django.urls import path, include
# from projects.views import index
from projects import views
from rest_framework.routers import DefaultRouter

# 全局路由配置
# 1 urlpatterns为固定名称的列表
# 2列表中的一个元素，代表一个路由
# 3.从上到下匹配，如果能匹配上，django会导入和调用path函数第二个参数指定的视图
# 4.如果匹配不上，会出现一个404异常


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('home/', index)
    path('projects/<int:pk>/', views.ProjectDetial.as_view()),
    path('projects/', views.ProjectList.as_view()),

]
# int 为路径参数转换器
# 左边是转换器，右边是参数别名，要把别名当做参数放到视图后面
