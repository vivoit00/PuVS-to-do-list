# python manage.py runserver 8080 muss glaub rein oder so
FROM python:3.8-slim

# # Arbeitsverzeichnis im Container festlegen
# WORKDIR /app
# 
# # Abhängigkeiten installieren
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# 
# # Kopieren des Django-Projektcodes
# COPY . /app

EXPOSE 8000

# Start Django Server 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]