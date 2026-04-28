import pandas as pd
import numpy as np
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_raw = os.path.normpath(os.path.join(BASE_DIR, "..", "..", "data", "raw", "game.csv"))
path_processed = os.path.normpath(os.path.join(BASE_DIR, "..", "..", "data", "processed", "game_processed.csv"))


# 1. Extracción (Extract)
cols = ["game_date", "fg3a_away", "fg3m_away", "fg3a_home", "fg3m_home",
        "fga_home", "fgm_home", "fga_away", "fgm_away",
        "pts_home", "pts_away", "season_type"]

df = pd.read_csv(path_raw, usecols=cols)

# 2. Transformación (Transform)
# Convertir a numérico de forma masiva (más limpio)
numeric_cols = df.columns.drop(['game_date', 'season_type'])
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

# Filtrado de temporada (asegúrate de que el CSV tenga estos nombres exactos)
df = df[df['season_type'].isin(['Regular Season', 'Playoffs'])]

# Cálculos
df['total_puntos'] = df['pts_home'] + df['pts_away']
df['game_date'] = pd.to_datetime(df['game_date'])
df['ganador'] = np.where(df['pts_away'] > df['pts_home'], 'away', 'home')

# Agregados totales
df['fg3m'] = df['fg3m_away'] + df['fg3m_home'].astype(float)
df['fg3a'] = df['fg3a_away'] + df['fg3a_home'].astype(float)
df['fga'] = df['fga_away'] + df['fga_home'].astype(float)
df['fgm'] = df['fgm_away'] + df['fgm_home'].astype(float)

# Porcentajes (manejando división por cero con np.where)
df['fg3pc'] = np.where(df['fg3a'] > 0, df['fg3m'] / df['fg3a'], 0)
df['fgpc'] = np.where(df['fga'] > 0, df['fgm'] / df['fga'], 0)
df['fg3pc_away'] = np.where(df['fg3a_home'] > 0, df['fg3m_home'] / df['fg3a_home'], 0)
df['fg3pc_home'] = np.where(df['fg3a_away'] > 0, df['fg3m_away'] / df['fg3a_away'], 0)
df['3p%_ganador'] = np.where(df['pts_away'] > df['pts_home'], df['fg3pc_away'], df['fg3pc_home'])
df['3p%_perdedor'] = np.where(df['pts_away'] > df['pts_home'], df['fg3pc_home'], df['fg3pc_away'])

# Tiros de 2
df['fg2a'] = df['fga'] - df['fg3a'].astype(float)
df['fg2m'] = df['fgm'] - df['fg3m'].astype(float)
df['fg2pc'] = np.where(df['fg2a'] > 0, df['fg2m'] / df['fg2a'], 0)

# Año y limpieza
df.insert(0, 'game_year', df['game_date'].dt.year)
df = df.drop('game_date', axis=1)
df = df.dropna(subset=['fg3pc', 'fg3a', 'fg3m'])

# Eliminar inconsistencias
df = df[df['fg3m'] <= df['fg3a']]

# Ordenar
df = df.sort_values('fg3pc', ascending=False)

# 4. Carga (Load)
# Crear carpeta si no existe
os.makedirs(os.path.dirname(path_processed), exist_ok=True)
df.to_csv(path_processed, index=False)

print(f"ETL finalizado con éxito. Archivo guardado en: {path_processed}")