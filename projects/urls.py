from django.contrib import admin
from django.urls import path, include
# from projects.views import index
from projects import views
# 全局路由配置
# 1 urlpatterns为固定名称的列表
# 2列表中的一个元素，代表一个路由
# 3.从上到下匹配，如果能匹配上，django会导入和调用path函数第二个参数指定的视图
# 4.如果匹配不上，会出现一个404异常
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', index)
    path('',views.IndexView.as_view())
]
