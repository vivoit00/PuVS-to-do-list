# python manage.py runserver 8080 muss glaub rein oder so
FROM python:3.8-slim

    # Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Kopieren des gesamten Django-Projektcodes ins Arbeitsverzeichnis
COPY . /app

# Port freigeben, auf dem der Server läuft
EXPOSE 8000

# Befehl zum Starten des Django-Servers
CMD sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000" 
