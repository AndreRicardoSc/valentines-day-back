from django.db import models

from .text import Text


class Paragraph(models.Model):
    value = models.TextField()
    text = models.ForeignKey(
        Text, on_delete=models.PROTECT, related_name='paragraphs'
    )

    def __str__(self):
        return f'({self.id}) - {self.text.title}'
