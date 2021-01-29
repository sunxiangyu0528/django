from rest_framework import serializers


class ProjectSerrializers(serializers.Serializer):
    """
     创建项目序列化器
    """
    # label选项相当于verbose_name
    # read_only=True,指定该字段只能进行序列化输出
    #,write_only=True指定该字段只能进行反序列化输入
    id = serializers.IntegerField(label='ID',read_only=True)
    name = serializers.CharField(label='项目名称',max_length=200,help_text='项目名称',write_only=True)
    tester = serializers.CharField(label='测试人员',max_length=200,help_text='测试人员')
    # publish_app = serializers.CharField(label='发布人员',max_length=200,help_text='发布人员')
    # programer = serializers.CharField(label='开发人员',max_length=200,help_text='开发人员')
    # desc = serializers.CharField(label='简要描述',allow_null=True,allow_blank=True)
