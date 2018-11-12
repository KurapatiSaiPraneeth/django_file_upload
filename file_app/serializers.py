from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):

    language=serializers.ListField()
    genre = serializers.ListField()
    actor = serializers.ListField()
    class Meta():
        model = File
        fields = '__all__'