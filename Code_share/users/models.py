from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class Custom_user(AbstractUser):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    username=models.CharField(max_length=20, null=False, unique=True )
    github=models.URLField(max_length=255, null=True, blank=True)
    email=models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username