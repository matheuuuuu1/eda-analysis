# NBA Analysis - EDA con Jupyter
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /work

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements .
RUN pip install --no-cache-dir -r requirements jupyter

COPY notebooks/ notebooks/
COPY src/ src/
COPY data/ data/

# datos descargados por Kaggle se guardan fuera del contenedor (volumen)
VOLUME /work/data

EXPOSE 8888

CMD ["jupyter", "lab", "--ip", "0.0.0.0", "--port", "8888", "--no-browser", "--allow-root", "--NotebookApp.token="]
