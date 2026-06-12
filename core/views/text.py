from rest_framework.viewsets import ModelViewSet

from core.models import Text
from core.serializers import TextDetailSerializer, TextSerializer


class TextViewSet(ModelViewSet):
    queryset = Text.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TextDetailSerializer
        return TextSerializer
