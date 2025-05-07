
# 📘 Manual do Usuário – Plataforma Leverage

Este manual descreve o uso da plataforma Leverage para Gestão de Obrigações de Securitizadoras.

---

## ✅ Acesso ao Sistema

1. Acesse o link: `https://<seu_app>.streamlit.app/`
2. Use o menu lateral para navegar entre os módulos.

---

## 🧭 Módulos Disponíveis

### 1. **Dashboard**
- Visualização geral de:
  - Obrigações por status (A Vencer, Inadimplida, Cumprida)
  - Calendário de vencimentos
- Ideal para acompanhamento estratégico

---

### 2. **Cadastro de Obrigações**
- Preencha os seguintes campos:
  - Operação, Gestora, Categoria
  - Descrição no formato:
    ```
    Devedora - Documento - Cláusula - Resumo - Prazo - (Periodicidade)
    ```
  - Data de vencimento, Periodicidade
  - Última cobrança e observações
- O sistema calcula automaticamente:
  - Dias para vencimento
  - Status (Cumprida, A Vencer, Inadimplida)
  - Ação recomendada (Cobrar, Lembrete, Sem Ação)
  - Alerta de notificação (+45 dias vencido)

---

### 3. **Lista de Obrigações**
- Exibe todas as obrigações registradas
- Possui botão “📥 Exportar para Excel”
- Use para auditorias, revisões e análises externas

---

### 4. **Monitoramento de Crédito**
- Registre:
  - Entidade, Score, Limite, Vencimento
- Alertas aparecem se o vencimento estiver em até 7 dias
- Controle de risco de crédito

---

### 5. **Vencimento Antecipado**
- Registre ocorrências críticas por categoria:
  - Protesto, Judicial, Falência, Cross Default etc.
- Campos obrigatórios:
  - Parte, Data, Status, Fonte
- O sistema loga:
  - Valor máximo, recomendação jurídica, envio ao jurídico

---

### 6. **Due Diligence**
- Registre documentos recebidos (Estatuto, Certidão, etc.)
- Ações:
  - Marcar status (Pendente, Recebido)
  - Criar evento de vencimento antecipado com 1 clique

---

## 💾 Banco de Dados
- Os dados são armazenados localmente em `leverage.db`
- Todas as operações são persistentes

---

## 📤 Exportação
- Você pode exportar:
  - Obrigações (.xlsx)
  - Eventos críticos (.xlsx)

---

## 🧑‍💼 Suporte
Desenvolvido por Danielle Bernardo – Leverage Securitizadora  
Para dúvidas, contate: suporte@leveragesecuritizadora.com.br
