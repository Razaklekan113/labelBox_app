from django.db import models
from cloudinary.models import CloudinaryField
import uuid

class AnnotationTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', folder='annotations')  # Use CloudinaryField instead of ImageField
    annotation = models.JSONField(null=True, blank=True)  # Store annotation data as JSON
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


