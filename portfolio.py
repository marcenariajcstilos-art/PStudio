import streamlit as st
import time

# ==============================================================================
# 1. CONFIGURAÇÃO DE AMBIENTE
# ==============================================================================
st.set_page_config(
    page_title="Palladium Studio | Premium ArchViz",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'page' not in st.session_state:
    st.session_state['page'] = 'Início'
if 'projeto_selecionado' not in st.session_state:
    st.session_state['projeto_selecionado'] = None

# ==============================================================================
# 2. MOTOR VISUAL PREMIUM E INJEÇÃO DE CSS
# ==============================================================================
def injetar_css_premium():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --bg-color: #080808;
            --text-main: #f2f2f2;
            --text-muted: #888888;
            --accent: #d4af37; 
            --card-bg: #111111;
            --border: #222222;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color) !important;
            color: var(--text-main) !important;
        }

        #MainMenu, header, footer {visibility: hidden;}

        h1, h2, h3, h4 {
            font-family: 'Cinzel', serif !important;
            font-weight: 600 !important;
            color: #ffffff !important;
            letter-spacing: 1px;
        }

        /* --- CARDS DE PROJETOS --- */
        .project-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 6px;
            padding: 0px;
            transition: all 0.4s ease;
            margin-bottom: 30px;
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        .project-card:hover {
            border-color: var(--accent);
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(212, 175, 55, 0.08);
        }
        .img-container {
            width: 100%;
            aspect-ratio: 16/9;
            overflow: hidden;
            background: #1a1a1a;
        }
        .img-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 1.2s ease;
        }
        .project-card:hover img { transform: scale(1.05); }
        .card-content { padding: 25px; display: flex; flex-direction: column; flex-grow: 1; }
        .project-title { font-family: 'Cinzel', serif; font-size: 1.2rem; color: var(--accent); margin-bottom: 10px; }
        .project-desc { font-size: 0.9rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 15px; flex-grow: 1; }

        /* --- SIDEBAR CUSTOMIZADA --- */
        [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 1px solid var(--border); }
        [data-testid="stSidebar"] .stButton>button {
            background-color: transparent !important; color: #666 !important;
            border: none !important; border-left: 3px solid transparent !important;
            text-align: left !important; padding: 15px 25px !important;
            font-size: 0.9rem !important; letter-spacing: 3px; transition: 0.3s;
            width: 100%; justify-content: flex-start;
        }
        [data-testid="stSidebar"] .stButton>button:hover {
            color: #fff !important; border-left: 3px solid var(--accent) !important;
            background-color: #0a0a0a !important; transform: translateX(5px);
        }

        /* --- BOTÕES PREMIUM --- */
        .btn-gold {
            display: block; background: var(--accent); color: #000 !important;
            text-align: center; padding: 18px 25px; font-weight: 700;
            letter-spacing: 2px; text-decoration: none; text-transform: uppercase;
            transition: 0.4s; border-radius: 3px; border: 1px solid var(--accent);
        }
        .btn-gold:hover { background: #fff; border-color: #fff; box-shadow: 0 0 25px rgba(212, 175, 55, 0.3); }
        
        .btn-outline {
            display: block; background: transparent; color: var(--accent) !important;
            text-align: center; padding: 18px 25px; font-weight: 600;
            letter-spacing: 2px; text-decoration: none; text-transform: uppercase;
            transition: 0.3s; border: 1px solid var(--accent); border-radius: 3px;
        }
        .btn-outline:hover { background: var(--accent); color: #000 !important; }

        /* --- TABELAS DE PREÇO --- */
        .pricing-card {
            background: #0d0d0d; border: 1px solid #333; padding: 40px 30px;
            text-align: center; border-radius: 8px; transition: 0.3s; height: 100%;
            display: flex; flex-direction: column;
        }
        .pricing-card:hover { border-color: var(--accent); background: #141414; transform: translateY(-5px); }
        .pricing-title { font-family: 'Cinzel', serif; color: #fff; font-size: 1.5rem; margin-bottom: 10px; }
        .pricing-subtitle { color: var(--accent); font-size: 0.9rem; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 25px; }
        .pricing-features {
            text-align: left; color: #aaa; line-height: 2.2; margin-bottom: 30px;
            font-size: 0.95rem; border-top: 1px solid #222; padding-top: 25px; flex-grow: 1;
        }
        .pricing-features span { color: var(--accent); margin-right: 10px; }

        button[title="View fullscreen"] { display: none; }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. BANCO DE DADOS RELACIONAL (URLs Estáveis)
# ==============================================================================
def carregar_banco_de_dados():
    interiores = [
        {"id": "INT-001", "titulo": "Cozinha Minimalista Nero", "categoria": "Cozinha", "estilo": "Minimalista", "descricao_curta": "MDF Preto Silk com iluminação embutida e puxadores cava discretos.", "descricao_longa": "Projeto desenvolvido para destacar o minimalismo. A marcenaria foi configurada com Preto Silk da Guararapes. Detalhe técnico exigido: os puxadores são cava, integrados e totalmente invisíveis, garantindo a linha contínua do design. Iluminação cenográfica em perfis de LED 3000K.", "materiais": ["MDF Preto Silk", "Puxador Cava", "Perfis LED"], "software": "SketchUp + V-Ray", "tempo_render": "3h", "img": "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-002", "titulo": "Suíte Master com Ripado", "categoria": "Dormitório", "estilo": "Contemporâneo", "descricao_curta": "Painel amadeirado ripado, laca cinza e cabeceira estofada em linho.", "descricao_longa": "Suíte master projetada para máximo conforto visual. Painel ripado em MDF Freijó Puro da Arauco, com espaçamento técnico de 15mm. Cabeceira estofada em linho cru com iluminação wall washer.", "materiais": ["MDF Freijó", "Laca Cinza Fosca", "Linho Cru"], "software": "3ds Max + Corona", "tempo_render": "5h", "img": "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-003", "titulo": "Living Contemporâneo", "categoria": "Living", "estilo": "Luxo Moderno", "descricao_curta": "Sala de pé-direito duplo com grandes aberturas e mobiliário de design.", "descricao_longa": "Living de pé-direito duplo que exige precisão volumétrica. O render tira partido da luz natural, estudando a interação do sol com o porcelanato polido. Marcenaria de apoio em painéis lisos de MDF Areia.", "materiais": ["MDF Areia", "Porcelanato Polido", "Vidro Laminado"], "software": "SketchUp + Enscape", "tempo_render": "1h", "img": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-004", "titulo": "Banheiro SPA em Mármore", "categoria": "Banheiro", "estilo": "Clássico", "descricao_curta": "Gabinete em MDF Branco Ultra com cuba esculpida em mármore.", "descricao_longa": "Sala de banho focada em relaxamento. Marcenaria técnica simulando MDF Ultra (resistente à umidade) com puxadores cava 45 graus. Configuração avançada de materiais translúcidos (Subsurface Scattering) no mármore Calacatta.", "materiais": ["Mármore Calacatta", "MDF Branco Ultra", "Puxador Cava"], "software": "3ds Max + Corona", "tempo_render": "6h", "img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-005", "titulo": "Gourmet Integrado", "categoria": "Área de Lazer", "estilo": "Industrial", "descricao_curta": "Churrasqueira com marcenaria em tons grafite e madeira de demolição.", "descricao_longa": "Integração de churrasco com o living interno. Marcenaria simulando MDF Grafite da Duratex. Destaque para a iluminação diurna (HDRI) que invade o ambiente projetando sombras na mesa rústica.", "materiais": ["MDF Grafite", "Madeira Maciça", "Cimento Queimado"], "software": "3ds Max + V-Ray", "tempo_render": "4h", "img": "https://images.unsplash.com/photo-1565538810643-b5bdb714032a?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-006", "titulo": "Home Office Corporativo", "categoria": "Escritório", "estilo": "Corporativo", "descricao_curta": "Estante com nichos iluminados e mesa flutuante.", "descricao_longa": "Espaço otimizado para conferências. A estante mistura nichos em Laca Preta e abertos em MDF Carvalho Hannover. Modelagem detalhada incluindo fiação invisível e textura de couro.", "materiais": ["Laca Preta", "MDF Carvalho", "Couro"], "software": "SketchUp + V-Ray Cloud", "tempo_render": "45m", "img": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-007", "titulo": "Closet Iluminado", "categoria": "Dormitório", "estilo": "Boutique", "descricao_curta": "Divisórias em MDF cinza, portas em vidro reflecta e cabideiros em LED.", "descricao_longa": "Closet estilo boutique. Proteção feita com esquadrias pretas e Vidro Reflecta Bronze. Marcenaria interna paginada rigorosamente no 3D para otimizar cortes das chapas.", "materiais": ["Vidro Reflecta", "MDF Cinza Sagrado", "Alumínio"], "software": "SketchUp + Enscape", "tempo_render": "1h 20m", "img": "https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-008", "titulo": "Sala de Jantar Elegance", "categoria": "Living", "estilo": "Clássico", "descricao_curta": "Buffet sob medida com portas em palhinha natural e tampo de pedra.", "descricao_longa": "Sala de jantar sofisticada. A marcenaria apresenta renderização realista da textura da palhinha indiana vazada usando mapas de Opacidade e Normal Bump.", "materiais": ["Palhinha Indiana", "MDF Nogueira", "Mármore"], "software": "SketchUp + V-Ray", "tempo_render": "4h 40m", "img": "https://images.unsplash.com/photo-1617806118233-18e16208a50a?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-009", "titulo": "Quarto Lúdico", "categoria": "Dormitório", "estilo": "Lúdico", "descricao_curta": "Marcenaria funcional com nichos e acabamentos curvos.", "descricao_longa": "Foco em ergonomia e segurança infantil. Render detalha cantos arredondados, simulando laca impecável. Cores pastéis configuradas com valores RGB exatos.", "materiais": ["Laca Pastel", "MDF Carvalho", "Algodão"], "software": "3ds Max + V-Ray", "tempo_render": "3h", "img": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-010", "titulo": "Adega Privativa", "categoria": "Área de Lazer", "estilo": "Rústico Moderno", "descricao_curta": "Nichos tipo colmeia para vinhos e climatização.", "descricao_longa": "Adega de alto padrão. Baixa luz exige algoritmos avançados de Denoising (IA) do V-Ray para limpar a imagem. Marcenaria simulada com lâminas de Cumaru.", "materiais": ["Madeira Cumaru", "Tijolo", "Vidro Duplo"], "software": "3ds Max + V-Ray", "tempo_render": "5h", "img": "https://images.unsplash.com/photo-1510626176961-4b57d4fbad03?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-011", "titulo": "Hall Minimal", "categoria": "Circulação", "estilo": "Minimalista", "descricao_curta": "Aparador suspenso slim e painel de espelhos bisotados.", "descricao_longa": "Lentes de 35mm utilizadas para evitar distorção em espaços pequenos. Aparador suspenso com gavetas de fecho-toque e parede de espelho para ampliar a passagem.", "materiais": ["MDF Lacca", "Espelho Prata", "Granito"], "software": "SketchUp + Corona", "tempo_render": "2h", "img": "https://images.unsplash.com/photo-1583847268964-b28dc2f51ac9?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-012", "titulo": "Lavanderia Organizada", "categoria": "Serviço", "estilo": "Funcional", "descricao_curta": "Armários aéreos totais e tulhas embutidas.", "descricao_longa": "Marcenaria técnica desenhada respeitando ventilação das máquinas. Simulação de MDF Branco Ártico, com rodapés em alumínio contra danos por água.", "materiais": ["MDF Branco", "Corian", "Alumínio"], "software": "SketchUp + Enscape", "tempo_render": "40m", "img": "https://images.unsplash.com/photo-1521783593447-5702b9bfd267?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-013", "titulo": "Biblioteca Clássica", "categoria": "Escritório", "estilo": "Clássico", "descricao_curta": "Estante pé-direito duplo com escada rolante metálica.", "descricao_longa": "Render utilizou instanciamento proxy para popular as estantes com livros 3D sem travar. Marcenaria renderizada usando textura de Carvalho Natural.", "materiais": ["MDF Carvalho", "Estrutura Metálica", "Piso Vinílico"], "software": "3ds Max + Corona", "tempo_render": "6h", "img": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-014", "titulo": "Recepção Clínica", "categoria": "Comercial", "estilo": "Comercial", "descricao_curta": "Balcão orgânico em curvas com filetes de LED.", "descricao_longa": "Balcão com curvas suaves revestidas em Fórmica Brilhante. Recuo com LED cria sensação de flutuação. Pós-produção focada em assepsia.", "materiais": ["Fórmica Branca", "MDF Claro", "Porcelanato"], "software": "SketchUp + V-Ray", "tempo_render": "2h", "img": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80"},
        {"id": "INT-015", "titulo": "Home Theater Foco Laca", "categoria": "Living", "estilo": "Moderno", "descricao_curta": "Painel de TV detalhado com laca brilho e iluminação zenital.", "descricao_longa": "Estudo avançado de reflexividade de materiais. A laca de alto brilho foi renderizada com múltiplas camadas de verniz no V-Ray para refletir a iluminação zenital corretamente.", "materiais": ["Laca Alto Brilho", "MDF Grafite", "Couro Preto"], "software": "3ds Max + V-Ray", "tempo_render": "4h 30m", "img": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=800&q=80"}
    ]

    exteriores = [
        {"id": "EXT-001", "titulo": "Residência Brises", "categoria": "Fachada", "estilo": "Contemporâneo", "descricao_curta": "Fachada com brises amadeirados e iluminação externa.", "descricao_longa": "Uso de brises verticais modelados individualmente para gerar sombras anguladas no pôr do sol. Vegetação renderizada com Chaos Cosmos.", "materiais": ["Brises Alumínio", "Concreto", "Esquadrias"], "software": "SketchUp + V-Ray", "tempo_render": "1h", "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-002", "titulo": "Área de Piscina", "categoria": "Área de Lazer", "estilo": "Tropical", "descricao_curta": "Deck em madeira natural nivelado com borda infinita.", "descricao_longa": "Foco na física da água. Cáusticas geradas pela luz do sol e mapeamento realista do deck de madeira Itaúba com imperfeições hiper-realistas.", "materiais": ["Madeira Itaúba", "Pastilha", "Mármore"], "software": "3ds Max + Corona", "tempo_render": "7h", "img": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-003", "titulo": "Corporativo Glass", "categoria": "Comercial", "estilo": "Corporativo", "descricao_curta": "Pele de vidro e perfis de alumínio no contexto urbano.", "descricao_longa": "Fachada em Pele de Vidro Refletivo exigiu modelagem de escritórios falsos internos. Asfalto realista com texturas PBR molhadas.", "materiais": ["Vidro Refletivo", "ACM Preto", "Concreto"], "software": "3ds Max + V-Ray", "tempo_render": "5h 45m", "img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-004", "titulo": "Casa de Campo", "categoria": "Fachada", "estilo": "Rústico", "descricao_curta": "Integração total com a natureza, pedras irregulares.", "descricao_longa": "Forest Pack utilizado para distribuir milhares de árvores e gramíneas sem travar. Mistura de madeira maciça e revestimento em pedra Moledo.", "materiais": ["Pedra Moledo", "Eucalipto", "Telha Shingle"], "software": "3ds Max + Corona", "tempo_render": "8h 30m", "img": "https://images.unsplash.com/photo-1500313830540-7b6650a74fd0?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-005", "titulo": "Rooftop Lounge", "categoria": "Área de Lazer", "estilo": "Urbano Moderno", "descricao_curta": "Mobiliário externo e vista skyline noturna.", "descricao_longa": "Exploração de iluminação noturna (Blue Hour), contrastando luzes frias da cidade com balizadores quentes na marcenaria de piso.", "materiais": ["Deck Sintético", "Corda Náutica", "Vidro Temperado"], "software": "SketchUp + Enscape", "tempo_render": "1h 15m", "img": "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-006", "titulo": "Entrada de Condomínio", "categoria": "Comercial", "estilo": "Imponente", "descricao_curta": "Guarita revestida em chapa de aço corten.", "descricao_longa": "Projeto de portaria segura e elegante. Aço Corten mapeado cuidadosamente para evitar repetições na textura de ferrugem.", "materiais": ["Aço Corten", "Vidro Blindado", "Pedra Portuguesa"], "software": "SketchUp + V-Ray", "tempo_render": "3h 40m", "img": "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-007", "titulo": "Estudo Luminotécnico", "categoria": "Fachada", "estilo": "Contemporâneo", "descricao_curta": "Fachada noturna com ênfase em fachos de luz.", "descricao_longa": "Configuração de IES Profiles (arquivos reais das lâmpadas) para garantir que os fachos de luz no render sejam idênticos à obra real.", "materiais": ["Tinta Acrílica", "MDF Naval Externo", "LED IES"], "software": "3ds Max + V-Ray", "tempo_render": "6h", "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-008", "titulo": "Industrial Loft", "categoria": "Fachada", "estilo": "Industrial", "descricao_curta": "Retrofit com janelas quadriculadas e tijolos.", "descricao_longa": "Técnicas avançadas de Displacement no V-Ray para que os rejuntes dos tijolos ingleses tenham profundidade 3D interagindo com sombras.", "materiais": ["Tijolo Demolição", "Metalon", "Vidro Canelado"], "software": "SketchUp + V-Ray", "tempo_render": "4h", "img": "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-009", "titulo": "Varanda Gourmet", "categoria": "Área de Lazer", "estilo": "Moderna", "descricao_curta": "Fechamento em vidro e painel ripado externo.", "descricao_longa": "Marcenaria projetada utiliza MDF Naval resistente à insolação. Iluminação de final de tarde entra pelas frestas dos fechamentos de vidro.", "materiais": ["MDF Naval", "Porcelanato", "Sistema Reiki"], "software": "3ds Max + Corona", "tempo_render": "4h 20m", "img": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=80"},
        {"id": "EXT-010", "titulo": "Jardim de Inverno", "categoria": "Área Externa", "estilo": "Zen", "descricao_curta": "Microclima com espelho d'água e pérgola.", "descricao_longa": "Espelho d'água escuro que reflete o céu e pérgola em vigas de Cumaru. Modelagem botânica intensa simulando espécies da Mata Atlântica.", "materiais": ["Madeira Cumaru", "Pedra Vulcânica", "Jardim Vertical"], "software": "SketchUp + V-Ray", "tempo_render": "5h", "img": "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=800&q=80"}
    ]
    return interiores, exteriores

# ==============================================================================
# 4. COMPONENTES E PÁGINAS DO SISTEMA
# ==============================================================================
def render_project_card(proj):
    with st.container():
        st.markdown(f"""
            <div class="project-card">
                <div class="img-container"><img src="{proj['img']}" alt="{proj['titulo']}"></div>
                <div class="card-content">
                    <div class="project-title">{proj['titulo']}</div>
                    <div style="font-size: 0.8rem; color: #d4af37; margin-bottom: 10px; text-transform: uppercase;">{proj['categoria']} | {proj['estilo']}</div>
                    <div class="project-desc">{proj['descricao_curta']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"VER RELATÓRIO TÉCNICO", key=f"btn_{proj['id']}"):
            st.session_state['projeto_selecionado'] = proj
            st.session_state['page'] = 'Detalhes do Projeto'
            st.rerun()

def page_home():
    st.markdown("<h1 style='text-align:center; font-size:4.5rem; margin-top:20px; margin-bottom:0;'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; letter-spacing:6px; margin-top:5px;'>ARCHVIZ PARA ALTA MARCENARIA</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1500&q=80", use_container_width=True)
    
    st.markdown("<br><h2 style='text-align:center; color:#d4af37 !important;'>Elevando Projetos à Realidade.</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#aaa; max-width: 800px; margin: 0 auto; line-height:1.8;'>Entregamos ferramentas de vendas fotorealistas para escritórios de arquitetura e marcenarias, respeitando modulações reais, catálogos físicos e detalhamentos executivos.</p>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1, 1])
    with col:
        if st.button("ACESSAR PORTFÓLIO", use_container_width=True):
            st.session_state['page'] = 'Portfólio'
            st.rerun()

def page_portfolio():
    int_db, ext_db = carregar_banco_de_dados()
    
    st.markdown("<h1>Catálogo de Visualização</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666; margin-bottom:40px;'>Soluções de renderização de alto padrão divididas por áreas de atuação.</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='border-left: 4px solid #d4af37; padding-left: 10px;'>INTERIORES & DETALHAMENTO (15 Projetos)</h3><br>", unsafe_allow_html=True)
    cols_int = st.columns(3)
    for i, proj in enumerate(int_db):
        with cols_int[i % 3]: render_project_card(proj)
            
    st.markdown("<br><hr style='border-color:#333;'><br>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='border-left: 4px solid #d4af37; padding-left: 10px;'>ARQUITETURA EXTERIOR (10 Projetos)</h3><br>", unsafe_allow_html=True)
    cols_ext = st.columns(3)
    for i, proj in enumerate(ext_db):
        with cols_ext[i % 3]: render_project_card(proj)

def page_projeto_detalhe():
    proj = st.session_state.get('projeto_selecionado')
    if not proj:
        st.session_state['page'] = 'Portfólio'
        st.rerun()
        return

    if st.button("← VOLTAR"):
        st.session_state['projeto_selecionado'] = None
        st.session_state['page'] = 'Portfólio'
        st.rerun()
        
    st.image(proj['img'], use_container_width=True)
    st.markdown(f"<h1 style='font-size:2.5rem; margin-top:20px; margin-bottom:0;'>{proj['titulo']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#d4af37; letter-spacing:2px; text-transform:uppercase;'>{proj['categoria']} | {proj['estilo']}</p>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("<h3>Memorial Descritivo da Imagem</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#aaa; line-height:1.8;'>{proj['descricao_longa']}</p>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='background:#111; border:1px solid #222; padding:25px; border-radius:6px;'><h4 style='color:#d4af37 !important;'>Ficha Técnica</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:0;'>Software:</p><p style='color:#ccc;'>{proj['software']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:0;'>Processamento:</p><p style='color:#ccc;'>{proj['tempo_render']}</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#888; font-size:0.9rem; margin-bottom:5px;'>Materiais PBR:</p>", unsafe_allow_html=True)
        for mat in proj['materiais']:
            st.markdown(f"<span style='display:inline-block; background:#1a1a1a; border:1px solid #333; color:#aaa; font-size:0.8rem; padding:4px 8px; border-radius:4px; margin:2px;'>{mat}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

def page_planos():
    """Área exclusiva dos Planos Solicitada pelo Usuário"""
    st.markdown("<h1 style='text-align:center;'>Planos e Pacotes</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; margin-bottom:50px;'>Escolha o formato ideal para acelerar as aprovações da sua marcenaria.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
            <div class='pricing-card'>
                <h3 class='pricing-title'>ArchViz Essencial</h3>
                <div class='pricing-subtitle'>Para projetos rápidos</div>
                <p style='color:#888; font-size:0.9rem; height:45px;'>Ideal para apresentar aquele ambiente focado do dia a dia (cozinhas ou quartos unitários).</p>
                <div class='pricing-features'>
                    <span>✓</span> Otimização de Arquivo Base<br>
                    <span>✓</span> Aplicação de Texturas Reais<br>
                    <span>✓</span> Iluminação Padrão Diurna<br>
                    <span>✓</span> <b>2 Imagens Estáticas 4K</b><br>
                    <span style='color:#555;'>✗</span> <i>Sem alterações estruturais</i>
                </div>
                <a href='https://wa.me/5514998405046?text=Ol%C3%A1,%20gostaria%20de%20solicitar%20o%20Plano%20Essencial' target='_blank' class='btn-outline' style='margin-top:auto;'>SOLICITAR</a>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
            <div class='pricing-card' style='border-color: #d4af37; position: relative;'>
                <div style='position:absolute; top:-15px; left:50%; transform:translateX(-50%); background:#d4af37; color:#000; padding:4px 15px; border-radius:20px; font-size:0.75rem; font-weight:bold;'>MAIS VENDIDO</div>
                <h3 class='pricing-title'>Premium Marcenaria</h3>
                <div class='pricing-subtitle'>Casa Completa</div>
                <p style='color:#888; font-size:0.9rem; height:45px;'>O pacote definitivo para fechar projetos de alto padrão com clientes exigentes.</p>
                <div class='pricing-features'>
                    <span>✓</span> Modelagem Fina de Detalhes<br>
                    <span>✓</span> Produção e Decoração de Cena VIP<br>
                    <span>✓</span> Iluminação Cenográfica Avançada<br>
                    <span>✓</span> <b>5 Imagens Estáticas 4K</b><br>
                    <span>✓</span> 1 Rodada de Alteração de Materiais
                </div>
                <a href='https://wa.me/5514998405046?text=Ol%C3%A1,%20quero%20fechar%20o%20Plano%20Premium' target='_blank' class='btn-gold' style='margin-top:auto;'>CONTRATAR AGORA</a>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
            <div class='pricing-card'>
                <h3 class='pricing-title'>Imersão 360º</h3>
                <div class='pricing-subtitle'>Apresentação Interativa</div>
                <p style='color:#888; font-size:0.9rem; height:45px;'>Gere um link para o seu cliente explorar o ambiente olhando para todos os lados pelo celular.</p>
                <div class='pricing-features'>
                    <span>✓</span> Modelagem Otimizada 360<br>
                    <span>✓</span> Renderização Esférica<br>
                    <span>✓</span> Criação de Link Interativo<br>
                    <span>✓</span> <b>1 Ambiente 360 Completo</b><br>
                    <span>✓</span> Hospedagem do Link (6 meses)
                </div>
                <a href='https://wa.me/5514998405046?text=Ol%C3%A1,%20gostaria%20de%20saber%20mais%20sobre%20o%20Tour%20360' target='_blank' class='btn-outline' style='margin-top:auto;'>SABER MAIS</a>
            </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# 5. ROTEADOR PRINCIPAL E MENU LATERAL
# ==============================================================================
def main():
    injetar_css_premium()
    
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; font-size: 2.2rem;'>PALLADIUM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#555; font-size:0.7rem; letter-spacing:5px;'>ARCHVIZ STUDIO</p>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        if st.button("INÍCIO"): 
            st.session_state['projeto_selecionado'] = None
            st.session_state['page'] = 'Início'
        if st.button("PORTFÓLIO"): 
            st.session_state['projeto_selecionado'] = None
            st.session_state['page'] = 'Portfólio'
        if st.button("PLANOS E PACOTES"): 
            st.session_state['projeto_selecionado'] = None
            st.session_state['page'] = 'Planos'
            
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<a href="https://wa.me/5514998405046" target="_blank" class="btn-gold" style="padding: 15px;">FALAR COM EQUIPE</a>', unsafe_allow_html=True)
        
        st.markdown("<div style='position: absolute; bottom: 20px; width: 100%; text-align: center; color: #333; font-size: 0.65rem;'>PALLADIUM STUDIO © 2026</div>", unsafe_allow_html=True)

    page = st.session_state['page']
    with st.container():
        st.markdown("<div style='padding: 1% 4% 5% 4%;'>", unsafe_allow_html=True)
        if page == 'Início': page_home()
        elif page == 'Portfólio': page_portfolio()
        elif page == 'Detalhes do Projeto': page_projeto_detalhe()
        elif page == 'Planos': page_planos()
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
