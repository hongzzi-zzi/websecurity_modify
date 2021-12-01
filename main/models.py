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

