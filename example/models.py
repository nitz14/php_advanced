from datetime import datetime
from django.db import models


class GiftList(models.Model):
    name = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
