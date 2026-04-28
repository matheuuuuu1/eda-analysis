# 🏀 NBA EDA — Análisis de la Evolución del Juego (1946–2024)

> Análisis exploratorio de datos sobre el impacto de la línea de tres puntos en el baloncesto de la NBA, desde sus inicios en 1946 hasta la temporada 2023–24.

---

## 📌 Descripción

Este proyecto analiza **cómo ha cambiado el juego de la NBA a lo largo de casi 80 años**, con foco en el impacto que tuvo la introducción del tiro de tres puntos (1979–80) sobre la anotación, la selección de tiro y la efectividad de los equipos ganadores vs. perdedores.

Las preguntas clave que guían el análisis son:

- ¿Cómo evolucionó el promedio de puntos anotados por partido desde 1946?
- ¿Los equipos que ganan tiran mejor de tres que los que pierden?
- ¿En qué medida el triple ha desplazado al tiro de dos puntos?
- ¿Cuánto ha crecido el volumen de triples intentados y realizados?

El resultado final se presenta como un **dashboard HTML estático** con todas las visualizaciones generadas.

---

## 📊 Visualizaciones

El proyecto genera cuatro gráficos principales, exportados en alta resolución (`300 dpi`):

| Gráfico | Descripción |
|---|---|
| `ptp_prom.jpeg` | Evolución del promedio de puntos combinados por partido (1946–2024) |
| `triple_win_loser.jpeg` | Porcentaje de triples anotados: ganadores vs. perdedores (1981–2024) |
| `triple_evolucion.jpeg` | Volumen anual de triples realizados vs. intentados como % del total (1981–2024) |
| `triple_mid.jpeg` | Selección de tiro: % de triples vs. % de tiros de dos sobre el total (1981–2024) |

---

## 🔍 Hallazgos Principales

- **Pico histórico de anotación** en los años 60 (~235 pts/partido combinados), seguido de una caída sostenida hasta finales de los 90 (~186 pts), y una **recuperación notable desde 2014** impulsada por el triple.
- **Los perdedores anotan un mayor % de triples** que los ganadores de forma consistente desde ~1995, lo que sugiere que los equipos que van perdiendo tienden a forzar más tiros desde el perímetro.
- El tiro de dos puntos se mantiene estable como porcentaje del total (~48–55%), pero **comparte ahora el espacio con un volumen masivo de triples** que antes no existía.

---

## 🗂️ Estructura del Proyecto

```
eda-analysis/
│
├── data/
│   ├── raw/
│   │   └── game.csv                  # Dataset original descargado de Kaggle
│   └── processed/
│       └── game_processed.csv        # Dataset limpio tras el proceso ETL
│
├── src/
│   ├── down.py                       # Script de descarga del dataset desde Kaggle
│   └── clean.py                      # Pipeline ETL: extracción, transformación y carga
│
├── notebooks/
│   └── tests.ipynb                   # Notebook principal de análisis y visualización
│
├── outputs/
│   ├── figures/
│   │   ├── ptp_prom.jpeg
│   │   ├── triple_win_loser.jpeg
│   │   ├── triple_evolucion.jpeg
│   │   └── triple_mid.jpeg
│   └── index.html                    # Dashboard final con todos los gráficos
│
└── README.md
```

---

## 🛠️ Pipeline ETL (`clean.py`)

El script `clean.py` implementa un pipeline **Extracción → Transformación → Carga**:

**Extracción**
- Lee `game.csv` desde `data/raw/` seleccionando únicamente las columnas relevantes (tiros, puntos, tipo de temporada y fecha).

**Transformación**
- Convierte columnas numéricas y reemplaza valores nulos con `0`.
- Filtra para conservar solo partidos de **Temporada Regular** y **Playoffs**.
- Calcula métricas derivadas: puntos totales del partido, equipo ganador, triples combinados (`fg3m`, `fg3a`), porcentajes de tiro (`fg3pc`, `fgpc`, `fg2pc`) y porcentaje de tres puntos diferenciado por ganador/perdedor.
- Gestiona divisiones por cero con `np.where`.
- Elimina inconsistencias lógicas (ej. triples convertidos > triples intentados).

**Carga**
- Guarda el DataFrame procesado en `data/processed/game_processed.csv`.

---

## 📓 Notebook de Análisis (`tests.ipynb`)

El notebook realiza el análisis exploratorio completo sobre el dataset procesado (**60,475 partidos**, **27 columnas**).

**Columnas principales del dataset procesado:**

| Columna | Descripción |
|---|---|
| `game_year` | Año del partido |
| `pts_home` / `pts_away` | Puntos del equipo local y visitante |
| `fg3m` / `fg3a` | Triples realizados / intentados (combinados) |
| `fg3pc` | Porcentaje de triples del partido |
| `3p%_ganador` / `3p%_perdedor` | % de triples del equipo que ganó y del que perdió |
| `fg2a` / `fg2m` / `fg2pc` | Intentos, conversiones y % de tiros de dos puntos |
| `total_puntos` | Suma de puntos de ambos equipos |
| `ganador` | Indica si ganó `home` o `away` |
| `season_type` | `Regular Season` o `Playoffs` |

**Análisis realizados:**
- Estadísticas descriptivas generales (`describe()`).
- Evolución temporal del promedio de puntos (1946–2024).
- Comparativa anual del % de triples entre ganadores y perdedores.
- Evolución del volumen de triples realizados vs. intentados.
- Análisis de selección de tiro: triples vs. dos puntos como % del total de intentos.

---

## 📥 Datos

El dataset proviene de **Kaggle** ([NBA Games Dataset](https://www.kaggle.com/datasets/nathanlauga/nba-games)) y es descargado automáticamente mediante `down.py`.

El archivo original es `game.csv`, que contiene estadísticas de todos los partidos de la NBA desde la temporada 1946–47.

> ⚠️ Para ejecutar `down.py` se necesita una cuenta de Kaggle y el archivo `kaggle.json` con las credenciales en la ruta `~/.kaggle/kaggle.json`.

---

## ⚙️ Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/matheuuuuu1/eda-analysis.git
cd eda-analysis
```

### 2. Instalar dependencias

```bash
pip install pandas numpy matplotlib seaborn wget
```

### 3. Descargar el dataset

Coloca tu archivo `kaggle.json` en `~/.kaggle/` y luego ejecuta:

```bash
python src/down.py
```

### 4. Ejecutar el ETL

```bash
python src/clean.py
```

Esto genera `data/processed/game_processed.csv`.

### 5. Ejecutar el notebook

```bash
jupyter notebook notebooks/tests.ipynb
```

Los gráficos se exportarán automáticamente a `outputs/figures/`.

### 6. Ver el dashboard

Abre `outputs/index.html` en cualquier navegador para visualizar el reporte completo.

---

## 🧰 Tecnologías Utilizadas

| Librería | Uso |
|---|---|
| `pandas` | Manipulación y transformación de datos |
| `numpy` | Cálculos numéricos y manejo de casos borde |
| `matplotlib` | Generación de gráficos de línea |
| `seaborn` | Estética y paletas de color |
| `cycler` | Personalización de ciclos de color en matplotlib |
| `wget` | Descarga del dataset |
| Bootstrap 5 | Layout del dashboard HTML |

**Python:** 3.10+

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos y de análisis de datos.

---

*Datos procesados desde la base de datos en Kaggle mediante Python y Pandas.*
