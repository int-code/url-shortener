from django.db import models

# Create your models here.
class url_Model(models.Model):
    long_url = models.URLField(max_length=300)
    short_url = models.CharField(max_length=5, unique=True, primary_key=True)