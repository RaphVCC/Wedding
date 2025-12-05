# 🚀 Quick Start - Render Deploy

## Passo a Passo Rápido

### 1️⃣ Criar Web Service no Render

1. Acesse: https://dashboard.render.com
2. Clique em **"New +"** → **"Web Service"**
3. Conecte: `MackKirk/WeddingWebsite`

### 2️⃣ Configurar o Serviço

**Campos:**
- **Name**: `wedding-website`
- **Root Directory**: *(vazio)*
- **Build Command**: 
  ```
  cd frontend && npm install && npm run build && cd .. && pip install -r backend/requirements.txt && cd backend && alembic upgrade head
  ```
- **Start Command**: 
  ```
  cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```

### 3️⃣ Adicionar Variáveis de Ambiente

Clique em **"Environment"** e adicione:

| Nome | Valor |
|------|-------|
| `DATABASE_URL` | `postgresql://weddingwebsite_bsbs_user:eLXkbiVBfawT9ymi7GwuMu1VTglc71zw@dpg-d4p24i63jp1c73dqe1gg-a/weddingwebsite_bsbs` |
| `JWT_SECRET` | `sua-chave-secreta-aqui` (gere uma string longa) |
| `ADMIN_USERNAME` | `admin` |
| `ADMIN_PASSWORD` | `sua-senha-forte` |
| `CORS_ORIGINS` | `["https://wedding-website-xxxx.onrender.com"]` (atualize depois) |
| `ENVIRONMENT` | `prod` |

### 4️⃣ Deploy

1. Clique em **"Create Web Service"**
2. Aguarde o build (10-15 minutos)
3. Anote a URL gerada

### 5️⃣ Atualizar CORS

1. Vá em **Environment**
2. Atualize `CORS_ORIGINS` com a URL real do serviço
3. Salve (vai reiniciar automaticamente)

### 6️⃣ Testar

- **Site**: `https://seu-servico.onrender.com`
- **Admin**: `https://seu-servico.onrender.com/admin/login`

---

## ✅ Pronto!

Seu site está no ar! 🎉

