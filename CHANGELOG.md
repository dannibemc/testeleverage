
# 📘 CHANGELOG - Plataforma Leverage

Todos os registros de alterações relevantes da plataforma serão documentados aqui.

---

## [1.0.0] - 2025-05-05
### Adicionado
- Estrutura inicial da aplicação em Streamlit
- Páginas: Dashboard, Cadastro de Obrigações, Lista de Obrigações
- Módulos: Due Diligence, Monitoramento de Crédito, Vencimento Antecipado
- Exportação para Excel
- Login e controle de sessão com autenticação
- Banco de dados SQLite com SQLAlchemy
- Tema visual baseado no Brandbook da Leverage
- Logo Leverage integrado ao topo
- Configuração `.streamlit/config.toml`
- README.md, .gitignore e .env.example

### Melhorias
- Estrutura modular por páginas
- Criação de formulários CRUD interativos
- OCR e NLP para extração de obrigações contratuais
- Classificação inteligente de eventos críticos
- Dashboard visual com gráficos de eventos

### Corrigido
- Layout de páginas e alinhamento de cores
- Erros de leitura de arquivos PDF, DOCX e XLSX

---

## Planejado para versões futuras
- Integração com banco PostgreSQL
- Envio automático de notificações
- Painel com BI interativo (Power BI ou Plotly)
- Logs de auditoria e controle de ações do usuário
