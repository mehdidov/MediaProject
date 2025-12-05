from django.db import models
import uuid 

class Media(models.Model):

    # ID unique généré automatiquement 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Nom du fichier
    filename = models.CharField(max_length=255)

    # ID qui est retourné par ImageKit après l’upload
    file_id = models.CharField(max_length=255, null=True, blank=True)

    # L’URL du fichier qui est hébergé sur ImageKit
    url = models.TextField(null=True, blank=True)

    # Type du fichier 
    mime_type = models.CharField(max_length=100, null=True, blank=True)

    # Taille du fichier en octets
    size_bytes = models.BigIntegerField(null=True, blank=True)

    # Date de création automatique dans la base
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        # Nom de la table dans la BDD
        db_table = "media_job"

    def __str__(self):

        # Ce qui s’affiche quand Django montre l’objet
        return f"Media file : {self.filename}"
