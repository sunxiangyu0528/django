from django.contrib import admin
from projects.models import Projects
from interfaces.models import Interface

# Register your models here.


# admin.site.register(Projects)


# admin.site.register(Interface)


class ProjectAdmin(admin.ModelAdmin):
    """
    定制后天管理站点类
    """
    # 指定在修改（新增）中需要显示的字段
    fields = ('name', 'leader', 'tester', 'publish_app', 'programer', 'desc')
    # 指定要列出的字段
    list_display = ['id', 'name', 'leader', 'tester', 'publish_app', 'programer', 'desc']


admin.site.register(Projects, ProjectAdmin)
