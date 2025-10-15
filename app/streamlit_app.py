import streamlit as st
from pathlib import Path
from utils.render_nb import render_notebook

st.set_page_config(page_title="Melhoria de Métodos IA — OULAD", layout="wide")

# ========================
# 🎛️ MENU LATERAL
# ========================
with st.sidebar:
    st.markdown("### 📚 Menu")
    page = st.radio("", ["🏠 Home", "📘 Artigo 1", "📗 Artigo 2"], label_visibility="collapsed")

def find_nb(which: int):
    nb_dir = Path(__file__).resolve().parent / "notebooks"
    cands = sorted([p for p in nb_dir.glob("*.ipynb")
                    if ("artigo" in p.name.lower() and str(which) in p.name.lower())])
    return nb_dir, (cands[0] if cands else None)

# ========================
# 🏠 HOME
# ========================
if page == "🏠 Home":
    st.title("Melhoria de Métodos IA — OULAD")
    st.markdown("""
    Este aplicativo foi desenvolvido como parte das atividades da disciplina **Inteligência Artificial (IA)** do curso de **Análise e Desenvolvimento de Sistemas – 3º Período**, no **Instituto Federal de Educação, Ciência e Tecnologia de Pernambuco (IFPE) – Campus Jaboatão dos Guararapes**.
    A pesquisa e implementação foram conduzidas pelos estudantes **João Pedro Carvalho da Costa** e **Marciojunior Almeida da Silva Filho**, com o objetivo de **replicar e aprimorar experimentos científicos em ambientes virtuais de aprendizagem (VLEs)** utilizando o conjunto de dados **OULAD (Open University Learning Analytics Dataset)**.
    O aplicativo, desenvolvido em **Streamlit**, tem como propósito **facilitar a visualização e execução dos experimentos** realizados a partir de dois artigos científicos que exploram a predição de desempenho e engajamento estudantil por meio de algoritmos de aprendizado de máquina:
    - **Artigo 1:** *Predicting At-Risk Students Using Clickstream Data in the Virtual Learning Environment* — **Réplica e Melhorias**
    - **Artigo 2:** *Students’ Academic Performance and Engagement Prediction in a Virtual Learning Environment Using Random Forest with Data Balancing* — **Réplica e Melhorias**
    > O uso do Streamlit possibilita integrar, em uma única interface, os notebooks de replicação e de aprimoramento dos modelos, permitindo comparar os resultados de forma interativa e acessível.
    **Dica:** Acesse o menu lateral para navegar entre as seções e clique em **“Executar notebook agora”** para reproduzir os experimentos diretamente no ambiente do app.
    """)

# ========================
# 📘 ARTIGO 1
# ========================
elif page == "📘 Artigo 1":
    st.title("Artigo 1 — Réplica & Melhorias")
    nb_dir, nb_path = find_nb(1)
    if nb_path is None:
        st.error("Não encontrei notebook do Artigo 1 em: " + str(nb_dir))
        st.code("\\n".join(sorted([p.name for p in nb_dir.glob('*.ipynb')])))
    else:
        st.caption(f"Notebook alvo: **{nb_path.name}**")
        mode = st.radio("Modo de exibição", ["Usar outputs salvos (rápido)", "Executar agora (lento)"], horizontal=True)
        if st.button("Mostrar", type="primary"):
            render_notebook(str(nb_path), execute=(mode == "Executar agora (lento)"))
        else:
            st.info("Escolha o modo e clique em **Mostrar**.")

# ========================
# 📗 ARTIGO 2
# ========================
elif page == "📗 Artigo 2":
    st.title("Artigo 2 — Continuação")
    nb_dir, nb_path = find_nb(2)
    if nb_path is None:
        st.error("Não encontrei notebook do Artigo 2 em: " + str(nb_dir))
        st.code("\\n".join(sorted([p.name for p in nb_dir.glob('*.ipynb')])))
    else:
        st.caption(f"Notebook alvo: **{nb_path.name}**")
        mode = st.radio("Modo de exibição", ["Usar outputs salvos (rápido)", "Executar agora (lento)"], horizontal=True)
        if st.button("Mostrar", type="primary"):
            render_notebook(str(nb_path), execute=(mode == "Executar agora (lento)"))
        else:
            st.info("Escolha o modo e clique em **Mostrar**.")
