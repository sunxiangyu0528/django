from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Projects


# 自定义校验器
# 自定义校验器优于类内部校验器
def is_unique_project_name(name):
    if "项目" not in name:
        raise serializers.ValidationError("项目必须包含项目")


class ProjectSerrializers(serializers.Serializer):
    """
     创建项目序列化器
    """
    # label选项相当于verbose_name
    # read_only=True,指定该字段只能进行序列化输出
    # ,write_only=True指定该字段只能进行反序列化输入
    id = serializers.IntegerField(label='ID', read_only=True)
    # validators里面从头往后开始校验
    name = serializers.CharField(label='项目名称', max_length=200,
                                 help_text='项目名称', write_only=True,
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目名称不能重复"),
                                             is_unique_project_name]

                                 )
    tester = serializers.CharField(label='测试人员', max_length=200, help_text='测试人员')

    # publish_app = serializers.CharField(label='发布人员',max_length=200,help_text='发布人员')
    # programer = serializers.CharField(label='开发人员',max_length=200,help_text='开发人员')
    # desc = serializers.CharField(label='简要描述',allow_null=True,allow_blank=True)

    # 单字段校验
    def validate_name(self, value):
        if not value.endswith("项目"):
            raise serializers.ValidationError("项目名称必须以项目结束")
        # 当校验成功后，要把value值返回
        return value

    # 多字段校验

    def validate(self, attrs):
        if 'icon' not in attrs["name"] and 'icon' not in attrs["tester"]:
            raise serializers.ValidationError("icon必须出现")
        return attrs

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)
        pass

    def update(self, instance, validated_data):
        pass
