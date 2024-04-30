from uuid import uuid4
from django.db import models

# Create your models here.
class CommonField(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.QuerySet.as_manager() 
    
    class Meta:
        abstract = True