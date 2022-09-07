from django.db import models
import uuid

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.username