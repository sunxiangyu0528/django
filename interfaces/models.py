from django.db import models


# Create your models here.
# 一个项目中有多个接口，那么需要在“多”的一侧创建外检，项目表为父表
class Interface(models.Model):
    name = models.CharField(verbose_name="接口名称", max_length=200, help_text="项目名称", unique=True)
    tester = models.CharField(verbose_name="测试人员", max_length=200, help_text="测试人员")
    desc = models.TextField(verbose_name="简要描述", help_text="简要描述", blank=True, default='', null=True)
    # 第一个参数为关联的模型路径（应用名。模型类）喝着模型类
    # 第二个参数设置的事，当父表删除之后，改字段的处理方式
    # CASCADE-->字表也会删除
    # SET_NULL-->当前外检会被设置None
    # PROJECR--> 会报错
    # SET_DEFAULT -->设置默认值，同时需要指定默认值，null=True
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, verbose_name="所属项目", help_text='所属项目')

    class Meta:
        db_table = 'tb_interfaces'
        verbose_name = "接口"
        verbose_name_plural = '接口'


    def __str__(self):
        return self.name