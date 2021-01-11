from django.db import models


# Create your models here.
# 1.每一个应用下的数据库模型类，需要在当前应用下的mmodels.py文件中定义
# 2.一个数据库模型类相当于一个数据表
# 3.定义一个类属性，相当于数据库表中的一个字段
# 4.默认会创建一个自动递增的id主键
# 5.默认创建的数据库名，应用名小写_数据库模型类小写
# 6 .max_length字段的最大长度，verbose_name用于设置跟人性化的字段名，
# unique用于甚至当前字段是否唯一.help_text用于api文档
# null设置数据库中此字段允许为空 ，black用于设置前端用户可不传
# class Person(models.Model):
#     """ 创建person类"""
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#
#     class Meta:
#         db_table = 'tb_projects'
#         verbose_name = "人类"
#         verbose_name_plural = '人类'


class Projects(models.Model):
    name = models.CharField(verbose_name="项目名称", max_length=200, help_text="项目名称", unique=True)
    leader = models.CharField(verbose_name="负责人", max_length=200, help_text="负责人")
    tester = models.CharField(verbose_name="测试人员", max_length=200, help_text="测试人员")
    publish_app = models.CharField(verbose_name="发布应用", max_length=200, help_text="发布应用")
    programer = models.CharField(verbose_name="开发人员", max_length=200, help_text="开发人员")
    desc = models.TextField(verbose_name="简要描述", help_text="简要描述", blank=True, default='', null=True)

    # models.IntegerField(choices=[])

    class Meta:
        db_table = 'tb_projects'
        verbose_name = "项目计划"
        verbose_name_plural = '项目计划'
