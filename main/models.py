from django.db import models

# Create your models here.
class Explanation(models.Model):
    def __str__(self):
        return self.name
class MLModel(models.Model):
    def __str__(self):
        return self.name

class MLResult(models.Model):
    def __str__(self):
        return self.name


class PDFdocuments(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)