
# Plataforma Leverage - Gestão de Obrigações

Sistema interativo em Streamlit para gestão de obrigações contratuais de securitizadoras.

[![Deploy on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)

## 🔧 Funcionalidades

- Cadastro e controle de obrigações com cálculo automático de vencimento
- Monitoramento de crédito com alertas de score e limites
- Vencimento antecipado com categorização crítica
- Due diligence com vínculo automático a eventos
- Painéis visuais (gráficos e calendário)
- Exportação de dados para Excel
- Banco SQLite integrado

## 📦 Estrutura

```
📁 leverage/
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Cadastro_de_Obrigacoes.py
│   ├── 3_Lista_de_Obrigacoes.py
│   ├── 4_Monitoramento_de_Credito.py
│   ├── 5_Vencimento_Antecipado.py
│   └── 6_Due_Diligence.py
│
├── static/logo.png
├── app.py
├── models.py
├── requirements.txt
├── leverage.db  ← será gerado na primeira execução
├── .env.example
└── README.md
```

## ▶️ Executar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Deploy no Streamlit Cloud

1. Faça push para o GitHub
2. Vá para https://streamlit.io/cloud
3. Crie novo app apontando para `app.py` no seu repositório

---

© Leverage Securitizadora - Desenvolvido por Danielle Bernardo
