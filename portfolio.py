import streamlit as st

# Configuração da página - Wide ajuda a criar layouts melhores
st.set_page_config(page_title="Palladium Studio | Marcenaria 3D", page_icon="🏛️", layout="wide")

# --- CSS INJETADO (Visual Premium + RESPONSIVIDADE CELULAR) ---
st.markdown("""
    <style>
    /* Importando fonte minimalista e elegante */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
        background-color: #FFFFFF;
    }

    /* Escondendo ferramentas padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Configuração de Títulos e Textos */
    h1 { color: #1A1A1A; font-weight: 600; letter-spacing: 2px; }
    h2, h3 { color: #1A1A1A; font-weight: 400; margin-top: 1.5rem; }
    p { color: #444; line-height: 1.6; }

    /* Estilo Premium para Imagens e Galeria */
    .stImage img {
        border-radius: 4px;
        transition: transform 0.3s ease;
    }
    .stImage img:hover {
        transform: scale(1.02);
    }
    .stMarkdown div p { /* Legendas das imagens */
        font-size: 0.9rem;
        color: #666;
        text-align: center;
        margin-top: -10px;
        padding-bottom: 1rem;
    }

    /* Botão Premium (WhatsApp) */
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

    /* ========================================= */
    /* === REGRAS DE RESPONSIVIDADE (CELULAR) === */
    /* ========================================= */
    
    /* Quando a tela for menor que 768px (maioria dos celulares) */
    @media (max-width: 767px) {
        /* Força as colunas (stHorizontalBlock) a se empilharem */
        div[data-testid="stHorizontalBlock"] {
            display: flex;
            flex-direction: column !important;
        }
        
        /* Garante que cada elemento dentro da coluna ocupe 100% da largura */
        div[data-testid="stHorizontalBlock"] > div {
            width: 100% !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
            padding-bottom: 1rem;
        }

        /* Ajusta o tamanho do título principal no celular */
        h1 {
            font-size: 2.2rem !important;
            text-align: center;
        }
        .subtitle {
            font-size: 1rem !important;
            text-align: center;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER / TOPO DO SITE ---
st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom:0;'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle' style='text-align: center; font-size: 1.2rem; color: #666; font-weight: 300; margin-top:0;'>VISUALIZAÇÃO 3D ESPECIALIZADA EM MÓVEIS PLANEJADOS</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- GALERIA ESPECIALIZADA EM MARCENARIA (6 Projetos) ---
st.header("🖼️ Portfólio de Projetos Planejados")
st.write("Renders de alta fidelidade que valorizam o detalhamento da marcenaria e texturas reais.")
st.markdown("<br>", unsafe_allow_html=True)

# Lembrete: Para usar suas próprias imagens, suba os arquivos (.jpg) no mesmo repositório do GitHub
# E substitua o link abaixo pelo nome do arquivo: st.image("sua_cozinha.jpg")

# LINHA 1 DA GALERIA
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.unsplash.com/photo-1599619369931-6e3e57088b39?q=80&w=1200&auto=format&fit=crop", 
             caption="Cozinha Planejada Minimalista - Textura Amadeirada e LED")
with col2:
    st.image("https://images.unsplash.com/photo-1618219944342-824e40a13285?q=80&w=1200&auto=format&fit=crop", 
             caption="Suíte Master - Painel Ripado e Closet Integrado")

# LINHA 2 DA GALERIA
col3, col4 = st.columns(2)
with col3:
    st.image("https://images.unsplash.com/photo-1618219985960-496e579bd66c?q=80&w=1200&auto=format&fit=crop", 
             caption="Home Theater - Detalhes em Laca e Vidro Reflecta")
with col4:
    st.image("https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a?q=80&w=1200&auto=format&fit=crop", 
             caption="Área Gourmet Planejada - Integração com Churrasqueira")

# LINHA 3 DA GALERIA
col5, col6 = st.columns(2)
with col5:
    st.image("https://images.unsplash.com/photo-1618219961917-d266e76d9101?q=80&w=1200&auto=format&fit=crop", 
             caption="Escritório Home Office - Marcenaria Funcional")
with col6:
    st.image("https://images.unsplash.com/photo-1603912975949-c1e1e0a29363?q=80&w=1200&auto=format&fit=crop", 
             caption="Banheiro Premium - Gabinete Planejado e Cubas Esculpidas")

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# --- SEÇÃO DE DIFERENCIAL E CONTATO ---
col_texto, col_botao = st.columns([2, 1])

with col_texto:
    st.subheader("Entendemos a Linguagem da Marcenaria")
    st.write("""
    Nós sabemos que um render para marceneiro precisa mostrar mais do que 'ambiente bonito'. 
    Focamos no realismo das **texturas reais dos catálogos** (Arauco, Guararapes, Duratex), na 
    **proporção correta** dos móveis e no detalhamento que ajuda seu cliente final a aprovar o projeto 
    sem dúvidas. Aumente seu índice de fechamento de contratos com Palladium Studio.
    """)

with col_botao:
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("📍 **Base:** Ourinhos - SP")
    st.write("📱 **WhatsApp:** (14) 99840-5046")
    
    # Criando o link direto para o seu WhatsApp com uma mensagem pré-pronta
    link_wpp = "https://wa.me/5514998405046?text=Ol%C3%A1!%20Vi%20o%20portf%C3%B3lio%20do%20Palladium%20Studio%20e%20gostaria%20de%20fazer%20um%20or%C3%A7amento."
    
    # Estilizando o link para parecer o mesmo botão premium
    st.markdown(f"""
        <a href="{link_wpp}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #1A1A1A; color: white; text-align: center; padding: 12px 24px; border-radius: 2px; font-weight: 600; letter-spacing: 1px; width: 100%;">
                SOLICITAR ORÇAMENTO
            </div>
        </a>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br><center><p style='color: #999; font-size: 0.8rem;'>PALLADIUM STUDIO © 2026 | Visualização 3D para Móveis Planejados</p></center>", unsafe_allow_html=True)
