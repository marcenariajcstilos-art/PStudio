import streamlit as st

# Configuração da página para parecer um site profissional
st.set_page_config(page_title="Palladium Studio | ArchViz", page_icon="🏢", layout="wide")

# Estilo personalizado para remover botões do Streamlit e melhorar o visual
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    h1 { color: #2c3e50; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #2c3e50; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("🏢 Palladium Studio - Visualização Arquitetônica")
st.subheader("Transformando projetos de marcenaria em experiências realistas.")
st.write("Especialista em renders de alta fidelidade para móveis planejados e fachadas comerciais.")

st.divider()

# --- GALERIA DE PROJETOS ---
st.header("🖼️ Portfólio Selecionado")

# Exemplo de como organizar seus renders em colunas
col1, col2 = st.columns(2)

with col1:
    # Substitua 'imagem1.jpg' pelo caminho real das suas melhores imagens
    st.image("https://via.placeholder.com/800x600.png?text=Render+Cozinha+MDF+Arauco", 
             caption="Cozinha Planejada - Acabamento Arauco e Granito São Gabriel")
    st.image("https://via.placeholder.com/800x600.png?text=Dormitorio+Casal", 
             caption="Dormitório Suíte - Iluminação em LED e Ripado")

with col2:
    st.image("https://via.placeholder.com/800x600.png?text=Fachada+Comercial", 
             caption="Fachada Comercial - Estudo de Materiais e Iluminação Diurna")
    st.image("https://via.placeholder.com/800x600.png?text=Area+Gourmet", 
             caption="Área Gourmet - Integração de Ambientes")

st.divider()

# --- SOBRE E DIFERENCIAL ---
col_sobre, col_contato = st.columns([2, 1])

with col_sobre:
    st.header("📌 Por que contratar o Palladium Studio?")
    st.write("""
    Diferente de projetistas comuns, eu entendo a rotina de uma marcenaria. 
    Meus projetos são pensados para:
    - **Aprovação Rápida:** O cliente visualiza exatamente o que será entregue.
    - **Fidelidade de Materiais:** Renders configurados com catálogos reais (Guararapes, Arauco, etc).
    - **Economia de Tempo:** Redução de retrabalho na montagem através de uma pré-visualização perfeita.
    """)

with col_contato:
    st.header("📩 Contato")
    st.write("📍 Ourinhos - SP")
    st.write("📱 WhatsApp: (14) 99840-5046")
    if st.button("Solicitar Orçamento"):
        st.write("Redirecionando para o WhatsApp...")

# Rodapé
st.markdown("<center>Palladium Studio © 2026</center>", unsafe_allow_html=True)