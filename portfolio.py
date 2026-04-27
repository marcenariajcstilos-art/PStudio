import streamlit as st

# Configuração da página (mantém o layout largo)
st.set_page_config(page_title="Palladium Studio | ArchViz", page_icon="🏛️", layout="wide")

# --- CSS INJETADO (A mágica do visual premium) ---
st.markdown("""
    <style>
    /* Importando fonte minimalista e elegante do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');

    /* Aplicando a fonte em todo o site e definindo um fundo limpo */
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
    }

    /* Escondendo as ferramentas padrão do Streamlit para parecer um site nativo */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Deixando os botões com cara de botão de compra de site de luxo */
    .stButton>button {
        background-color: #1A1A1A;
        color: #FFFFFF;
        border: 1px solid #1A1A1A;
        border-radius: 2px;
        padding: 12px 24px;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease 0s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #FFFFFF;
        color: #1A1A1A;
        border: 1px solid #1A1A1A;
    }

    /* Melhorando a cor e peso dos títulos */
    h1, h2, h3 {
        color: #1A1A1A;
        font-weight: 600;
    }
    
    /* Espaçamento extra no topo */
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER / TOPO DO SITE ---
st.markdown("<h1 style='text-align: center; font-size: 3.5rem; letter-spacing: 2px;'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #666; font-weight: 300;'>VISUALIZAÇÃO ARQUITETÔNICA DE ALTO PADRÃO</p>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# --- GALERIA PREMIUM ---
st.subheader("Projetos em Destaque")
st.write("Especialidade em interiores residenciais e fachadas comerciais com realismo extremo.")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Substitua as URLs das imagens pelas URLs dos seus renders verdadeiros (você pode hospedar as imagens no próprio GitHub)
with col1:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=1200&auto=format&fit=crop", 
             caption="Integração de Ambientes - Iluminação Natural")
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1556910103-1c02745aae4d?q=80&w=1200&auto=format&fit=crop", 
             caption="Cozinha Planejada - Detalhamento de Marcenaria")

with col2:
    st.image("https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?q=80&w=1200&auto=format&fit=crop", 
             caption="Living Premium - Texturas de Alto Padrão")
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?q=80&w=1200&auto=format&fit=crop", 
             caption="Fachada Residencial - Renderização Noturna")

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# --- SEÇÃO DE VALOR E CONTATO ---
col_texto, col_botao = st.columns([2, 1])

with col_texto:
    st.subheader("Entendemos a Linguagem da Marcenaria")
    st.write("""
    Um bom render não é apenas uma imagem bonita, é uma ferramenta de vendas. 
    Trabalhamos com os catálogos reais do mercado e modelagem precisa para que o cliente final 
    aprove o projeto mais rápido, sem dúvidas sobre acabamentos ou proporções de pedras e pedras, como granito São Gabriel ou similares.
    """)

with col_botao:
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("📍 **Base:** Ourinhos - SP (Atendimento Nacional)")
    
    # Criando o link direto para o seu WhatsApp com uma mensagem pré-pronta
    link_wpp = "https://wa.me/5514998405046?text=Ol%C3%A1!%20Vi%20o%20portf%C3%B3lio%20do%20Palladium%20Studio%20e%20gostaria%20de%20fazer%20um%20or%C3%A7amento."
    
    st.markdown(f"""
        <a href="{link_wpp}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #1A1A1A; color: white; text-align: center; padding: 12px 24px; border-radius: 2px; font-weight: 600; letter-spacing: 1px;">
                SOLICITAR ORÇAMENTO
            </div>
        </a>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br><center><p style='color: #999; font-size: 0.8rem;'>PALLADIUM STUDIO © 2026</p></center>", unsafe_allow_html=True)
