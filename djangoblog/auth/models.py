from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserMeta(models.Model):
    user = models.ForeignKey(User)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()
