from rest_framework.viewsets import ModelViewSet

from core.models import Paragraph
from core.serializers import ParagraphSerializer


class ParagraphViewSet(ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
