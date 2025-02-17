#on utilise python 3.9
FROM python:3.9

#on difinit le dossier de travail dans le conteneur (l'api se situe dans app)
WORKDIR /app 
#on copie requirements pour installer les bibliotheques juste apres
COPY requirements.txt .
#installation flask;
RUN pip install --no-cache-dir -r requirements.txt 

#on copie tout dans le conteneur
COPY app/ . 

#on execute l'app
CMD ["python", "app.py"]
