# 🐍 Forçar Python 3 no Render

O Render está detectando Elixir automaticamente. Vamos forçar Python 3!

---

## ✅ Solução 1: Usar Python 3 (Recomendado)

### Passo 1: Adicionar arquivo `runtime.txt`

Já foi criado! O arquivo `runtime.txt` na raiz força Python 3.11.9.

### Passo 2: Configurar no Render

1. **Runtime**: Selecione manualmente **"Python 3"** (não deixe "Auto-detect")
2. **Build Command**: 
   ```bash
   cd frontend && npm install && npm run build && cd .. && pip install -r backend/requirements.txt && cd backend && alembic upgrade head
   ```
3. **Start Command**: 
   ```bash
   cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

### Passo 3: Verificar

- O Render deve detectar `runtime.txt` automaticamente
- Se não detectar, selecione **"Python 3"** manualmente no dropdown

---

## 🐳 Solução 2: Usar Docker (Alternativa)

Se preferir Docker (mais controle):

### Passo 1: Usar o Dockerfile

Já foi criado! O `Dockerfile` está na raiz do projeto.

### Passo 2: Configurar no Render

1. **Runtime**: Selecione **"Docker"**
2. **Dockerfile Path**: Deixe vazio (está na raiz)
3. **Build Command**: *(deixe vazio - Docker faz tudo)*
4. **Start Command**: *(deixe vazio - Docker faz tudo)*

### Passo 3: Variáveis de Ambiente

Adicione as mesmas variáveis de antes.

---

## 📋 Comparação

| Opção | Vantagens | Desvantagens |
|-------|-----------|-------------|
| **Python 3** | ✅ Mais simples<br>✅ Build mais rápido<br>✅ Menos configuração | ⚠️ Precisa configurar Node manualmente |
| **Docker** | ✅ Controle total<br>✅ Ambiente isolado<br>✅ Mais previsível | ⚠️ Build mais lento<br>⚠️ Mais complexo |

---

## 🎯 Recomendação

**Use Python 3** (Solução 1) - é mais simples e funciona perfeitamente!

---

## ⚙️ Configuração no Render (Python 3)

### Campos Obrigatórios:

- **Runtime**: `Python 3` (selecione manualmente!)
- **Root Directory**: *(vazio)*
- **Build Command**: 
  ```bash
  cd frontend && npm install && npm run build && cd .. && pip install -r backend/requirements.txt && cd backend && alembic upgrade head
  ```
- **Start Command**: 
  ```bash
  cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```

### Variáveis de Ambiente:

```
DATABASE_URL = postgresql://weddingwebsite_bsbs_user:eLXkbiVBfawT9ymi7GwuMu1VTglc71zw@dpg-d4p24i63jp1c73dqe1gg-a/weddingwebsite_bsbs
JWT_SECRET = sua-chave-secreta
ADMIN_USERNAME = admin
ADMIN_PASSWORD = sua-senha
CORS_ORIGINS = ["https://wedding-website-xxxx.onrender.com"]
ENVIRONMENT = prod
```

---

## 🔧 Se Ainda Não Funcionar

1. **Delete o serviço** no Render
2. **Crie novamente** selecionando **"Python 3"** desde o início
3. **Não deixe** "Auto-detect" selecionado

---

## ✅ Checklist

- [ ] Arquivo `runtime.txt` na raiz (já criado)
- [ ] Runtime = **Python 3** (selecionado manualmente)
- [ ] Build Command configurado
- [ ] Start Command configurado
- [ ] Variáveis de ambiente adicionadas
- [ ] Deploy iniciado

---

## 🎉 Pronto!

Agora deve funcionar com Python 3! 🐍

