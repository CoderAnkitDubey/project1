from django.db import models

# from autoslug import AoutoSlugField

# Create your models here
class service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=models.TextField()
    