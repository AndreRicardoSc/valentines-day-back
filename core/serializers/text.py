from rest_framework import serializers

from core.models import Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'title', 'date', 'paragraphs']


class TextDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'title', 'date', 'paragraphs']
        depth = 1
