from django.db import models


class Text(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'({self.id}) - {self.title}'
