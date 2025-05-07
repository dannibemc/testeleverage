from PIL import Image
import easyocr
import fitz  # PyMuPDF
import numpy as np
import tempfile
import os

reader = easyocr.Reader(['pt', 'en'], gpu=False)

def extrair_texto_ocr(caminho_arquivo):
    textos = []

    if caminho_arquivo.lower().endswith('.pdf'):
        doc = fitz.open(caminho_arquivo)
        for page in doc:
            imagem = page.get_pixmap(dpi=300)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_img:
                tmp_img.write(imagem.tobytes())
                tmp_img.flush()
                resultado = reader.readtext(tmp_img.name, detail=0)
                textos.extend(resultado)
                os.unlink(tmp_img.name)
    else:
        imagem = Image.open(caminho_arquivo).convert("RGB")
        resultado = reader.readtext(np.array(imagem), detail=0)
        textos.extend(resultado)

    return "\n".join(textos)
