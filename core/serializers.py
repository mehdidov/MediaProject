from rest_framework import serializers

# On importe les outils de Django REST Framework pour créer des serializers.
#Les serializers sont utiles pour transformer les données Python en JSON et c'est pareil dans l'autre sens


class PingSerializer(serializers.Serializer):
    # Ce serializer sert juste à renvoyer un message

    message = serializers.CharField()  # On dit que message est un texte.


class HealthCheckSerializer(serializers.Serializer):
    # Ce serializer sert pour l’endpoint /health et il regarde si l’API fonctionne

    status = serializers.CharField()  # On renvoie un texte 


class VersionSerializer(serializers.Serializer):
    # Ce serializer sert à renvoyer la version de notre API

    version = serializers.CharField()  




