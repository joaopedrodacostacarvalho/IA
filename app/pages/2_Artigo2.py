import streamlit as st
from pathlib import Path
from utils.render_nb import render_notebook

st.title("Artigo 2 — Réplica & Melhorias")

nb_dir = Path(__file__).resolve().parents[1] / "notebooks"
cands = sorted([p for p in nb_dir.glob("*.ipynb")
                if ("artigo" in p.name.lower() and "2" in p.name.lower())])

if not cands:
    st.error("Não encontrei notebook do Artigo 2 em: " + str(nb_dir))
    st.code("\\n".join(sorted([p.name for p in nb_dir.glob('*.ipynb')])))
else:
    nb_path = cands[0]
    st.caption(f"Notebook alvo: **{nb_path.name}**")
    if st.button("Executar notebook agora", type="primary"):
        render_notebook(str(nb_path))
    else:
        st.info("Clique em **Executar notebook agora** para ver os resultados.")
