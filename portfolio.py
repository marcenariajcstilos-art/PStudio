import streamlit as st

# O layout="wide" usa bem a tela do PC e se adapta no celular
st.set_page_config(page_title="Palladium Studio | ArchViz", page_icon="🏛️", layout="wide")

# --- CSS INJETADO (Apenas para fontes e botões, sem quebrar o layout nativo) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }

    /* Esconde a interface padrão de aplicativo do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Botão elegante do WhatsApp */
    .btn-contato {
        display: block;
        background-color: #1A1A1A;
        color: #FFFFFF !important;
        text-align: center;
        padding: 15px 20px;
        text-decoration: none;
        font-weight: 600;
        letter-spacing: 1px;
        border-radius: 4px;
        margin-top: 20px;
        transition: 0.3s;
    }
    .btn-contato:hover {
        background-color: #333333;
        transform: translateY(-2px);
    }
    
    /* Ajuste de textos */
    .titulo { text-align: center; font-weight: 600; font-size: 2.8rem; color: #111; margin-bottom: 0; padding-bottom: 0; }
    .subtitulo { text-align: center; font-weight: 300; font-size: 1.1rem; color: #666; margin-top: 5px; }
    .legenda { font-size: 0.85rem; color: #777; margin-top: -10px; margin-bottom: 20px; text-align: center; display: block; }
    .nome-projeto { font-size: 1rem; font-weight: 600; color: #222; text-align: center; margin-bottom: 0; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='titulo'>PALLADIUM STUDIO</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Visualização 3D de Alto Padrão para Móveis Planejados</div>", unsafe_allow_html=True)
st.write("---")

# --- GALERIA RESPONSIVA ---
# O Streamlit automaticamente coloca lado a lado no PC e empilha no Celular
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1599619369931-6e3e57088b39?q=80&w=800&auto=format&fit=crop", use_container_width=True)
    st.markdown("<span class='nome-projeto'>Cozinha Minimalista</span>", unsafe_allow_html=True)
    st.markdown("<span class='legenda'>MDF Amadeirado e Iluminação LED</span>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1618219985960-496e579bd66c?q=80&w=800&auto=format&fit=crop", use_container_width=True)
    st.markdown("<span class='nome-projeto'>Home Theater</span>", unsafe_allow_html=True)
    st.markdown("<span class='legenda'>Detalhes em Laca Premium</span>", unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1618219944342-824e40a13285?q=80&w=800&auto=format&fit=crop", use_container_width=True)
    st.markdown("<span class='nome-projeto'>Suíte Master</span>", unsafe_allow_html=True)
    st.markdown("<span class='legenda'>Painel Ripado e Cabeceira</span>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a?q=80&w=800&auto=format&fit=crop", use_container_width=True)
    st.markdown("<span class='nome-projeto'>Área Gourmet</span>", unsafe_allow_html=True)
    st.markdown("<span class='legenda'>Integração com Marcenaria Externa</span>", unsafe_allow_html=True)

with col3:
    st.image("https://images.unsplash.com/photo-1618219961917-d266e76d9101?q=80&w=800&auto=format&fit=crop", use_container_width=True)
    st.markdown("<span class='nome-projeto'>Home Office</span>", unsafe_allow_html=True)
    st.markdown("<span class='legenda'>Espaço Corporativo Funcional</span>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1603912975949-c1e1e0a29363?q=80&w=800&auto=format&fit=crop", use_container_width=True)
    st.markdown("<span class='nome-projeto'>Banheiro Premium</span>", unsafe_allow_html=True)
    st.markdown("<span class='legenda'>Gabinete em Acabamento Realista</span>", unsafe_allow_html=True)

st.write("---")

# --- ÁREA DE CONVERSÃO E CONTATO ---
st.markdown("<h3 style='text-align: center; color: #111;'>Apresente seus projetos com a qualidade que eles merecem.</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555; max-width: 800px; margin: 0 auto;'>Entendemos de chapas, encaixes e da linguagem técnica da marcenaria. Usamos texturas dos catálogos originais (Guararapes, Arauco) para o seu cliente aprovar mais rápido e sem dúvidas.</p>", unsafe_allow_html=True)

# Centraliza o botão no desktop e deixa do tamanho certo no mobile
_, col_btn, _ = st.columns([1, 2, 1])

with col_btn:
    link_wpp = "https://wa.me/5514998405046?text=Ol%C3%A1!%20Vi%20o%20portf%C3%B3lio%20do%20Palladium%20Studio%20e%20gostaria%20de%20fazer%20um%20or%C3%A7amento."
    st.markdown(f'<a href="{link_wpp}" target="_blank" class="btn-contato">SOLICITAR ORÇAMENTO</a>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; font-size: 12px; color: gray;'>Palladium Studio © 2026 | Ourinhos - SP</p>", unsafe_allow_html=True)
