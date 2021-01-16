from rest_framework.serializers import ModelSerializer
from projects.models import Projects


class ProjectsModelSerializer():
    class Meta:
        model = Projects
        fields = '__all__'
