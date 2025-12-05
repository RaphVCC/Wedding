# ⚙️ Configuração Rápida no Render

Use estas configurações exatas para o seu deploy.

---

## 🔧 Configuração do Web Service

### Build Command:
```bash
cd frontend && npm install && npm run build && cd .. && pip install -r backend/requirements.txt && cd backend && alembic upgrade head
```

### Start Command:
```bash
cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Root Directory:
*(deixe vazio)*

---

## 🔐 Variáveis de Ambiente

Adicione estas variáveis no Render (Environment Variables):

### 1. DATABASE_URL
```
postgresql://weddingwebsite_bsbs_user:eLXkbiVBfawT9ymi7GwuMu1VTglc71zw@dpg-d4p24i63jp1c73dqe1gg-a/weddingwebsite_bsbs
```

### 2. JWT_SECRET
```
sua-chave-secreta-super-segura-para-jwt-2024-wedding
```
*(Gere uma string aleatória longa e segura)*

### 3. ADMIN_USERNAME
```
admin
```

### 4. ADMIN_PASSWORD
```
sua-senha-forte-aqui
```
*(Escolha uma senha forte para o admin)*

### 5. CORS_ORIGINS
```
["https://wedding-website-xxxx.onrender.com"]
```
*(Atualize com a URL real do seu serviço depois do deploy)*

### 6. ENVIRONMENT
```
prod
```

---

## 📋 Checklist de Configuração

- [ ] Web Service criado no Render
- [ ] Build Command configurado
- [ ] Start Command configurado
- [ ] Root Directory vazio
- [ ] DATABASE_URL adicionada
- [ ] JWT_SECRET adicionada
- [ ] ADMIN_USERNAME adicionada
- [ ] ADMIN_PASSWORD adicionada
- [ ] CORS_ORIGINS adicionada (atualizar depois)
- [ ] ENVIRONMENT = prod
- [ ] Deploy iniciado

---

## 🚀 Após o Deploy

1. **Anote a URL do serviço** (ex: `https://wedding-website-xxxx.onrender.com`)

2. **Atualize CORS_ORIGINS** com a URL real:
   ```
   ["https://wedding-website-xxxx.onrender.com"]
   ```

3. **Teste o site**: Acesse a URL do serviço

4. **Teste o admin**: `https://wedding-website-xxxx.onrender.com/admin/login`
   - Username: `admin`
   - Password: A senha que você configurou

---

## ⚠️ Importante

- **NÃO compartilhe** a URL do banco de dados publicamente
- **NÃO compartilhe** o JWT_SECRET
- **NÃO compartilhe** a senha do admin
- Mantenha essas informações seguras!

---

## 🎉 Pronto!

Depois de configurar tudo, o Render vai fazer o deploy automaticamente. Aguarde alguns minutos e seu site estará no ar!

