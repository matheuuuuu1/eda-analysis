import wget
import zipfile as zf
import os

# Configuración
url = 'https://storage.googleapis.com/kaggle-data-sets/1218020/6090760/compressed/csv/game.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260428%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260428T101307Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=47bd24641b5495b3f4264b63311b100184fed06ace8eb9a5d71eb73dfa774a81eabfb623184652bd50c146b70ec871b4cff163bf49c22694769e8ce953d04f425c1ccd7281f65b503f546337c578a953456a230d840d66ac118a2b07c56558d1175831e5a7df18f41b2ec149d6e8d62951cf5ecc1675d03f095ba646dd668eed19284551c2e168c299c8587acb49064e9cf85660d0cdf1d8841ea430e8082b3b7e591533c29ddc136204e7d6112f31c59dd644f9ee9dbb2892131062642c4e8389d2f560bdad04bd059dbc49096b8e116fd49951dae28d46f3ab7b29d65d6d7a2a312e8556d19c15d6a49558d098971a6dbb27010e3430e378d1705a48cde228'
zip_path = 'data/game.csv.zip'
dest_dir = 'data/'

print('Descargando...')
wget.download(url, zip_path)

print('\nExtrayendo...')
with zf.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(dest_dir)

print('Limpiando...')
if os.path.exists(zip_path):
    os.remove(zip_path)

print('Listo: Datos extraídos y temporal eliminado.')
