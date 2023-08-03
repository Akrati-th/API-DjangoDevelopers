from rest_framework.serializers import ModelSerializer
from .models import Developer


class ViewDeveloperSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["developer_type"] = instance.developer_type.name
        data["skills"] = instance.developer_type.developer_skill
        return data

    class Meta:
        model = Developer
        exclude = "developer_type"


class CreateDeveloperSerializer(ModelSerializer):
    class Meta:
        models = Developer
        fields = '__all__'
