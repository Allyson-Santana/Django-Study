from django.db import models

class Files(models.Model):
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to='images')

    def __str__(self) -> str:
        return self.title