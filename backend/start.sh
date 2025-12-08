#!/bin/bash
set -e

echo "Starting Wedding Website Backend..."

# Verificar se estamos no diretório correto
if [ ! -f "app/main.py" ]; then
    echo "Error: app/main.py not found. Make sure you're in the backend directory."
    exit 1
fi

# Rodar migrations
echo "Running database migrations..."
alembic upgrade head || echo "Warning: Migration failed, continuing..."

# Iniciar servidor
echo "Starting uvicorn server on port ${PORT:-8000}..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}

