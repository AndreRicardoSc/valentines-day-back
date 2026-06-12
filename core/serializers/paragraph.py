from rest_framework import serializers

from core.models import Paragraph


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'value', 'text']
