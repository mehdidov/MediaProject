from django.db import models
import uuid 

class Media(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   filename = models.CharField(max_length=255)
   file_id = models.CharField(max_length=255, null=True, blank=True)
   url = models.TextField(null=True, blank=True)
   mime_type = models.CharField(max_length=100, null=True, blank=True)
   size_bytes = models.BigIntegerField(null=True, blank=True)

   created_at = models.DateTimeField(auto_now_add=True)
   
  
class Meta:
    db_table = "media_job"
        
    def __str__(self):
        return f"{self.id} - {self.original_filename}"