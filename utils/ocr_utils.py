# ocr_utils.py
import easyocr

def extrair_texto_ocr(caminho_arquivo):
    reader = easyocr.Reader(['pt'], gpu=False)
    resultado = reader.readtext(caminho_arquivo, detail=0, paragraph=True)
    return "\n".join(resultado)
