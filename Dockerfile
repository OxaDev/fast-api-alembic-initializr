FROM python:3.12-slim

# Empêche Python d'écrire des .pyc et buffer stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dépendances système minimales
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Dépendances Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Code
COPY alembic /app/alembic
COPY api /app/api
COPY core /app/core
COPY db /app/db
COPY alembic.ini /app/alembic.ini

# Utilisateur non-root (optionnel mais recommandé)
RUN useradd -m apiuser
USER apiuser

EXPOSE 8000

# Lancement d'Uvicorn
CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000"]