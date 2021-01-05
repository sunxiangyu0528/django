"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from projects.views import

# 全局路由配置
# 1 urlpatterns为固定名称的列表
# 2列表中的一个元素，代表一个路由
# 3.从上到下匹配，如果能匹配上，django会
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', index),
    path('projects/', include('projects.urls'))
]
