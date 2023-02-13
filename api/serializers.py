from rest_framework.serializers import ModelSerializer
from .models import Developer


class DevSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'
