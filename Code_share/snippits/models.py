import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class snippit_share(models.Model):
    code_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code_file=models.TextField()
    description=models.CharField(blank=True, max_length=255)
    language=models.CharField(max_length=10, blank=False, null=False)
    create_at=models.DateField(auto_now=True)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_snippits", on_delete=models.CASCADE)

    def __str__(self):
        return self.title