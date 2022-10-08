from django.db import models

class Password(models.Model):
    senha = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

    def __str__(self):
        return self.url
