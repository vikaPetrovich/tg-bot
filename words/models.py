from django.db import models


class Words(models.Model):
    text = models.TextField(verbose_name="Quote", max_length=400)

    def __str__(self):
        return self.text
