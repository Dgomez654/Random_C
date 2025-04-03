import os
import requests
import datetime
import subprocess

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_OWNER = 'Dgomez654'  # Reemplaza con tu usuario de GitHub
REPO_NAME = 'Random_C'
EXECUTABLE_PATH = 'main.exe'  # Ruta al ejecutable generado por Jenkins

# Generar etiqueta basada en la hora
now = datetime.datetime.now()
release_tag = f'v{now.year}.{now.month}.{now.day}-{now.hour}.{now.minute}.{now.second}'

# Crear la versión en GitHub
release_url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases'
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}
release_data = {
    'tag_name': release_tag,
    'name': release_tag,
    'body': 'Versión automática generada por Jenkins',
    'draft': False,
    'prerelease': False
}
response = requests.post(release_url, headers=headers, json=release_data)
response.raise_for_status()
release_id = response.json()['id']

# Subir el ejecutable a la versión
upload_url = f'https://uploads.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/{release_id}/assets?name=main.exe'
with open(EXECUTABLE_PATH, 'rb') as file:
    upload_response = requests.post(upload_url, headers=headers, data=file)
    upload_response.raise_for_status()

print(f'Versión {release_tag} creada y ejecutable subido con éxito.')
