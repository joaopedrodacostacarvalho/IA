import base64
from pathlib import Path
import nbformat
from nbclient import execute as nb_execute
import streamlit as st

def _show_output(output):
    data = output.get("data", {})
    out_type = output.get("output_type")

    if out_type == "stream":
        text = output.get("text", "")
        if text:
            st.code(text)
        return

    if out_type == "error":
        ename = output.get("ename", "")
        evalue = output.get("evalue", "")
        traceback = "\n".join(output.get("traceback", []))
        st.error(f"{ename}: {evalue}")
        if traceback:
            st.code(traceback)
        return

    if "image/png" in data:
        st.image(base64.b64decode(data["image/png"]))
        return
    if "image/jpeg" in data:
        st.image(base64.b64decode(data["image/jpeg"]))
        return
    if "text/html" in data:
        from streamlit.components.v1 import html
        html(data["text/html"], height=500, scrolling=True)
        return
    if "text/plain" in data:
        st.code(data["text/plain"])
        return

def _render_cells(nb):
    """Renderiza células (markdown e outputs existentes)."""
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            st.markdown(cell.source)
        elif cell.cell_type == "code":
            if cell.outputs:
                for out in cell.outputs:
                    _show_output(out)

def _has_any_output(nb):
    for cell in nb.cells:
        if cell.cell_type == "code" and cell.outputs:
            return True
    return False

@st.cache_data(show_spinner=False)
def _read_nb_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

def render_notebook(nb_path: str, execute: bool = False, execute_timeout: int = 900, kernel_name: str = "python3"):
    """
    - execute=False: MODO RÁPIDO -> lê o .ipynb e exibe os outputs já salvos (não roda nada)
    - execute=True:  executa todas as células (lento) e exibe os outputs gerados agora
    """
    p = Path(nb_path)
    if not p.exists():
        st.error(f"Notebook não encontrado: {p}")
        return

    nb_txt = _read_nb_text(str(p))
    nb = nbformat.reads(nb_txt, as_version=4)

    if not execute:
        if _has_any_output(nb):
            st.info("Exibindo **outputs salvos** do notebook (modo rápido).")
            _render_cells(nb)
        else:
            st.warning("Este notebook não tem outputs salvos. Se quiser ver os resultados, selecione **Executar agora (lento)**.")
    else:
        st.info("Executando notebook agora (pode levar minutos)...")
        nb = nb_execute(nb, timeout=execute_timeout, kernel_name=kernel_name)
        _render_cells(nb)
