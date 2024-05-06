# Verwende ein Basisimage mit Python
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis innerhalb des Containers
WORKDIR /PuVS-to-do-list/samle/otel-in-action/todobackend_django

# Kopiere die requirements.txt-Datei in das Arbeitsverzeichnis
COPY dependencies.txt .

# Installiere die Python-Abhängigkeiten
RUN pip install --no-cache-dir -r dependencies.txt

# Kopiere den Rest des Anwendungsquellcodes in das Arbeitsverzeichnis
COPY . .

# Führe den Django-Server aus, wenn der Container gestartet wird
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
