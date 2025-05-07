
#!/bin/bash

# Verifica se o repositório Git está inicializado
if [ ! -d ".git" ]; then
    git init
    echo "Repositório Git inicializado."
fi

# Solicita nome do repositório remoto se não estiver configurado
if ! git remote get-url origin &> /dev/null; then
    read -p "Digite a URL do seu repositório GitHub: " REPO_URL
    git remote add origin "$REPO_URL"
fi

# Adiciona e commita as alterações
git add .
git commit -m "Deploy inicial da plataforma Leverage Streamlit"
git branch -M main

# Realiza push para o GitHub
git push -u origin main
