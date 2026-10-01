#!/usr/bin/env bash
# NBA EDA: dashboard estático generado (outputs/). Servir el resultado.
# El pipeline (down.py → clean.py → notebook) necesita pip: pandas numpy matplotlib seaborn
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -f outputs/index.html ]; then
    echo "Falta outputs/index.html. Genera el dashboard primero:"
    echo "  pip install pandas numpy matplotlib seaborn"
    echo "  python src/down.py && python src/clean.py"
    echo "  jupyter notebook notebooks/tests.ipynb"
    exit 1
fi
echo "Dashboard:  http://localhost:8090"
exec python3 -m http.server 8090 -d outputs
