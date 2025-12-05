# 🚀 Deploy em Serviço Único (Frontend + Backend)

Este guia mostra como fazer deploy do frontend e backend no **mesmo Web Service** no Render.

## 📋 Pré-requisitos

1. Código já no GitHub: https://github.com/MackKirk/WeddingWebsite
2. Conta no Render.com

---

## 🗄️ PASSO 1: Criar Banco PostgreSQL

1. Acesse [dashboard.render.com](https://dashboard.render.com)
2. Clique em **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `wedding-db`
   - **Region**: Escolha a mais próxima
   - **Plan**: Free
4. Clique em **"Create Database"**
5. **Anote a Internal Database URL**

---

## ⚙️ PASSO 2: Criar Web Service Único

### 2.1 Criar o Serviço

1. No Render, clique em **"New +"** → **"Web Service"**
2. Conecte seu repositório: `MackKirk/WeddingWebsite`
3. Configure:

**Configurações Básicas:**
- **Name**: `wedding-website`
- **Region**: Mesma do banco
- **Branch**: `main`
- **Root Directory**: *(deixe vazio - raiz do projeto)*
- **Runtime**: `Python 3`
- **Build Command**: 
  ```bash
  cd frontend && npm install && npm run build && cd .. && pip install -r backend/requirements.txt && cd backend && alembic upgrade head
  ```
- **Start Command**: 
  ```bash
  cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```

### 2.2 Variáveis de Ambiente

Adicione estas variáveis:

```
DATABASE_URL = <Internal Database URL do passo 1>
```

```
JWT_SECRET = <Gere uma string aleatória longa>
```

```
ADMIN_USERNAME = admin
```

```
ADMIN_PASSWORD = <Escolha uma senha forte>
```

```
CORS_ORIGINS = ["https://wedding-website.onrender.com"]
```
*(Atualize com a URL real depois)*

```
ENVIRONMENT = prod
```

**NÃO precisa** de `VITE_API_URL` - o frontend vai usar o mesmo domínio!

### 2.3 Fazer Deploy

1. Clique em **"Create Web Service"**
2. Aguarde o build (pode levar 10-15 minutos)
3. Anote a URL gerada (ex: `https://wedding-website-xxxx.onrender.com`)

---

## ✅ PASSO 3: Testar

### 3.1 Testar Site Público

1. Acesse a URL do serviço
2. Deve carregar o site de casamento completo
3. Navegue pelas páginas

### 3.2 Testar Admin

1. Acesse: `https://wedding-website-xxxx.onrender.com/admin/login`
2. Login com:
   - **Username**: `admin`
   - **Password**: A senha que você configurou

### 3.3 Testar API

1. Acesse: `https://wedding-website-xxxx.onrender.com/api/home`
2. Deve retornar JSON com os dados

---

## 🔧 Como Funciona

### Estrutura de Rotas

- **`/`** → Frontend (React SPA)
- **`/api/*`** → API Backend
- **`/auth/*`** → Autenticação
- **`/static/*`** → Arquivos estáticos (uploads)
- **`/admin/*`** → Admin panel (servido pelo frontend)

### Build Process

1. **Frontend**: Compila React e coloca em `backend/frontend_dist/`
2. **Backend**: Instala dependências Python
3. **Database**: Roda migrations
4. **Start**: Inicia FastAPI que serve tudo

---

## 🐛 Solução de Problemas

### Problema: Frontend não carrega

**Solução:**
- Verifique se o build do frontend está funcionando
- Veja os logs do build no Render
- Certifique-se que `backend/frontend_dist/` existe após o build

### Problema: 404 em rotas do frontend

**Solução:**
- Isso é normal! O FastAPI está configurado para servir `index.html` para todas as rotas não-API
- Verifique se o arquivo `backend/frontend_dist/index.html` existe

### Problema: API não funciona

**Solução:**
- Verifique se as rotas começam com `/api/` ou `/auth/`
- Veja os logs do serviço no Render
- Teste diretamente: `https://seu-site.onrender.com/api/home`

### Problema: Build demora muito

**Solução:**
- Normal na primeira vez (instala Node + Python)
- Builds seguintes são mais rápidos (cache)
- Plano free pode ser mais lento

---

## 📝 Checklist

- [ ] Banco PostgreSQL criado
- [ ] Web Service criado com build command correto
- [ ] Variáveis de ambiente configuradas
- [ ] Deploy concluído
- [ ] Site público funcionando
- [ ] Admin panel acessível
- [ ] API respondendo

---

## 💡 Vantagens do Serviço Único

✅ **Mais Simples**: Um único serviço para gerenciar  
✅ **Mais Barato**: Apenas um serviço (plano free)  
✅ **Sem CORS**: Frontend e backend no mesmo domínio  
✅ **Deploy Automático**: Um push no GitHub atualiza tudo  

---

## 🔄 Atualizações

Sempre que fizer push no GitHub, o Render:
1. Detecta a mudança
2. Roda o build command
3. Reinicia o serviço
4. Tudo atualizado automaticamente!

---

## 🎉 Pronto!

Seu site está no ar em uma única URL! Compartilhe com seus convidados.

**URL do Site**: `https://wedding-website-xxxx.onrender.com`

