import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
from utils.ui import aplicar_tema_leverage

# Configuração da página
st.set_page_config(page_title="Monitoramento de Securitização - Leverage", layout="wide")

# Aplica o tema
aplicar_tema_leverage()

# Título da página
st.title("🏢 Monitoramento de Securitização")

# Adicionar CSS personalizado para esta página
st.markdown("""
<style>
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #0066cc;
    }
    .metric-label {
        font-size: 14px;
        color: #666;
    }
    .alert-high {
        background-color: #ffebee;
        border-left: 5px solid #f44336;
        padding: 10px;
        margin-bottom: 10px;
    }
    .alert-medium {
        background-color: #fff8e1;
        border-left: 5px solid #ffc107;
        padding: 10px;
        margin-bottom: 10px;
    }
    .alert-low {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
        padding: 10px;
        margin-bottom: 10px;
    }
    .table-container {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Função para gerar dados de exemplo (simular dados reais)
def gerar_dados_securitizacao():
    # Tipos de operações de securitização
    tipos_operacao = ["CRI", "CRA", "FIDC", "Debêntures", "FII"]
    cedentes = ["Banco ABC", "Construtora XYZ", "Financeira 123", "Imobiliária Prime", "Agro Invest"]
    classes_risco = ["AAA", "AA+", "AA", "A+", "A", "BBB", "BB", "B"]
    indices = ["CDI", "IPCA", "IGPM", "SELIC", "Prefixado"]
    
    hoje = datetime.now()
    
    # Dados das operações de securitização
    operacoes = []
    
    # Gera 15 operações
    for i in range(15):
        tipo = random.choice(tipos_operacao)
        emissao = hoje - timedelta(days=random.randint(30, 730))
        vencimento = emissao + timedelta(days=random.randint(365, 3650))
        
        taxa_base = random.choice(indices)
        spread = random.uniform(1.0, 7.0)
        
        valor_emissao = random.randint(10000000, 500000000)
        classe_risco = random.choice(classes_risco)
        
        # Status da operação
        if vencimento < hoje:
            status = "Encerrada"
        else:
            status = random.choices(["Ativa", "Em monitoramento especial"], weights=[0.8, 0.2])[0]
        
        # Gerar um código de identificação para a operação
        codigo = f"{tipo}{random.randint(10, 99)}-{random.randint(1, 9)}ª"
        
        operacoes.append({
            "ID": i + 1,
            "Código": codigo,
            "Tipo": tipo,
            "Cedente": random.choice(cedentes),
            "Valor Emissão": valor_emissao,
            "Taxa": f"{taxa_base} + {spread:.2f}%" if taxa_base != "Prefixado" else f"{random.uniform(8.0, 15.0):.2f}%",
            "Taxa Base": taxa_base,
            "Spread": spread,
            "Classe de Risco": classe_risco,
            "Data de Emissão": emissao,
            "Data de Vencimento": vencimento,
            "Duração (anos)": round((vencimento - emissao).days / 365, 1),
            "Dias para Vencimento": (vencimento - hoje).days,
            "Status": status,
            "Lastro": random.choice(["Imobiliário", "Agronegócio", "Recebíveis Comerciais", "Crédito Corporativo", "Crédito Consignado"]),
            "Subordinação": random.uniform(5.0, 30.0)
        })
    
    # Dados de carteiras de crédito subjacentes
    carteiras = []
    
    # Para cada operação, criamos dados da carteira
    for op in operacoes:
        id_operacao = op["ID"]
        
        # Desempenho da carteira
        inadimplencia = random.uniform(0.5, 8.0)
        pdd = inadimplencia * random.uniform(1.0, 1.5)
        
        # Status da carteira baseado na inadimplência
        if inadimplencia < 2.0:
            status_carteira = "Normal"
        elif inadimplencia < 5.0:
            status_carteira = "Atenção"
        else:
            status_carteira = "Crítica"
        
        # Taxas de juros da carteira
        taxa_media = random.uniform(12.0, 28.0)
        
        # Prazo médio
        prazo_medio = random.randint(12, 120)
        
        # LTV médio (Loan to Value)
        ltv_medio = random.uniform(50.0, 85.0)
        
        # Valor da carteira
        valor_carteira = op["Valor Emissão"] * random.uniform(1.05, 1.3)
        
        # Quantidade de contratos
        qtd_contratos = random.randint(100, 5000)
        
        carteiras.append({
            "ID_Operacao": id_operacao,
            "Valor Carteira": valor_carteira,
            "Qtd Contratos": qtd_contratos,
            "Ticket Médio": valor_carteira / qtd_contratos,
            "Taxa Média": taxa_media,
            "Prazo Médio (meses)": prazo_medio,
            "LTV Médio": ltv_medio,
            "Inadimplência": inadimplencia,
            "PDD": pdd,
            "Status Carteira": status_carteira,
            "Concentração Maior Devedor": random.uniform(1.0, 15.0),
            "Concentração 5 Maiores": random.uniform(5.0, 30.0),
            "Garantia Principal": random.choice(["Imóvel", "Recebíveis", "Alienação", "Aval", "Hipoteca"]),
            "Índice de Cobertura": random.uniform(110.0, 150.0)
        })
    
    # Dados de fluxo de pagamentos
    pagamentos = []
    
    # Para cada operação, geramos alguns pagamentos
    for op in operacoes:
        id_operacao = op["ID"]
        data_emissao = op["Data de Emissão"]
        data_vencimento = op["Data de Vencimento"]
        
        # Define a quantidade de pagamentos já ocorridos
        if op["Status"] == "Encerrada":
            qtd_pagamentos = random.randint(10, 20)
        else:
            dias_desde_emissao = (hoje - data_emissao).days
            qtd_pagamentos = max(1, int(dias_desde_emissao / 30))
        
        # Gera os pagamentos
        for i in range(qtd_pagamentos):
            data_pagamento = data_emissao + timedelta(days=30 * (i + 1))
            
            if data_pagamento > hoje:
                continue
            
            valor_esperado = op["Valor Emissão"] * random.uniform(0.01, 0.03)
            
            # Define se houve atraso
            atraso = random.choices([True, False], weights=[0.1, 0.9])[0]
            
            if atraso:
                dias_atraso = random.randint(1, 30)
                data_efetiva = data_pagamento + timedelta(days=dias_atraso)
            else:
                dias_atraso = 0
                data_efetiva = data_pagamento
            
            # Define o valor efetivo
            if atraso:
                valor_efetivo = valor_esperado * random.uniform(0.9, 1.0)
            else:
                valor_efetivo = valor_esperado
            
            pagamentos.append({
                "ID_Operacao": id_operacao,
                "Número Pagamento": i + 1,
                "Data Prevista": data_pagamento,
                "Data Efetiva": data_efetiva,
                "Dias Atraso": dias_atraso,
                "Valor Esperado": valor_esperado,
                "Valor Efetivo": valor_efetivo,
                "Diferença": valor_efetivo - valor_esperado,
                "Status": "Atrasado" if atraso else "Regular"
            })
    
    return pd.DataFrame(operacoes), pd.DataFrame(carteiras), pd.DataFrame(pagamentos)

# Carregar ou gerar dados
if "df_securitizacao" not in st.session_state:
    df_operacoes, df_carteiras, df_pagamentos = gerar_dados_securitizacao()
    st.session_state.df_operacoes = df_operacoes
    st.session_state.df_carteiras = df_carteiras
    st.session_state.df_pagamentos = df_pagamentos

# Recupera os dataframes da sessão
df_operacoes = st.session_state.df_operacoes
df_carteiras = st.session_state.df_carteiras
df_pagamentos = st.session_state.df_pagamentos

# Dashboard principal
st.markdown("### Visão Geral das Operações de Securitização")

# Métricas principais
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_operacoes = len(df_operacoes)
    operacoes_ativas = len(df_operacoes[df_operacoes["Status"] == "Ativa"])
    st.markdown(f"""
    <div class="card">
        <div class="metric-label">Total de Operações</div>
        <div class="metric-value">{total_operacoes}</div>
        <div style="font-size: 14px; color: #666;">({operacoes_ativas} Ativas)</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    volume_total = df_operacoes["Valor Emissão"].sum()
    st.markdown(f"""
    <div class="card">
        <div class="metric-label">Volume Total Emitido</div>
        <div class="metric-value">R$ {volume_total/1_000_000:.1f} mi</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    # Média de inadimplência ponderada pelo valor da carteira
    media_inadimplencia = sum(df_carteiras["Inadimplência"] * df_carteiras["Valor Carteira"]) / sum(df_carteiras["Valor Carteira"])
    st.markdown(f"""
    <div class="card">
        <div class="metric-label">Inadimplência Média</div>
        <div class="metric-value">{media_inadimplencia:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    # Operações em monitoramento especial
    em_monitoramento = len(df_operacoes[df_operacoes["Status"] == "Em monitoramento especial"])
    st.markdown(f"""
    <div class="card">
        <div class="metric-label">Em Monitoramento Especial</div>
        <div class="metric-value">{em_monitoramento}</div>
        <div style="font-size: 14px; color: #666;">({em_monitoramento/total_operacoes*100:.1f}% do total)</div>
    </div>
    """, unsafe_allow_html=True)

# Gráficos 1
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Distribuição por Tipo de Operação")
    
    # Dados para o gráfico
    tipo_valores = df_operacoes.groupby("Tipo")["Valor Emissão"].sum().reset_index()
    
    # Cria o gráfico
    fig = px.pie(
        tipo_valores, 
        values="Valor Emissão", 
        names="Tipo",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Distribuição por Classe de Risco")
    
    # Dados para o gráfico
    risco_valores = df_operacoes.groupby("Classe de Risco")["Valor Emissão"].sum().reset_index()
    
    # Ordenar de acordo com o rating
    ordem_ratings = ["AAA", "AA+", "AA", "A+", "A", "BBB", "BB", "B"]
    risco_valores['ordem'] = risco_valores['Classe de Risco'].apply(lambda x: ordem_ratings.index(x) if x in ordem_ratings else 999)
    risco_valores = risco_valores.sort_values('ordem')
    
    # Cria o gráfico
    fig = px.bar(
        risco_valores, 
        x="Classe de Risco", 
        y="Valor Emissão",
        color="Classe de Risco",
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# Gráficos 2
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Vencimentos Projetados")
    
    # Preparar dados para gráfico de vencimentos
    df_vencimentos = df_operacoes[df_operacoes["Status"] != "Encerrada"].copy()
    df_vencimentos['Ano Vencimento'] = df_vencimentos['Data de Vencimento'].dt.year
    vencimentos_por_ano = df_vencimentos.groupby('Ano Vencimento')['Valor Emissão'].sum().reset_index()
    
    # Criar gráfico
    fig = px.bar(
        vencimentos_por_ano, 
        x="Ano Vencimento", 
        y="Valor Emissão",
        labels={"Valor Emissão": "Valor Total (R$)", "Ano Vencimento": "Ano de Vencimento"},
        color_discrete_sequence=['#0066cc']
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Inadimplência por Tipo de Lastro")
    
    # Juntar dados da operação e carteira
    df_combined = pd.merge(df_operacoes[['ID', 'Lastro', 'Valor Emissão']], 
                           df_carteiras[['ID_Operacao', 'Inadimplência', 'Valor Carteira']], 
                           left_on='ID', right_on='ID_Operacao')
    
    # Agregar por tipo de lastro
    lastro_inad = df_combined.groupby('Lastro')['Inadimplência'].mean().reset_index()
    lastro_inad = lastro_inad.sort_values('Inadimplência')
    
    # Criar gráfico
    fig = px.bar(
        lastro_inad, 
        x="Lastro", 
        y="Inadimplência",
        color="Inadimplência",
        color_continuous_scale='Reds',
        labels={"Inadimplência": "Taxa de Inadimplência (%)", "Lastro": "Tipo de Lastro"}
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# Alertas de Monitoramento
st.markdown("### Alertas de Monitoramento")

# Identificar carteiras críticas
carteiras_criticas = df_carteiras[df_carteiras["Status Carteira"] == "Crítica"]
ids_criticos = carteiras_criticas["ID_Operacao"].tolist()
operacoes_criticas = df_operacoes[df_operacoes["ID"].isin(ids_criticos)]

# Identificar pagamentos atrasados
pagamentos_atrasados = df_pagamentos[df_pagamentos["Status"] == "Atrasado"]
ids_atrasados = pagamentos_atrasados["ID_Operacao"].unique().tolist()
operacoes_atrasadas = df_operacoes[df_operacoes["ID"].isin(ids_atrasados)]

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Carteiras em Situação Crítica")
    
    if not operacoes_criticas.empty:
        for _, row in operacoes_criticas.iterrows():
            carteira = df_carteiras[df_carteiras["ID_Operacao"] == row["ID"]].iloc[0]
            st.markdown(f"""
            <div class="alert-high">
                <strong>{row['Código']} - {row['Tipo']} - {row['Cedente']}</strong><br>
                Inadimplência: {carteira['Inadimplência']:.2f}% | PDD: {carteira['PDD']:.2f}%<br>
                Valor da Carteira: R$ {carteira['Valor Carteira']/1_000_000:.2f} milhões<br>
                Índice de Cobertura: {carteira['Índice de Cobertura']:.2f}%
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("Não há carteiras em situação crítica no momento.")

with col2:
    st.markdown("#### Últimos Pagamentos Atrasados")
    
    if not pagamentos_atrasados.empty:
        # Ordene por data mais recente
        pagamentos_atrasados = pagamentos_atrasados.sort_values("Data Efetiva", ascending=False)
        
        for _, row in pagamentos_atrasados.head(5).iterrows():
            operacao = df_operacoes[df_operacoes["ID"] == row["ID_Operacao"]].iloc[0]
            st.markdown(f"""
            <div class="alert-medium">
                <strong>{operacao['Código']} - {operacao['Tipo']} - Pagamento #{row['Número Pagamento']}</strong><br>
                Atraso: {row['Dias Atraso']} dias | Valor: R$ {row['Valor Efetivo']/1_000_000:.2f} milhões<br>
                Data Prevista: {row['Data Prevista'].strftime('%d/%m/%Y')} | Data Efetiva: {row['Data Efetiva'].strftime('%d/%m/%Y')}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("Não há pagamentos atrasados registrados.")

# Timeline de pagamentos futuros
st.markdown("### Cronograma de Pagamentos Futuros")

# Simular pagamentos futuros
def gerar_pagamentos_futuros():
    hoje = datetime.now()
    data_limite = hoje + timedelta(days=180)  # próximos 6 meses
    
    pagamentos_futuros = []
    
    for _, op in df_operacoes[df_operacoes["Status"] != "Encerrada"].iterrows():
        id_operacao = op["ID"]
        ultimo_pagamento = df_pagamentos[df_pagamentos["ID_Operacao"] == id_operacao]["Número Pagamento"].max() if not df_pagamentos[df_pagamentos["ID_Operacao"] == id_operacao].empty else 0
        
        # Se não houver pagamentos anteriores, usamos a data de emissão
        ultima_data = df_pagamentos[df_pagamentos["ID_Operacao"] == id_operacao]["Data Prevista"].max() if not df_pagamentos[df_pagamentos["ID_Operacao"] == id_operacao].empty else op["Data de Emissão"]
        
        # Definir periodicidade (mensais, trimestrais, semestrais)
        periodicidade = random.choice([30, 90, 180])
        
        # Gerar próximos pagamentos
        proxima_data = ultima_data + timedelta(days=periodicidade)
        num_pagamento = ultimo_pagamento + 1
        
        while proxima_data <= data_limite:
            valor_esperado = op["Valor Emissão"] * random.uniform(0.01, 0.03)
            
            pagamentos_futuros.append({
                "ID_Operacao": id_operacao,
                "Código": op["Código"],
                "Tipo": op["Tipo"],
                "Cedente": op["Cedente"],
                "Número Pagamento": num_pagamento,
                "Data Prevista": proxima_data,
                "Valor Esperado": valor_esperado
            })
            
            proxima_data = proxima_data + timedelta(days=periodicidade)
            num_pagamento += 1
    
    return pd.DataFrame(pagamentos_futuros)

# Gerar pagamentos futuros
df_futuros = gerar_pagamentos_futuros()
df_futuros = df_futuros.sort_values("Data Prevista")

# Filtro por período
periodo = st.radio(
    "Período:",
    options=["Próximos 30 dias", "Próximos 90 dias", "Próximos 180 dias"],
    horizontal=True,
    index=0
)

hoje = datetime.now()
if periodo == "Próximos 30 dias":
    df_futuros_filtrado = df_futuros[df_futuros["Data Prevista"] <= (hoje + timedelta(days=30))]
elif periodo == "Próximos 90 dias":
    df_futuros_filtrado = df_futuros[df_futuros["Data Prevista"] <= (hoje + timedelta(days=90))]
else:
    df_futuros_filtrado = df_futuros[df_futuros["Data Prevista"] <= (hoje + timedelta(days=180))]

if not df_futuros_filtrado.empty:
    # Criar gráfico de timeline
fig = px.timeline(
    df_futuros_filtrado,
    x_start="Data Prevista",
    x_end="Data Prevista",  # Adicione esta linha
    y="Código",
    color="Tipo",
    hover_data=["Cedente", "Número Pagamento", "Valor Esperado"],
    height=400
)
fig.update_yaxes(autorange="reversed")
fig.update_layout(margin=dict(l=20, r=20, t=10, b=20))
st.plotly_chart(fig, use_container_width=True)
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(margin=dict(l=20, r=20, t=10, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabela de pagamentos futuros
    st.subheader(f"Pagamentos Previstos ({len(df_futuros_filtrado)})")
    
    # Formatar DataFrame para exibição
    df_exibir = df_futuros_filtrado.copy()
    df_exibir["Data Prevista"] = df_exibir["Data Prevista"].dt.strftime("%d/%m/%Y")
    df_exibir["Valor Esperado"] = df_exibir["Valor Esperado"].apply(lambda x: f"R$ {x/1_000_000:.2f} milhões")
    
    # Selecionar colunas para exibir
    colunas_exibir = ["Código", "Tipo", "Cedente", "Número Pagamento", "Data Prevista", "Valor Esperado"]
    
    # Exibir tabela
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.dataframe(
        df_exibir[colunas_exibir],
        use_container_width=True,
        hide_index=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info(f"Não há pagamentos previstos para os {periodo.lower()}.")

# Análise detalhada das operações
st.markdown("### Análise Detalhada")

# Selecionar operação
operacao_selecionada = st.selectbox(
    "Selecione uma operação para ver detalhes:",
    options=df_operacoes["ID"].tolist(),
    format_func=lambda x: f"{df_operacoes[df_operacoes['ID'] == x]['Código'].values[0]} - {df_operacoes[df_operacoes['ID'] == x]['Tipo'].values[0]} - {df_operacoes[df_operacoes['ID'] == x]['Cedente'].values[0]}"
)

if operacao_selecionada:
    # Obter dados da operação selecionada
    operacao = df_operacoes[df_operacoes["ID"] == operacao_selecionada].iloc[0]
    carteira = df_carteiras[df_carteiras["ID_Operacao"] == operacao_selecionada].iloc[0]
    
    # Pagamentos passados
    pagamentos_historico = df_pagamentos[df_pagamentos["ID_Operacao"] == operacao_selecionada].sort_values("Número Pagamento")
    
    # Pagamentos futuros
    pagamentos_futuros = df_futuros[df_futuros["ID_Operacao"] == operacao_selecionada].sort_values("Número Pagamento")
    
    # Exibir dados da operação
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Detalhes da Operação")
        st.markdown(f"""
        <div class="card">
            <p><strong>Código:</strong> {operacao['Código']}</p>
            <p><strong>Tipo:</strong> {operacao['Tipo']}</p>
            <p><strong>Cedente:</strong> {operacao['Cedente']}</p>
            <p><strong>Valor de Emissão:</strong> R$ {operacao['Valor Emissão']/1_000_000:.2f} milhões</p>
            <p><strong>Taxa:</strong> {operacao['Taxa']}</p>
            <p><strong>Classe de Risco:</strong> {operacao['Classe de Risco']}</p>
            <p><strong>Data de Emissão:</strong> {operacao['Data de Emissão'].strftime('%d/%m/%Y')}</p>
            <p><strong>Data de Vencimento:</strong> {operacao['Data de Vencimento'].strftime('%d/%m/%Y')}</p>
            <p><strong>Status:</strong> {operacao['Status']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Dados da Carteira")
        
        # Definir cores com base no status da carteira
        cor_status = "#4CAF50" if carteira['Status Carteira'] == "Normal" else "#FFC107" if carteira['Status Carteira'] == "Atenção" else "#F44336"
        
        st.markdown(f"""
        <div class="card">
            <p><strong>Valor da Carteira:</strong> R$ {carteira['Valor Carteira']/1_000_000:.2f} milhões</p>
            <p><strong>Quantidade de Contratos:</strong> {carteira['Qtd Contratos']}</p>
            <p><strong>Ticket Médio:</strong> R$ {carteira['Ticket Médio']/1_000:.2f} mil</p>
            <p><strong>Taxa Média:</strong> {carteira['Taxa Média']:.2f}% a.a.</p>
            <p><strong>Prazo Médio:</strong> {carteira['Prazo Médio (meses)']:.1f} meses</p>
            <p><strong>Inadimplência:</strong> <span style="color: {cor_status}; font-weight: bold;">{carteira['Inadimplência']:.2f}%</span></p>
            <p><strong>PDD:</strong> {carteira['PDD']:.2f}%</p>
            <p><strong>Concentração Maior Devedor:</strong> {carteira['Concentração Maior Devedor']:.2f}%</p>
            <p><strong>Garantia Principal:</strong> {carteira['Garantia Principal']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Histórico de pagamentos
    st.markdown("#### Histórico de Pagamentos")
    
    if not pagamentos_historico.empty:
        # Preparar dados para o gráfico
        pagamentos_historico['Cumprimento'] = (pagamentos_historico['Valor Efetivo'] / pagamentos_historico['Valor Esperado']) * 100
        pagamentos_historico['Cor'] = pagamentos_historico['Dias Atraso'].apply(lambda x: '#F44336' if x > 15 else '#FFC107' if x > 0 else '#4CAF50')
        
        # Criar gráfico
        fig = go.Figure()
        
        # Adicionar barras para cada pagamento
        fig.add_trace(go.Bar(
            x=pagamentos_historico['Número Pagamento'],
            y=pagamentos_historico['Cumprimento'],
            marker_color=pagamentos_historico['Cor'],
            name='Cumprimento (%)'
        ))
        
        # Adicionar linha de 100%
        fig.add_shape(
            type='line',
            x0=0,
            x1=pagamentos_historico['Número Pagamento'].max() + 1,
            y0=100,
            y1=100,
            line=dict(color='black', width=2, dash='dash')
        )
        
        # Configurar layout
        fig.update_layout(
            title="Histórico de Cumprimento dos Pagamentos (%)",
            xaxis_title="Número do Pagamento",
            yaxis_title="Cumprimento (%)",
            height=400,
            yaxis=dict(range=[0, max(120, pagamentos_historico['Cumprimento'].max() + 10)])
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabela de histórico de pagamentos
        st.markdown("##### Detalhes dos Pagamentos")
        
        # Formatar DataFrame para exibição
        df_hist_exibir = pagamentos_historico.copy()
        df_hist_exibir["Data Prevista"] = df_hist_exibir["Data Prevista"].dt.strftime("%d/%m/%Y")
        df_hist_exibir["Data Efetiva"] = df_hist_exibir["Data Efetiva"].dt.strftime("%d/%m/%Y")
        df_hist_exibir["Valor Esperado"] = df_hist_exibir["Valor Esperado"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
        df_hist_exibir["Valor Efetivo"] = df_hist_exibir["Valor Efetivo"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
        
        # Selecionar colunas para exibir
        colunas_hist = ["Número Pagamento", "Data Prevista", "Data Efetiva", "Dias Atraso", "Valor Esperado", "Valor Efetivo", "Status"]
        
        # Exibir tabela
        st.markdown('<div class="table-container">', unsafe_allow_html=True)
        st.dataframe(
            df_hist_exibir[colunas_hist],
            use_container_width=True,
            hide_index=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Não há histórico de pagamentos para esta operação.")
    
    # Evolução da carteira
    st.markdown("#### Evolução da Inadimplência")
    
    # Simulação de dados históricos de inadimplência
    def gerar_dados_historicos():
        hoje = datetime.now()
        datas = []
        inadimplencias = []
        
        # Valor atual da inadimplência
        inad_atual = carteira['Inadimplência']
        
        # Gerar 12 meses de histórico
        for i in range(12, 0, -1):
            data = hoje - timedelta(days=30 * i)
            datas.append(data)
            
            # Simular variações na inadimplência
            variacao = random.uniform(-0.5, 0.7)
            inad = max(0.2, inad_atual + variacao * (i / 2))
            inadimplencias.append(inad)
        
        # Adicionar valor atual
        datas.append(hoje)
        inadimplencias.append(inad_atual)
        
        return pd.DataFrame({
            'Data': datas,
            'Inadimplência': inadimplencias
        })
    
    df_hist_inad = gerar_dados_historicos()
    
    # Criar gráfico de linha
    fig = px.line(
        df_hist_inad, 
        x='Data', 
        y='Inadimplência',
        labels={'Inadimplência': 'Taxa de Inadimplência (%)', 'Data': 'Período'},
        line_shape='spline',
        markers=True
    )
    
    # Adicionar áreas de referência
    fig.add_shape(
        type="rect",
        x0=df_hist_inad['Data'].min(),
        x1=df_hist_inad['Data'].max(),
        y0=0,
        y1=2,
        fillcolor="rgba(76, 175, 80, 0.2)",
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_shape(
        type="rect",
        x0=df_hist_inad['Data'].min(),
        x1=df_hist_inad['Data'].max(),
        y0=2,
        y1=5,
        fillcolor="rgba(255, 193, 7, 0.2)",
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_shape(
        type="rect",
        x0=df_hist_inad['Data'].min(),
        x1=df_hist_inad['Data'].max(),
        y0=5,
        y1=df_hist_inad['Inadimplência'].max() * 1.2,
        fillcolor="rgba(244, 67, 54, 0.2)",
        line=dict(width=0),
        layer="below"
    )
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Análise de cobertura e subordinação
    st.markdown("#### Análise de Cobertura e Subordinação")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de cobertura
        valor_carteira = carteira['Valor Carteira']
        valor_emissao = operacao['Valor Emissão']
        cobertura = (valor_carteira / valor_emissao) * 100
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = cobertura,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Índice de Cobertura (%)"},
            gauge = {
                'axis': {'range': [100, 160]},
                'bar': {'color': "#0066cc"},
                'steps': [
                    {'range': [100, 110], 'color': "#ffcccb"},
                    {'range': [110, 130], 'color': "#ffffcc"},
                    {'range': [130, 160], 'color': "#ccffcc"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 110
                }
            }
        ))
        
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Gráfico de subordinação
        subordinacao = carteira['Subordinação']
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = subordinacao,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Nível de Subordinação (%)"},
            gauge = {
                'axis': {'range': [0, 40]},
                'bar': {'color': "#0066cc"},
                'steps': [
                    {'range': [0, 10], 'color': "#ffcccb"},
                    {'range': [10, 20], 'color': "#ffffcc"},
                    {'range': [20, 40], 'color': "#ccffcc"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 15
                }
            }
        ))
        
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Botões de ação
    st.markdown("#### Ações de Monitoramento")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Gerar Relatório Completo", type="primary"):
            st.info("Gerando relatório completo da operação. Esta funcionalidade será implementada em breve.")
    
    with col2:
        if operacao["Status"] != "Em monitoramento especial":
            if st.button("⚠️ Colocar em Monitoramento Especial"):
                st.warning("Operação colocada em monitoramento especial.")
        else:
            if st.button("✅ Remover do Monitoramento Especial"):
                st.success("Operação removida do monitoramento especial.")
    
    with col3:
        if st.button("📧 Enviar Notificação ao Cedente"):
            st.info("Funcionalidade de envio de notificação em desenvolvimento.")

# Análise de portfólio
st.markdown("### Análise de Portfólio")

# Tabs para diferentes análises
tab1, tab2, tab3 = st.tabs(["Visão por Cedente", "Análise de Risco", "Projeção de Fluxo"])

with tab1:
    # Análise por cedente
    st.markdown("#### Exposição por Cedente")
    
    # Dados para análise
    cedente_analise = df_operacoes.groupby("Cedente").agg({
        "Valor Emissão": "sum",
        "ID": "count"
    }).reset_index()
    
    cedente_analise.columns = ["Cedente", "Valor Emissão", "Quantidade de Operações"]
    cedente_analise = cedente_analise.sort_values("Valor Emissão", ascending=False)
    
    # Calcular percentual
    valor_total = cedente_analise["Valor Emissão"].sum()
    cedente_analise["Percentual"] = cedente_analise["Valor Emissão"] / valor_total * 100
    
    # Gráfico de barras
    fig = px.bar(
        cedente_analise,
        x="Cedente",
        y="Valor Emissão",
        text="Percentual",
        color="Quantidade de Operações",
        color_continuous_scale="Viridis",
        labels={
            "Valor Emissão": "Valor Total (R$)",
            "Cedente": "Cedente",
            "Percentual": "% do Portfólio"
        }
    )
    
    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='outside'
    )
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabela com detalhes dos cedentes
    cedente_detalhes = df_operacoes.groupby("Cedente").apply(lambda x: pd.Series({
        "Quantidade": len(x),
        "Valor Total": x["Valor Emissão"].sum(),
        "Menor Operação": x["Valor Emissão"].min(),
        "Maior Operação": x["Valor Emissão"].max(),
        "Operação Média": x["Valor Emissão"].mean(),
        "Tipos": ", ".join(x["Tipo"].unique()),
        "Classes de Risco": ", ".join(x["Classe de Risco"].unique())
    })).reset_index()
    
    # Formatar valores
    cedente_detalhes["Valor Total"] = cedente_detalhes["Valor Total"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
    cedente_detalhes["Menor Operação"] = cedente_detalhes["Menor Operação"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
    cedente_detalhes["Maior Operação"] = cedente_detalhes["Maior Operação"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
    cedente_detalhes["Operação Média"] = cedente_detalhes["Operação Média"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
    
    # Exibir tabela
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.dataframe(
        cedente_detalhes,
        use_container_width=True,
        hide_index=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    # Análise de risco
    st.markdown("#### Distribuição por Classe de Risco")
    
    # Preparar dados para heat map
    risco_tipo = df_operacoes.pivot_table(
        index="Classe de Risco",
        columns="Tipo",
        values="Valor Emissão",
        aggfunc="sum",
        fill_value=0
    )
    
    # Ordenar os ratings
    ordem_ratings = ["AAA", "AA+", "AA", "A+", "A", "BBB", "BB", "B"]
    risco_tipo = risco_tipo.reindex(ordem_ratings)
    
    # Criar heatmap
    fig = px.imshow(
        risco_tipo,
        labels=dict(x="Tipo de Operação", y="Classe de Risco", color="Valor (R$)"),
        x=risco_tipo.columns,
        y=risco_tipo.index,
        color_continuous_scale="Viridis",
        aspect="auto"
    )
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Análise de concentração de risco
    st.markdown("#### Concentração de Risco")
    
    # Calcular percentuais por classe de risco
    risco_percentual = df_operacoes.groupby("Classe de Risco")["Valor Emissão"].sum().reset_index()
    risco_percentual["Percentual"] = risco_percentual["Valor Emissão"] / risco_percentual["Valor Emissão"].sum() * 100
    
    # Ordenar por rating
    risco_percentual['ordem'] = risco_percentual['Classe de Risco'].apply(lambda x: ordem_ratings.index(x) if x in ordem_ratings else 999)
    risco_percentual = risco_percentual.sort_values('ordem')
    
    # Criar gráfico de sunburst
    tipos_percentual = df_operacoes.groupby(["Classe de Risco", "Tipo"])["Valor Emissão"].sum().reset_index()
    
    fig = px.sunburst(
        tipos_percentual,
        path=['Classe de Risco', 'Tipo'],
        values='Valor Emissão',
        color='Classe de Risco',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    # Projeção de fluxo
    st.markdown("#### Projeção de Fluxo de Caixa")
    
    # Gerar projeção de fluxo para os próximos 12 meses
    def gerar_projecao_fluxo():
        hoje = datetime.now()
        meses = []
        recebimentos = []
        pagamentos = []
        
        for i in range(12):
            mes = hoje + timedelta(days=30 * i)
            mes_str = mes.strftime("%b/%Y")
            meses.append(mes_str)
            
            # Estimar recebimentos
            recebimento = 0
            for _, op in df_operacoes[df_operacoes["Status"] != "Encerrada"].iterrows():
                valor_emissao = op["Valor Emissão"]
                # Supondo pagamentos mensais médios de 1-3% do valor de emissão
                taxa_pagamento = random.uniform(0.01, 0.03)
                recebimento += valor_emissao * taxa_pagamento
            
            # Adicionar variação aleatória
            variacao = random.uniform(0.8, 1.2)
            recebimento = recebimento * variacao
            recebimentos.append(recebimento)
            
            # Estimar pagamentos (uma parte dos recebimentos vai para investidores)
            pagamento = recebimento * random.uniform(0.6, 0.9)
            pagamentos.append(pagamento)
        
        return meses, recebimentos, pagamentos
    
    meses, recebimentos, pagamentos = gerar_projecao_fluxo()
    
    # Criar gráfico de fluxo de caixa
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=meses,
        y=recebimentos,
        name='Recebimentos Projetados',
        marker_color='#4CAF50'
    ))
    
    fig.add_trace(go.Bar(
        x=meses,
        y=pagamentos,
        name='Pagamentos aos Investidores',
        marker_color='#FFC107'
    ))
    
    fig.add_trace(go.Scatter(
        x=meses,
        y=[r-p for r, p in zip(recebimentos, pagamentos)],
        mode='lines+markers',
        name='Resultado Líquido',
        line=dict(color='#0066cc', width=3)
    ))
    
    fig.update_layout(
        title="Projeção de Fluxo de Caixa - Próximos 12 Meses",
        xaxis_title="Mês",
        yaxis_title="Valor (R$)",
        barmode='group',
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabela de projeção
    st.markdown("#### Detalhamento da Projeção")
    
    df_projecao = pd.DataFrame({
        "Mês": meses,
        "Recebimentos": recebimentos,
        "Pagamentos": pagamentos,
        "Resultado": [r-p for r, p in zip(recebimentos, pagamentos)]
    })
    
    # Formatar valores
    df_projecao["Recebimentos"] = df_projecao["Recebimentos"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
    df_projecao["Pagamentos"] = df_projecao["Pagamentos"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
    df_projecao["Resultado"] = df_projecao["Resultado"].apply(lambda x: f"R$ {x/1_000_000:.2f} mi")
    
    # Exibir tabela
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.dataframe(
        df_projecao,
        use_container_width=True,
        hide_index=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Informações sobre o módulo
with st.expander("ℹ️ Sobre este Módulo"):
    st.markdown("""
    ### Módulo de Monitoramento de Securitização
    
    Este módulo foi desenvolvido para atender às necessidades específicas de securitizadoras, permitindo:
    
    - **Monitoramento de Operações**: Acompanhamento completo de CRIs, CRAs, FIDCs e outras operações de securitização
    - **Análise de Carteiras**: Monitoramento de índices de inadimplência, PDD e cobertura das carteiras cedidas
    - **Gestão de Fluxo**: Projeção e acompanhamento de fluxos de pagamento
    - **Análise de Risco**: Visualização da concentração de risco por tipo de operação e classe de risco
    - **Alertas**: Identificação proativa de carteiras em situação de deterioração
    
    Os dados exibidos nesta página são exemplos gerados aleatoriamente. Em uma implementação real, eles seriam carregados do banco de dados da securitizadora.
    """)
        
