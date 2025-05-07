import streamlit as st
import tempfile
import os
from ocr_utils import extrair_texto_ocr

st.set_page_config(page_title="Mapeamento de Obrigações", layout="wide")

st.title("🧾 Mapeamento de Obrigações")
st.markdown("📄 Envie um contrato ou documento escaneado (.pdf ou imagem)")

uploaded_file = st.file_uploader(
    "Drag and drop file here",
    type=["pdf", "png", "jpg", "jpeg"],
    label_visibility="collapsed"
)

if uploaded_file:
    st.markdown(f"📎 **{uploaded_file.name}**")

    # Salvar o arquivo temporariamente
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    try:
        with st.spinner("🔍 Extraindo texto com OCR..."):
            texto_extraido = extrair_texto_ocr(temp_path)

        if texto_extraido.strip():
            st.success("✅ Texto extraído com sucesso!")
            st.text_area("📝 Resultado da Extração", value=texto_extraido, height=400)
        else:
            st.warning("⚠️ Nenhum texto foi detectado.")

    except Exception as e:
        st.error(f"❌ Erro durante a extração: {e}")

    # Remover arquivo temporário
    os.remove(temp_path)
else:
    st.info("📂 Aguarde o envio de um arquivo.")
