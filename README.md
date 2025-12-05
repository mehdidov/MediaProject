📁 MEDIA PROJECT — Upload & Gestion de fichiers avec Django, Docker & Micro-services
🎯 But du projet

Le but du projet est de construire une API Django capable de :

✔️ recevoir un fichier (image, pdf, etc.) via une requête HTTP
✔️ envoyer ce fichier à ImageKit (hébergement externe)
✔️ enregistrer dans PostgreSQL les informations associées au fichier : nom, type, taille, URL cloud…
✔️ préparer la suite du pipeline :

enregistrer des métadonnées dans MongoDB

stocker un titre ou tag dans Redis

L’application est totalement exécutée grâce à Docker, dans une architecture proche d’un micro-service.

🧱 Architecture du projet

Le projet utilise plusieurs services indépendants, chacun dans son conteneur Docker :

🎛 Django (API principale)

Reçoit le fichier

Appelle ImageKit

Stocke les données dans PostgreSQL

Expose des endpoints : /ping/, /healthcheck/, /upload/, /swagger/…

🐘 PostgreSQL

Stocke les données du fichier dans une table : media_job.

🍃 MongoDB

Servira plus tard à stocker des métadonnées techniques (ex : EXIF d’une image).

🔥 Redis

Permettra de stocker un champ très rapide d’accès (par ex : un titre de fichier).

☁️ ImageKit

Reçoit réellement le fichier et renvoie une URL d’accès publique.

L’ensemble est orchestré via docker-compose.

🗂 Structure du projet
media_project/
│
├── config/                 # Configuration Django
│   ├── settings.py         # DB, apps installées, ImageKit keys
│   ├── urls.py             # URLs globales du projet
│
├── core/                   # App principale
│   ├── models.py           # Modèle Media (table PostgreSQL)
│   ├── views.py            # Vues : Ping, HealthCheck, Upload
│   ├── urls.py             # Routes de l'app
│   ├── serializers.py      # Format de réponse API
│
├── media/                  
│   ├── imagekit.py         # Fonction d’envoi du fichier à ImageKit
│
├── docker_ressources/
│   ├── init.sql            # Script d'initialisation PostgreSQL
│
├── Dockerfile              # Build de l'image Django
├── docker-compose.yml      # Définition des services
├── .env                    # Variables secrètes

🧬 Comment fonctionne l’API ?
🔹 1. L’utilisateur envoie un fichier

Endpoint :

POST /upload/


Le fichier est envoyé en multipart/form-data.

🔹 2. Django reçoit le fichier

Il est récupéré via :

incoming_file = request.FILES.get("file")

🔹 3. Django envoie le fichier à ImageKit

Appel REST dans media/imagekit.py :

response = requests.post(IMAGEKIT_API_URL, files=..., headers=...)

🔹 4. ImageKit renvoie un JSON

Exemple :

{
  "fileId": "...",
  "url": "https://ik.imagekit.io/.../image.png",
  "size": 18372,
  "mime": "image/png"
}

🔹 5. Django enregistre ces infos dans PostgreSQL

Le modèle utilisé est :

class Media(models.Model):
    id = UUID (clé primaire)
    filename = string
    file_id = string
    url = text
    mime_type = string
    size_bytes = int
    created_at = date


La table créée s’appelle media_job.

🐳 Lancement du projet
1️⃣ Construire & lancer tous les services
docker compose up -d --build

2️⃣ Appliquer les migrations (création de la table media)
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate

3️⃣ Accéder à PostgreSQL
docker compose exec db psql -U media -d media

🌐 Endpoints disponibles
Méthode	URL	Description
GET	/ping/	Test simple
GET	/healthcheck/	Vérifie que l’API fonctionne
POST	/upload/	Upload d’un fichier
GET	/schema/	Export OpenAPI
GET	/swagger/	Swagger UI
GET	/redoc/	Documentation ReDoc

Swagger permet de tester l’API directement dans le navigateur.

🧠 Architecture micro-services (expliquée simplement)

Une architecture micro-services consiste à séparer une application en plusieurs services indépendants, chacun ayant son rôle :

PostgreSQL = BDD principale

MongoDB = stockage de métadonnées

Redis = cache rapide

Django = logique métier

ImageKit = stockage de fichiers

Ces services peuvent tourner séparément, être redémarrés indépendamment et peuvent évoluer sans casser le reste.

Docker rend cela possible facilement.

📌 Pourquoi Docker est essentiel ?

✔️ Même environnement pour tout le monde
✔️ Lancement d’un seul fichier (docker-compose.yml)
✔️ Conteneurs isolés
✔️ PostgreSQL, MongoDB et Redis fonctionnent sans installation locale