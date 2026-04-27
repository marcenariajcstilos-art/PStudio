import streamlit as st
import time

# ==========================================
# 1. CONFIGURAÇÃO BASE DO SISTEMA
# ==========================================
st.set_page_config(
    page_title="Palladium Studio | ArchViz Premium",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. MOTOR DE ESTILIZAÇÃO CSS (FRAMEWORK VISUAL)
# ==========================================
def injetar_css_premium():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --bg-color: #0d0d0d;
            --text-main: #f2f2f2;
            --text-muted: #888888;
            --accent: #d4af37; 
            --card-bg: #1a1a1a;
            --border: #222222;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color) !important;
            color: var(--text-main) !important;
        }

        #MainMenu, header, footer {visibility: hidden;}

        h1, h2, h3 {
            font-family: 'Cinzel', serif !important;
            font-weight: 600 !important;
            color: #ffffff !important;
        }

        .hero-title {
            font-size: 4.5rem !important;
            text-align: center;
            background: -webkit-linear-gradient(45deg, #ffffff, #d4af37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0;
        }
        .hero-subtitle {
            font-size: 1.2rem;
            text-align: center;
            color: var(--text-muted);
            font-weight: 300;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-top: 10px;
            margin-bottom: 40px;
        }

        .project-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 15px;
            transition: all 0.4s ease;
            margin-bottom: 25px;
            cursor: pointer;
        }
        .project-card:hover {
            transform: translateY(-10px);
            border-color: var(--accent);
            box-shadow: 0 10px 30px rgba(212, 175, 55, 0.05);
        }
        .project-title {
            font-family: 'Cinzel', serif;
            font-size: 1.4rem;
            margin-top: 15px;
            margin-bottom: 5px;
            color: var(--accent);
        }
        .project-desc { font-size: 0.9rem; color: var(--text-muted); line-height: 1.5; }
        .project-tags {
            font-size: 0.75rem; color: #aaaaaa; background: #111;
            padding: 4px 8px; border-radius: 4px; display: inline-block;
            margin-top: 10px; margin-right: 5px; border: 1px solid #333;
        }

        /* --- NOVO ESTILO DA SIDEBAR --- */
        [data-testid="stSidebar"] {
            background-color: #050505 !important;
            border-right: 1px solid var(--border);
        }
        [data-testid="stSidebar"] h1 {
            color: var(--accent) !important;
            text-align: center;
            font-size: 2rem !important;
            margin-top: 10px;
        }

        /* Estilo dos botões gerais da página (ex: "Ver Portfólio") */
        .stButton>button {
            background-color: transparent !important;
            color: var(--accent) !important;
            border: 1px solid var(--accent) !important;
            border-radius: 0px !important;
            padding: 15px 30px !important;
            font-family: 'Inter', sans-serif;
            font-weight: 500 !important;
            letter-spacing: 2px;
            text-transform: uppercase;
            width: 100%;
            transition: all 0.3s ease !important;
        }
        .stButton>button:hover {
            background-color: var(--accent) !important;
            color: #000000 !important;
        }

        /* ESTILO EXCLUSIVO PARA OS BOTÕES DA SIDEBAR (MINIMALISTAS) */
        [data-testid="stSidebar"] .stButton>button {
            background-color: transparent !important;
            color: #aaaaaa !important;
            border: none !important;
            border-left: 3px solid transparent !important; /* Borda invisível para manter alinhamento */
            text-align: left !important;
            padding: 10px 15px !important;
            font-size: 0.95rem !important;
            letter-spacing: 3px;
            display: flex;
            justify-content: flex-start;
        }
        [data-testid="stSidebar"] .stButton>button:hover {
            background-color: transparent !important;
            color: #ffffff !important;
            border-left: 3px solid var(--accent) !important; /* Destaque lateral elegante */
            transform: translateX(8px); /* Efeito de empurrar o texto levemente */
            box-shadow: none !important;
        }
        [data-testid="stSidebar"] p {
            margin-bottom: 0 !important;
        }

        .streamlit-expanderHeader {
            font-family: 'Inter', sans-serif !important;
            font-weight: 500 !important; color: #ffffff !important;
            background-color: var(--card-bg) !important; border: 1px solid var(--border) !important;
        }
        hr { border-color: #222222 !important; margin: 40px 0 !important; }
        .stat-box {
            text-align: center; padding: 20px; background: #0a0a0a;
            border: 1px solid #222; border-radius: 4px;
        }
        .stat-number { font-family: 'Cinzel', serif; font-size: 3rem; color: var(--accent); margin:0;}
        .stat-label { font-size: 0.9rem; color: #666; text-transform: uppercase; letter-spacing: 1px;}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. BANCO DE DADOS SIMULADO (ESTRUTURA DE DADOS)
# ==========================================
def carregar_banco_dados():
    return [
        {
            "id": 1,
            "titulo": "Cozinha Gourmet Integrada",
            "categoria": "Cozinha",
            "imagem": "https://images.unsplash.com/photo-1599619369931-6e3e57088b39?q=80&w=1200&auto=format&fit=crop",
            "descricao": "Projeto de integração total. Modelagem precisa da marcenaria para garantir vãos exatos de eletrodomésticos.",
            "materiais": ["MDF Arauco", "Granito São Gabriel", "Vidro Reflecta"],
            "software": "SketchUp + V-Ray",
            "destaque": True
        },
        {
            "id": 2,
            "titulo": "Suíte Master com Ripado",
            "categoria": "Dormitório",
            "imagem": "https://images.unsplash.com/photo-1618219944342-824e40a13285?q=80&w=1200&auto=format&fit=crop",
            "descricao": "Estudo de iluminação artificial em fitas de LED embutidas no painel ripado da cabeceira.",
            "materiais": ["MDF Guararapes", "Laca Fosca", "Fita LED 3000K"],
            "software": "3ds Max + Corona",
            "destaque": True
        },
        {
            "id": 3,
            "titulo": "Fachada Comercial Modernista",
            "categoria": "Fachada",
            "imagem": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?q=80&w=1200&auto=format&fit=crop",
            "descricao": "Renderização externa com foco em volumetria e materiais rústicos aplicados à fachada.",
            "materiais": ["Aço Corten", "Concreto Aparente", "Esquadrias Pretas"],
            "software": "SketchUp + V-Ray + Chaos Cloud",
            "destaque": False
        },
        {
            "id": 4,
            "titulo": "Living de Alto Padrão",
            "categoria": "Sala de Estar",
            "imagem": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?q=80&w=1200&auto=format&fit=crop",
            "descricao": "Home theater planejado com painel de TV em pedra natural e marcenaria de apoio oculta.",
            "materiais": ["Mármore Calacatta", "MDF Carvalho", "Laca Branca Brilhante"],
            "software": "3ds Max + V-Ray",
            "destaque": True
        },
        {
            "id": 5,
            "titulo": "Home Office Corporativo",
            "categoria": "Escritório",
            "imagem": "https://images.unsplash.com/photo-1618219961917-d266e76d9101?q=80&w=1200&auto=format&fit=crop",
            "descricao": "Otimização de espaço para trabalho híbrido, com estante iluminada e mesa flutuante.",
            "materiais": ["MDF Preto Silk", "Aço Carbono", "Couro"],
            "software": "SketchUp + Enscape",
            "destaque": False
        },
        {
            "id": 6,
            "titulo": "Banheiro Spa Residencial",
            "categoria": "Banheiro",
            "imagem": "https://images.unsplash.com/photo-1603912975949-c1e1e0a29363?q=80&w=1200&auto=format&fit=crop",
            "descricao": "Gabinete suspenso planejado para resistir à umidade, com cuba dupla esculpida.",
            "materiais": ["Porcelanato Marmorizado", "MDF Ultra", "Metais Gold"],
            "software": "SketchUp + V-Ray",
            "destaque": False
        }
    ]

# ==========================================
# 4. MÓDULOS DE RENDERIZAÇÃO DE PÁGINAS
# ==========================================

def render_home(db):
    """Página inicial com Hero Section e destaques"""
    st.markdown("<h1 class='hero-title'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>A Arte da Visualização Arquitetônica</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; max-width: 800px; margin: 0 auto; color: #aaa; font-size: 1.1rem; line-height: 1.6;'>
            Elevamos o padrão de apresentação de marcenarias e escritórios de arquitetura. 
            Nossos renders não são apenas imagens bonitas; são ferramentas de conversão 
            construídas com fidelidade técnica, respeitando modulações e catálogos reais da indústria.
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # Métricas de Autoridade
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='stat-box'><p class='stat-number'>4K+</p><p class='stat-label'>Resolução de Entrega</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='stat-box'><p class='stat-number'>100%</p><p class='stat-label'>Fidelidade de Materiais</p></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='stat-box'><p class='stat-number'>24h</p><p class='stat-label'>Prévias Volumétricas</p></div>", unsafe_allow_html=True)
    
    st.write("---")
    
    # Vitrine de Projetos em Destaque
    st.markdown("<h2 style='text-align: center; color: #d4af37 !important;'>Projetos em Destaque</h2><br>", unsafe_allow_html=True)
    destaques = [p for p in db if p['destaque']]
    
    cols = st.columns(3)
    for i, proj in enumerate(destaques):
        with cols[i % 3]:
            tags_html = "".join([f"<span class='project-tags'>{t}</span>" for t in proj['materiais']])
            st.markdown(f"""
                <div class='project-card'>
                    <img src='{proj["imagem"]}' style='width: 100%; border-radius: 4px; aspect-ratio: 4/3; object-fit: cover;'>
                    <h3 class='project-title'>{proj["titulo"]}</h3>
                    <p class='project-desc'>{proj["descricao"]}</p>
                    <div style='margin-top: 15px;'>{tags_html}</div>
                </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        if st.button("VER PORTFÓLIO COMPLETO"):
            st.session_state['page'] = 'Portfólio'
            st.rerun()

def render_portfolio(db):
    """Página de portfólio com sistema de filtros dinâmico"""
    st.markdown("<h2>Galeria de Projetos</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>Filtre os ambientes para encontrar a referência ideal para o seu cliente.</p>", unsafe_allow_html=True)
    
    # Coleta categorias únicas
    categorias = ["Todos"] + sorted(list(set([p["categoria"] for p in db])))
    
    # Layout de filtro
    col_filtro, _ = st.columns([1, 3])
    with col_filtro:
        filtro_selecionado = st.selectbox("Filtrar por Ambiente:", categorias)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Aplica filtro
    projetos_filtrados = db if filtro_selecionado == "Todos" else [p for p in db if p["categoria"] == filtro_selecionado]
    
    if not projetos_filtrados:
        st.warning("Nenhum projeto encontrado para esta categoria.")
        return

    # Renderiza galeria em grid
    cols = st.columns(2) # Usando 2 colunas para imagens maiores no portfólio
    for i, proj in enumerate(projetos_filtrados):
        with cols[i % 2]:
            tags_html = "".join([f"<span class='project-tags'>{t}</span>" for t in proj['materiais']])
            st.markdown(f"""
                <div class='project-card'>
                    <img src='{proj["imagem"]}' style='width: 100%; border-radius: 4px; aspect-ratio: 16/9; object-fit: cover;'>
                    <h3 class='project-title'>{proj["titulo"]}</h3>
                    <p style='color: #d4af37; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;'>{proj["categoria"]} | {proj["software"]}</p>
                    <p class='project-desc'>{proj["descricao"]}</p>
                    <div style='margin-top: 10px;'>{tags_html}</div>
                </div>
            """, unsafe_allow_html=True)

def render_about():
    """Página sobre o estúdio e metodologia"""
    st.markdown("<h2>Nossa Essência</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
            <div style='color: #aaa; font-size: 1.1rem; line-height: 1.8; padding-right: 30px;'>
                <p>O Palladium Studio não é apenas um escritório de visualização arquitetônica. Nós somos a ponte entre a prancheta de design e a linha de produção da marcenaria.</p>
                
                <p><b>A Vantagem da Execução Real:</b> Diferente de artistas 3D que criam imagens bonitas porém impossíveis de fabricar, nossa base possui DNA de marcenaria de alto padrão. 
                Cada espessura de chapa, cada detalhe de tamponamento e cada textura aplicada (como os padrões Arauco, Guararapes e Duratex) são configurados com especificações técnicas reais.</p>
                
                <p>Nós renderizamos usando tecnologia de ponta (V-Ray e Chaos Cloud) para garantir que o projeto seja aprovado pelo cliente final na primeira reunião, reduzindo o tempo de negociação e aumentando o valor percebido do seu trabalho.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div style='background: #111; border: 1px solid #333; padding: 30px; border-radius: 8px;'>
                <h3 style='color: #d4af37 !important; font-size: 1.2rem !important;'>Fluxo de Trabalho</h3>
                <hr style='margin: 10px 0 !important;'>
                <ul style='color: #888; line-height: 2; padding-left: 20px;'>
                    <li>Recepção do modelo (SketchUp, Promob ou DWG)</li>
                    <li>Otimização de Malha e Setup de Câmeras</li>
                    <li>Mapeamento Realista PBR (Texturas Hign-End)</li>
                    <li>Estudo Luminotécnico Global</li>
                    <li>Renderização Final via Cloud Render</li>
                    <li>Pós-produção em Photoshop</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

def render_contact():
    """Página de contato com FAQ e redirecionamento de WhatsApp"""
    st.markdown("<h2>Vamos Conversar</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>Pronto para elevar o nível das suas apresentações? Fale com a nossa equipe.</p>", unsafe_allow_html=True)
    
    col_form, col_faq = st.columns([1, 1])
    
    with col_form:
        st.markdown("""
            <div style='background: #111; border: 1px solid #333; padding: 30px; border-radius: 8px; margin-bottom: 20px;'>
                <h3 style='font-size: 1.2rem !important;'>Informações Diretas</h3>
                <p style='color: #aaa;'>📍 Atendimento Nacional (Base em Ourinhos - SP)</p>
                <p style='color: #aaa;'>📱 (14) 99840-5046</p>
                <p style='color: #aaa;'>✉️ projetos@palladiumstudio.com</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='font-size: 1.2rem !important; margin-top: 30px;'>Solicitar Orçamento Rápido</h3>", unsafe_allow_html=True)
        # Formulário Simulado para envio ao WhatsApp
        tipo_projeto = st.selectbox("Qual o tipo de projeto?", ["Residencial Completo", "Ambiente Único (Cozinha/Quarto)", "Fachada Comercial", "Planta Humanizada"])
        urgencia = st.radio("Prazo de Entrega:", ["Normal (3-5 dias)", "Urgente (48h)"])
        
        link_base = "https://wa.me/5514998405046?text="
        msg_montada = f"Olá, Palladium Studio. Tenho interesse em terceirizar um render de *{tipo_projeto}*. Prazo desejado: *{urgencia}*. Podemos conversar sobre valores?"
        link_final = link_base + msg_montada.replace(" ", "%20").replace("&", "%26")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'<a href="{link_final}" target="_blank" style="text-decoration:none;"><button style="width:100%; background:#d4af37; color:#000; font-weight:bold; border:none; padding:15px; border-radius:4px; cursor:pointer; font-family:Inter; letter-spacing:1px; text-transform:uppercase;">Chamar no WhatsApp</button></a>', unsafe_allow_html=True)

    with col_faq:
        st.markdown("<h3 style='font-size: 1.2rem !important;'>Perguntas Frequentes</h3>", unsafe_allow_html=True)
        
        with st.expander("Vocês modelam o projeto do zero?"):
            st.write("Trabalhamos de duas formas. O ideal é receber o seu 3D base (SketchUp, Promob exportado) para focar apenas na iluminação e render. Mas também realizamos a modelagem técnica caso você envie apenas a planta baixa ou croqui com medidas.")
            
        with st.expander("Como é feita a cobrança?"):
            st.write("Cobramos por ambiente ou pacote de imagens. Por exemplo, uma cozinha fechada com 3 ângulos (câmeras) tem um valor fixo. O pagamento padrão é 50% no aceite e 50% na entrega final em alta resolução.")
            
        with st.expander("Posso pedir alterações?"):
            st.write("Sim! O nosso pacote padrão inclui até 2 rodadas de revisões gratuitas. Nelas, enviamos prévias em baixa resolução para você aprovar o ângulo da câmera, iluminação e texturas antes do processamento final.")
            
        with st.expander("Qual a resolução de entrega das imagens?"):
            st.write("Entregamos por padrão em resolução 4K (3840 x 2160 pixels), ideal para impressão de portfólio físico, apresentações em telas grandes ou uso em redes sociais com máxima nitidez.")

def render_footer():
    """Rodapé universal do sistema"""
    st.markdown("""
        <hr>
        <div style='text-align: center; color: #555; padding: 20px; font-size: 0.85rem;'>
            <p style='font-family: Cinzel, serif; font-size: 1.2rem; color: #777; margin-bottom: 5px;'>PALLADIUM STUDIO</p>
            <p>Visualização Arquitetônica & Design Estratégico para Marcenarias</p>
            <p>Ourinhos, SP • Brasil © 2026</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 5. CONTROLADOR DE ROTAS (MAIN LOOP)
# ==========================================
def main():
    injetar_css_premium()
    db = carregar_banco_dados()
    
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Início'
        
    with st.sidebar:
        st.markdown("<h1>PALLADIUM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#555; font-size:0.75rem; letter-spacing:4px; margin-top:-15px; margin-bottom:40px;'>STUDIO</p>", unsafe_allow_html=True)
        
        # Botões refeitos: sem emojis, focando na tipografia
        if st.button("INÍCIO"): st.session_state['page'] = 'Início'
        if st.button("PORTFÓLIO"): st.session_state['page'] = 'Portfólio'
        if st.button("METODOLOGIA"): st.session_state['page'] = 'Sobre'
        if st.button("CONTATO"): st.session_state['page'] = 'Contato'
        
        # Texto de versão reestruturado para não encavalar
        st.markdown("""
            <div style='margin-top: 80px; text-align: center; color: #333; font-size: 0.70rem; letter-spacing: 1px;'>
                ARCHVIZ SYSTEM v2.5<br>
                RENDER ENGINE: ONLINE
            </div>
        """, unsafe_allow_html=True)

    page = st.session_state['page']
    
    with st.container():
        st.markdown("<div style='padding: 2% 5%;'>", unsafe_allow_html=True)
        if page == 'Início': render_home(db)
        elif page == 'Portfólio': render_portfolio(db)
        elif page == 'Sobre': render_about()
        elif page == 'Contato': render_contact()
        st.markdown("</div>", unsafe_allow_html=True)
        
    render_footer()

if __name__ == "__main__":
    main()
