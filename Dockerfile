# Multi-stage build para otimizar tamanho
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend

# Copiar arquivos do frontend
COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# Stage 2: Python backend
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do backend
COPY backend/ ./backend/

# Copiar frontend build do stage anterior
COPY --from=frontend-builder /app/frontend/dist ./backend/frontend_dist/

# Criar diretório de uploads
RUN mkdir -p backend/static/uploads

# Expor porta
EXPOSE $PORT

# Comando de start
WORKDIR /app/backend
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}

