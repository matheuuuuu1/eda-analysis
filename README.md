# NBA Evolution Analysis
Este proyecto realiza un análisis exploratorio de datos (EDA) sobre la evolución histórica de la NBA, enfocándose en cómo la introducción de la línea de tres puntos y los cambios en la selección de tiro han transformado la eficiencia y el volumen de anotación desde 1946 hasta el presente.

# Estructura del Proyecto
La organización de carpetas sigue un estándar profesional para proyectos de ciencia de datos:
NBA Analysis/
├── data/
│ ├── raw/ # Datos originales (CSVs descargados)
│ └── processed/ # Datos limpios listos para análisis
├── src/
│ └── func/
│ ├── down.py # Script para descargar datos de Kaggle
│ └── clean.py # Script de procesamiento y limpieza (ETL)
├── tests.ipynb # Notebook con visualizaciones y hallazgos
├── requirements.txt # Librerías necesarias para ejecutar el proyecto
└── .gitignore # Archivos excluidos (datos pesados y credenciales)

# Configuración e Instalación
## 1. Requisitos Previos
Es necesario tener instalado Python 3.x y las dependencias listadas en el archivo de requerimientos:
pip install -r requirements.txt
## 2. Datos de Kaggle
El proyecto utiliza el dataset wyattowalsh/basketball. Para que el script down.py funcione, debes colocar tu archivo kaggle.json en src/func/ y configurar los permisos en Linux:
chmod 600 src/func/kaggle.json

# Scripts Principales
## ● down.py: 
Automatiza la descarga del archivo game.csv. Maneja la descompresión y
limpieza de archivos temporales (.zip).
## ● clean.py: 
Utiliza Pandas y NumPy para transformar los datos crudos, calcular promedios
anuales y filtrar estadísticas relevantes como el % de triples y tiros de campo.
## ● tests.ipynb: 
Contiene la lógica de visualización utilizando Matplotlib y Seaborn,
generando gráficos de alta resolución sobre la evolución del juego.

# Análisis y Resultados
### Puntos Totales:
Evolución del promedio de puntos combinados por partido desde la fundación de la liga.
### Evolución del Triple:
Comparativa del volumen de triples intentados vs. realizados desde su implementación en 1981.
### Eficiencia Ganadora:
Análisis de cómo el porcentaje de tiro de 3 puntos diferencia a los equipos ganadores de los perdedores.

# Autor
Proyecto desarrollado por matheuuuuu1 como parte de un estudio de análisis de datos deportivos.
