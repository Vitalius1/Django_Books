from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)
    published_date = models.CharField(max_length = 30)
    category = models.CharField(max_length = 30)
    in_print = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
# Create your models here.
