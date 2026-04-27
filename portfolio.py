import streamlit as st
import time
import streamlit.components.v1 as components

# ==============================================================================
# 1. CONFIGURAÇÃO DE AMBIENTE E ESTADO DO SISTEMA
# ==============================================================================
st.set_page_config(
    page_title="Palladium Studio | Premium ArchViz",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização de variáveis de estado para navegação no aplicativo (SPA)
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
        /* Importação de fontes premium */
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

        /* Paleta de Cores e Variáveis Globais */
        :root {
            --bg-color: #080808;
            --text-main: #f2f2f2;
            --text-muted: #888888;
            --accent: #d4af37; 
            --accent-hover: #e8c85c;
            --card-bg: #111111;
            --card-hover: #161616;
            --border: #222222;
        }

        /* Configurações Base */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color) !important;
            color: var(--text-main) !important;
        }

        /* Correção para barra superior e ocultação de menus indesejados */
        header {background-color: transparent !important;}
        #MainMenu, footer {visibility: hidden;}

        /* Tipografia de Títulos */
        h1, h2, h3, h4 {
            font-family: 'Cinzel', serif !important;
            font-weight: 600 !important;
            color: #ffffff !important;
            letter-spacing: 1px;
        }

        /* --- ESTILOS DO HERO (TOPO DA PÁGINA INICIAL) --- */
        .hero-title {
            text-align: center;
            font-size: 4.5rem;
            margin-top: 20px;
            margin-bottom: 0px;
            color: #ffffff;
            font-family: 'Cinzel', serif;
        }
        
        .hero-subtitle {
            text-align: center;
            color: #888;
            font-size: 1.1rem;
            letter-spacing: 8px;
            margin-top: 5px;
            margin-bottom: 40px;
        }

        /* --- SISTEMA DE GRID E CARDS DE PROJETOS --- */
        .project-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 6px;
            transition: all 0.4s ease;
            margin-bottom: 25px;
            display: flex;
            flex-direction: column;
            height: 100%;
            overflow: hidden;
        }
        .project-card:hover {
            border-color: var(--accent);
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(212, 175, 55, 0.1);
            background: var(--card-hover);
        }
        .img-container {
            width: 100%;
            aspect-ratio: 16/9;
            overflow: hidden;
            background: #1a1a1a;
            position: relative;
        }
        .img-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 1.2s ease;
        }
        .project-card:hover img { 
            transform: scale(1.05); 
        }
        .card-content { 
            padding: 25px; 
            display: flex; 
            flex-direction: column; 
            flex-grow: 1; 
        }
        .project-title { 
            font-family: 'Cinzel', serif; 
            font-size: 1.2rem; 
            color: var(--accent); 
            margin-bottom: 10px; 
        }
        .project-desc { 
            font-size: 0.9rem; 
            color: var(--text-muted); 
            line-height: 1.6; 
            margin-bottom: 15px; 
            flex-grow: 1; 
        }

        /* --- MENU LATERAL (SIDEBAR) --- */
        [data-testid="stSidebar"] { 
            background-color: #050505 !important; 
            border-right: 1px solid var(--border); 
        }
        [data-testid="stSidebar"] .stButton>button {
            background-color: transparent !important; 
            color: #666 !important;
            border: none !important; 
            border-left: 3px solid transparent !important;
            text-align: left !important; 
            padding: 15px 25px !important;
            font-size: 0.9rem !important; 
            letter-spacing: 3px; 
            transition: 0.3s;
            width: 100%; 
            justify-content: flex-start;
        }
        [data-testid="stSidebar"] .stButton>button:hover {
            color: #fff !important; 
            border-left: 3px solid var(--accent) !important;
            background-color: #0a0a0a !important; 
            transform: translateX(5px);
        }

        .sidebar-footer {
            padding: 20px;
            text-align: center;
            border-top: 1px solid #1a1a1a;
            margin-top: 20px;
        }

        /* --- BOTÕES PREMIUM CALL TO ACTION --- */
        .btn-gold {
            display: block; 
            background: var(--accent); 
            color: #000 !important;
            text-align: center; 
            padding: 15px; 
            font-weight: 700;
            letter-spacing: 2px; 
            text-decoration: none; 
            text-transform: uppercase;
            transition: 0.4s; 
            border-radius: 3px; 
            border: 1px solid var(--accent);
            font-size: 0.85rem;
        }
        .btn-gold:hover { 
            background: #fff; 
            border-color: #fff; 
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.3); 
        }
        
        .btn-outline {
            display: block; 
            background: transparent; 
            color: var(--accent) !important;
            text-align: center; 
            padding: 15px; 
            font-weight: 600;
            letter-spacing: 2px; 
            text-decoration: none; 
            text-transform: uppercase;
            transition: 0.3s; 
            border: 1px solid var(--accent); 
            border-radius: 3px;
            font-size: 0.85rem;
        }
        .btn-outline:hover { 
            background: var(--accent); 
            color: #000 !important; 
        }

        /* --- TABELAS DE PREÇO (PRICING) --- */
        .pricing-card {
            background: #0d0d0d; 
            border: 1px solid #333; 
            padding: 40px 30px;
            text-align: center; 
            border-radius: 8px; 
            transition: 0.3s; 
            height: 100%;
            display: flex; 
            flex-direction: column;
        }
        .pricing-card:hover { 
            border-color: var(--accent); 
            background: #141414; 
            transform: translateY(-5px); 
        }

        /* --- RESPONSIVIDADE MOBILE AVANÇADA --- */
        @media (max-width: 768px) {
            .hero-title { 
                font-size: 2.2rem !important; 
                margin-top: 40px !important; 
            }
            .hero-subtitle { 
                font-size: 0.7rem !important; 
                letter-spacing: 4px !important; 
            }
            [data-testid="stHorizontalBlock"] { 
                flex-direction: column !important; 
            }
            .pricing-card {
                margin-bottom: 25px;
            }
        }

        /* Esconde botões nativos das imagens do Streamlit */
        button[title="View fullscreen"] { display: none; }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. BANCO DE DADOS ESTRUTURADO (MULTI-ÂNGULO)
# ==============================================================================
def carregar_banco_de_dados():
    """
    Retorna a matriz de dados de interiores e exteriores.
    Arquitetura de dados orientada a objetos para listagens dinâmicas.
    """
    interiores = [
        {
            "id": "I1",
            "titulo": "Cozinha Minimalista Nero",
            "categoria": "Cozinha",
            "estilo": "Minimalista",
            "descricao_curta": "MDF Preto Silk e puxadores cava integrados.",
            "descricao_longa": "Análise técnica de 4 ângulos focando na continuidade das fibras do MDF Preto Silk e no detalhamento do puxador cava 45º, garantindo alinhamento perfeito das frentes sem ferragens aparentes.",
            "materiais": ["MDF Preto Silk", "Quartzo Cinza", "Puxador Cava", "LED 3000K"],
            "software": "SketchUp + V-Ray 6",
            "tempo_render": "3h 45m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1556911220-e15022357539?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1556911261-6bd341186b2f?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I2",
            "titulo": "Suíte Master Ripado",
            "categoria": "Dormitório",
            "estilo": "Contemporâneo",
            "descricao_curta": "Painel Freijó com iluminação indireta.",
            "descricao_longa": "Uma suíte master projetada para máximo conforto. 4 perspectivas detalhando a paginação técnica do ripado em MDF Freijó e o comportamento da luz 'wall washer' sobre a cabeceira em linho cru.",
            "materiais": ["MDF Freijó", "Linho Cru", "Laca Cinza"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "5h 20m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1616594111750-4744bda7e9a2?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1583847268964-b28dc2f51ac9?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I3",
            "titulo": "Living Contemporâneo",
            "categoria": "Living",
            "estilo": "Moderno",
            "descricao_curta": "Sala ampla com pé-direito duplo.",
            "descricao_longa": "Estudo de luz natural em diferentes ângulos da sala de pé-direito duplo, destacando os reflexos precisos no porcelanato de grande formato e a sutileza do MDF Areia no mobiliário.",
            "materiais": ["MDF Areia", "Porcelanato Polido", "Vidro Laminado"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "4h 10m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1618219944342-824e40a13285?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I4",
            "titulo": "Banheiro SPA em Mármore",
            "categoria": "Banheiro",
            "estilo": "Clássico",
            "descricao_curta": "MDF Branco Ultra e cuba em Calacatta Gold.",
            "descricao_longa": "Sequência de ângulos mostrando a resistência e assepsia do gabinete suspenso em MDF Ultra (resistente à umidade), contrastando com a cuba esculpida no nobre mármore Calacatta.",
            "materiais": ["MDF Ultra", "Mármore Calacatta", "Metais Red Gold"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "6h 15m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1603912975949-c1e1e0a29363?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1604014237800-1c9102c219da?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I5",
            "titulo": "Gourmet Integrado",
            "categoria": "Área de Lazer",
            "estilo": "Industrial",
            "descricao_curta": "Churrasqueira com marcenaria em tons grafite.",
            "descricao_longa": "Foco na integração visual entre a área técnica da churrasqueira e o mobiliário de apoio. Simulação de chapas em MDF Grafite com alta resistência a gordura, e o uso de madeira de demolição na mesa.",
            "materiais": ["MDF Grafite", "Cimento Queimado", "Madeira Maciça"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "4h 30m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1565538810643-b5bdb714032a?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1556912998-c57cc6b63ce7?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1565183928294-7063f23ce0f8?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1505692952047-1a78307da8f2?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I6",
            "titulo": "Home Office Executivo",
            "categoria": "Escritório",
            "estilo": "Corporativo",
            "descricao_curta": "Estante técnica com nichos iluminados.",
            "descricao_longa": "Visões focadas na ergonomia da mesa flutuante e no detalhamento das prateleiras iluminadas. Contraste marcante entre a Laca Preta e o padrão MDF Carvalho Hannover.",
            "materiais": ["Laca Preta", "MDF Carvalho Hannover", "Couro Natural"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "3h 45m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1497215898141-86daaa72295d?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I7",
            "titulo": "Closet Walk-in Boutique",
            "categoria": "Dormitório",
            "estilo": "Premium",
            "descricao_curta": "Portas em vidro reflecta e cabideiros em LED.",
            "descricao_longa": "Tour visual pelos módulos internos organizados para máxima eficiência de armazenamento. Proteção do closet feita inteiramente com Vidro Reflecta Bronze e perfis em alumínio preto.",
            "materiais": ["Vidro Reflecta Bronze", "MDF Cinza Sagrado", "Alumínio Preto"],
            "software": "SketchUp + Enscape",
            "tempo_render": "1h 50m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1618219944342-824e40a13285?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I8",
            "titulo": "Sala de Jantar Elegance",
            "categoria": "Living",
            "estilo": "Clássico",
            "descricao_curta": "Buffet com portas em palhinha indiana e tampo em mármore.",
            "descricao_longa": "Destaque para o realismo da textura vazada da palhinha indiana aplicada ao buffet e o encaixe perfeito da pedra de mármore travertino na marcenaria do apoio.",
            "materiais": ["Palhinha Indiana", "MDF Nogueira", "Mármore Travertino"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "5h 10m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1617806118233-18e16208a50a?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1540932239986-30128078f3b5?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I9",
            "titulo": "Quarto Lúdico Infantil",
            "categoria": "Dormitório",
            "estilo": "Infantil",
            "descricao_curta": "Cores pastéis, nichos e formas arredondadas.",
            "descricao_longa": "Detalhamento profundo de segurança, mostrando cantos arredondados simulando o acabamento curvo em laca premium, garantindo um ambiente ergonômico e lúdico para a criança.",
            "materiais": ["Laca Rosa Pastel", "MDF Carvalho", "Algodão Orgânico"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "3h 25m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1584622781564-1d987f7333c1?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1505692952047-1a78307da8f2?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I10",
            "titulo": "Adega Particular",
            "categoria": "Área de Lazer",
            "estilo": "Rústico Moderno",
            "descricao_curta": "Nichos colmeia em madeira maciça Cumaru.",
            "descricao_longa": "Ângulos imersivos que exploram a penumbra (tratada com AI Denoising) e a textura natural da madeira Cumaru contrastando com o tijolo inglês da parede de fundo.",
            "materiais": ["Madeira Cumaru", "Tijolo Inglês", "Vidro Duplo"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "6h 40m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1510626176961-4b57d4fbad03?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1585553616435-2dc0a54e271d?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1565183928294-7063f23ce0f8?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I11", "titulo": "Hall Minimal",
            "categoria": "Circulação",
            "estilo": "Minimalista",
            "descricao_curta": "Aparador slim suspenso e painel de espelhos.",
            "descricao_longa": "Uso estratégico de espelhos para duplicar o espaço. As 4 visões mostram o console de 12cm de espessura com gavetas no formato fecho-toque e o piso de granito polido.",
            "materiais": ["MDF Lacca Cetin", "Espelho Prata Bisotado", "Piso em Granito"],
            "software": "SketchUp + Corona Renderer",
            "tempo_render": "2h 30m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1583847268964-b28dc2f51ac9?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1618221118493-9cfa1a1c00da?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I12", "titulo": "Lavanderia Técnica",
            "categoria": "Serviço",
            "estilo": "Funcional",
            "descricao_curta": "MDF Branco Ártico, tulhas embutidas e cabideiro.",
            "descricao_longa": "Ângulos que provam como a marcenaria inteligente organiza o setor de serviços. Simulação técnica de respiros para máquinas e rodapés metálicos contra umidade.",
            "materiais": ["MDF Branco Ártico", "Corian", "Alumínio"],
            "software": "SketchUp + Enscape",
            "tempo_render": "1h 00m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1521783593447-5702b9bfd267?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1584622781564-1d987f7333c1?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1556911220-e15022357539?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I13", "titulo": "Biblioteca Classic",
            "categoria": "Escritório",
            "estilo": "Clássico Modernizado",
            "descricao_curta": "Estante pé-direito duplo e escada metálica.",
            "descricao_longa": "Destaque para a verticalidade da estante de 6 metros. O uso de texturas do Carvalho Natural contrasta com os trilhos de iluminação eletrificados e a escada deslizante.",
            "materiais": ["MDF Carvalho Natural", "Metal Preto", "Piso Vinílico"],
            "software": "3ds Max + Corona",
            "tempo_render": "6h 10m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1497215898141-86daaa72295d?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I14", "titulo": "Recepção Comercial",
            "categoria": "Comercial",
            "estilo": "Premium",
            "descricao_curta": "Balcão em curva com filetes LED embutidos.",
            "descricao_longa": "Perspectivas que mostram o design orgânico da recepção. A Fórmica Branca Brilhante e o recuo com LED criam uma sensação de leveza estrutural.",
            "materiais": ["Fórmica Branca Brilhante", "MDF Madeirado", "Porcelanato"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "3h 30m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1497215898141-86daaa72295d?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "I15", "titulo": "Hometheater Laca Brilho",
            "categoria": "Living",
            "estilo": "Luxo",
            "descricao_curta": "Painel de TV em laca com múltiplos polimentos.",
            "descricao_longa": "Estudo profundo de reflexos PBR em 4 ângulos, provando a perfeição das múltiplas camadas de verniz aplicadas à Laca Polida que reveste o painel principal da TV.",
            "materiais": ["Laca Alto Brilho", "MDF Grafite", "Couro Preto"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "5h 45m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1593910265171-ef6709849202?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1618221118493-9cfa1a1c00da?auto=format&fit=crop&w=1200&q=80"
            ]
        }
    ]

    exteriores = [
        {
            "id": "E1", "titulo": "Fachada Contemporânea", "categoria": "Fachada", "estilo": "Moderna",
            "descricao_curta": "Volumes sobrepostos e brises amadeirados.",
            "descricao_longa": "4 visões da volumetria externa, transitando entre a forte luz solar da tarde e a sutil iluminação noturna cênica embutida nos balizadores de piso e na laje.",
            "materiais": ["Brises de Alumínio", "Concreto Aparente", "Esquadrias Pretas"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "5h 10m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E2", "titulo": "Área de Lazer Tropical", "categoria": "Lazer", "estilo": "Tropical",
            "descricao_curta": "Deck em madeira natural e borda infinita.",
            "descricao_longa": "Análise da física da água (cáusticas e refrações) e reflexos do céu HDRI em múltiplos ângulos. O deck em Itaúba possui imperfeições realistas criadas com mapas de Displacement.",
            "materiais": ["Madeira Itaúba", "Pastilhas Cerâmicas", "Mármore Branco"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "7h 30m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E3", "titulo": "Corporativo Glass", "categoria": "Comercial", "estilo": "Urbano",
            "descricao_curta": "Pele de vidro refletiva e asfalto PBR molhado.",
            "descricao_longa": "Foco na transparência arquitetônica e no contexto urbano envolvente. O edifício possui interiores modelados em low-poly para que o vidro ganhe profundidade real.",
            "materiais": ["Pele de Vidro Prata", "ACM Preto", "Concreto"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "6h 45m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1497215898141-86daaa72295d?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E4", "titulo": "Casa de Campo", "categoria": "Fachada", "estilo": "Rústico",
            "descricao_curta": "Integração ambiental com pedras irregulares.",
            "descricao_longa": "Perspectivas integradas à vegetação densa. O uso do Forest Pack permitiu distribuir milhares de árvores e arbustos sem comprometer a performance do projeto 3D.",
            "materiais": ["Pedra Moledo", "Vigas de Eucalipto", "Telha Shingle"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "8h 15m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1500313830540-7b6650a74fd0?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E5", "titulo": "Rooftop Lounge", "categoria": "Lazer", "estilo": "Urbano Moderno",
            "descricao_curta": "Skyline noturna e mobiliário em corda náutica.",
            "descricao_longa": "4 ângulos da área social superior com foco em iluminação de 'Blue Hour' (horário mágico da fotografia), balanceando luzes quentes artificiais e o fundo frio da cidade.",
            "materiais": ["Deck Sintético", "Corda Náutica", "Vidro Temperado"],
            "software": "SketchUp + Enscape",
            "tempo_render": "1h 45m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E6", "titulo": "Entrada Condomínio", "categoria": "Comercial", "estilo": "Imponente",
            "descricao_curta": "Chapas de Aço Corten e guarita blindada.",
            "descricao_longa": "Visão técnica da segurança e elegância no acesso principal do empreendimento. O Aço Corten foi meticulosamente mapeado para não apresentar 'tile' (repetições na textura de ferrugem).",
            "materiais": ["Aço Corten", "Vidro Blindado", "Pedra Portuguesa"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "4h 10m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E7", "titulo": "Estudo Luminotécnico", "categoria": "Fachada", "estilo": "Contemporâneo",
            "descricao_curta": "Fachos de luz fiéis usando arquivos IES reais.",
            "descricao_longa": "4 imagens noturnas provando a precisão luminotécnica da simulação. O uso de perfis IES garante que as manchas de luz projetadas na alvenaria se comportem exatamente como o projeto executivo aprovado.",
            "materiais": ["Tinta Acrílica Branca", "MDF Naval Externo", "Iluminação LED IES"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "6h 25m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E8", "titulo": "Industrial Loft", "categoria": "Fachada", "estilo": "Industrial",
            "descricao_curta": "Tijolo de demolição, metal e grandes janelas.",
            "descricao_longa": "O projeto de retrofit conta com profunda aplicação de Displacement nos rejuntes e janelas com caixilhos de ferro. A iluminação de outono reforça o clima 'Brooklyn' proposto.",
            "materiais": ["Tijolo Inglês Demolição", "Metalon Grafite", "Vidro Canelado"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "4h 50m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1565538810643-b5bdb714032a?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E9", "titulo": "Varanda Gourmet de Apartamento", "categoria": "Lazer", "estilo": "Apartamento",
            "descricao_curta": "Fechamento Reiki, nivelamento e MDF Naval.",
            "descricao_longa": "Otimização de espaço em sacada com integração total à sala. Renderização explora o contraste entre a luz que invade o fechamento de vidro e a marcenaria naval que oculta condensadoras.",
            "materiais": ["MDF Naval Amadeirado", "Porcelanato", "Sistema em Vidro Reiki"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "4h 20m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1618219944342-824e40a13285?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
            ]
        },
        {
            "id": "E10", "titulo": "Jardim de Inverno", "categoria": "Externo", "estilo": "Zen Asiático",
            "descricao_curta": "Espelho d'água orgânico e jardim vertical exuberante.",
            "descricao_longa": "4 ângulos de um espaço de relaxamento. O grande triunfo do render é a modelagem botânica intensa simulando dezenas de espécies de plantas da Mata Atlântica refletindo no espelho d'água sob a pérgola.",
            "materiais": ["Madeira Cumaru", "Pedra Vulcânica Escura", "Jardim Vertical 3D"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "5h 45m (4K)",
            "imgs": [
                "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1500313830540-7b6650a74fd0?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80",
                "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80"
            ]
        }
    ]
    return interiores, exteriores

# ==============================================================================
# 4. COMPONENTES E PÁGINAS DO SISTEMA DE INTERFACE
# ==============================================================================
def render_project_card(proj):
    """Componente renderizador de blocos de projetos do portfólio."""
    with st.container():
        st.markdown(f"""
            <div class="project-card">
                <div class="img-container">
                    <img src="{proj['imgs'][0]}" alt="{proj['titulo']}">
                </div>
                <div class="card-content">
                    <div class="project-title">{proj['titulo']}</div>
                    <div style="font-size: 0.8rem; color: #d4af37; margin-bottom: 10px; text-transform: uppercase;">
                        {proj['categoria']} | {proj['estilo']}
                    </div>
                    <div class="project-desc">{proj['descricao_curta']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"VER RELATÓRIO TÉCNICO", key=f"btn_{proj['id']}"):
            st.session_state['projeto_selecionado'] = proj
            st.session_state['page'] = 'Detalhes do Projeto'
            st.rerun()

def page_home():
    """Tela Inicial do Palladium Studio (Hero Section)"""
    st.markdown("<h1 class='hero-title'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>ARCHVIZ PARA ALTA MARCENARIA</p>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1500&q=80", use_container_width=True)
    
    st.markdown("<br><h2 style='text-align:center; color:#d4af37 !important;'>O Seu Projeto, Antes de Existir.</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#aaa; max-width: 800px; margin: 0 auto; line-height:1.8;'>Respeitamos modulações reais e catálogos físicos para garantir aprovações rápidas.</p>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1, 1])
    with col:
        if st.button("ACESSAR PORTFÓLIO COMPLETO", use_container_width=True):
            st.session_state['page'] = 'Portfólio'
            st.rerun()

def page_portfolio():
    """Galeria completa em Grid System."""
    int_db, ext_db = carregar_banco_de_dados()
    st.markdown("<h1>Catálogo de Visualização</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666; margin-bottom:40px;'>Clique em 'Ver Relatório Técnico' para visualizar perspectivas extras de cada ambiente.</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='border-left: 4px solid #d4af37; padding-left: 10px;'>INTERIORES E DETALHAMENTO (15 Projetos)</h3><br>", unsafe_allow_html=True)
    cols_int = st.columns(3)
    for i, proj in enumerate(int_db):
        with cols_int[i % 3]: 
            render_project_card(proj)
            
    st.markdown("<br><hr style='border-color:#333;'><br>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='border-left: 4px solid #d4af37; padding-left: 10px;'>ARQUITETURA EXTERIOR (10 Projetos)</h3><br>", unsafe_allow_html=True)
    cols_ext = st.columns(3)
    for i, proj in enumerate(ext_db):
        with cols_ext[i % 3]: 
            render_project_card(proj)

def page_projeto_detalhe():
    """Página dinâmica que exibe os múltiplos ângulos (4 fotos) e a ficha técnica de um projeto."""
    proj = st.session_state.get('projeto_selecionado')
    if not proj:
        st.session_state['page'] = 'Portfólio'
        st.rerun()
        return

    if st.button("← VOLTAR PARA O PORTFÓLIO"):
        st.session_state['projeto_selecionado'] = None
        st.session_state['page'] = 'Portfólio'
        st.rerun()
        
    st.markdown(f"<h1 style='font-size:3rem; margin-top:20px; margin-bottom:0;'>Galeria Multi-Ângulo: {proj['titulo']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#d4af37; letter-spacing:2px; text-transform:uppercase;'>{proj['categoria']} | {proj['estilo']}</p><br>", unsafe_allow_html=True)
    
    # Exibição de 4 fotos empilhadas valorizando a verticalidade
    for i, img_url in enumerate(proj['imgs']):
        st.image(img_url, caption=f"Perspectiva de Câmera 0{i+1}", use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
    
    st.write("---")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("<h3>Memorial Descritivo da Renderização</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#aaa; line-height:1.8;'>{proj['descricao_longa']}</p>", unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div style='background:#111; border:1px solid #222; padding:25px; border-radius:6px;'>
                <h4 style='color:#d4af37 !important; border-bottom:1px solid #333; padding-bottom:10px; margin-top:0;'>Ficha Técnica</h4>
        """, unsafe_allow_html=True)
        st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:0;'>Processamento:</p><p style='color:#ccc;'>{proj['tempo_render']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:0;'>Softwares Usados:</p><p style='color:#ccc;'>{proj['software']}</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#888; font-size:0.9rem; margin-bottom:5px;'>Materiais e Texturas (PBR):</p>", unsafe_allow_html=True)
        for mat in proj['materiais']:
            st.markdown(f"<span style='display:inline-block; background:#1a1a1a; border:1px solid #333; color:#aaa; font-size:0.8rem; padding:4px 8px; border-radius:4px; margin:2px;'>{mat}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

def page_imersao():
    """NOVA ABA: Módulo de Experiências de Vídeo e Tour 360 Graus via Iframe."""
    st.markdown("<h1>Experiências Imersivas</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; font-size:1.1rem; margin-bottom:40px;'>Vá além das imagens estáticas. Impressione seu cliente final com tours interativos pelo ambiente e animações em vídeo fotorrealistas.</p>", unsafe_allow_html=True)
    
    # SEÇÃO 1: VÍDEO (Animação ArchViz)
    st.markdown("<h3 style='color:#d4af37 !important;'>1. Tour Virtual em Vídeo Animado</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#aaa;'>Animação sequencial desenvolvida com renderização em tempo real. Ideal para postagens no Instagram Reels e envio via WhatsApp, garantindo um alto índice de aprovação do projeto de marcenaria.</p>", unsafe_allow_html=True)
    
    # Componente nativo do Streamlit para rodar vídeos (substitua a URL abaixo pelo link do YouTube do seu projeto)
    st.video("https://www.youtube.com/watch?v=11X_N2U23zY")
    
    st.markdown("<br><hr style='border-color:#333;'><br>", unsafe_allow_html=True)
    
    # SEÇÃO 2: TOUR 360 GRAUS (Iframe Interativo)
    st.markdown("<h3 style='color:#d4af37 !important;'>2. Tour 360º Interativo</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#aaa;'>Clique e arraste a imagem abaixo para olhar em todas as direções do projeto. Você pode enviar links como este diretamente para o celular do seu cliente para que ele utilize com óculos VR ou movendo o próprio aparelho.</p>", unsafe_allow_html=True)
    
    # Usando st.components.v1 para injetar o visor 360 (Neste exemplo, um link público do Kuula. Substitua pelo seu)
    url_360 = "https://kuula.co/share/collection/7l1c9?logo=0&info=0&fs=1&vr=1&sd=1&initload=0&thumbs=1"
    components.iframe(url_360, height=600, scrolling=False)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<center><p style='color:#666;'>Os pacotes de Imersão e Animação podem ser orçados individualmente para cada ambiente planejado.</p></center>", unsafe_allow_html=True)

def page_planos():
    """Apresentação de pacotes de vendas alinhada perfeitamente com Flexbox CSS."""
    st.markdown("<h1 style='text-align:center;'>Planos e Pacotes</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; margin-bottom:50px;'>Soluções direcionadas para quem busca escalar as vendas de projetos de interiores.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
            <div class='pricing-card'>
                <h3 class='pricing-title'>ArchViz Essencial</h3>
                <div class='pricing-subtitle'>Para projetos rápidos</div>
                <p style='color:#888; font-size:0.9rem; height:45px;'>Ideal para apresentar ambientes unitários diários (ex: uma cozinha compacta ou um dormitório).</p>
                <div class='pricing-features'>
                    <span>✓</span> Otimização da Geometria Base<br>
                    <span>✓</span> Aplicação de Texturas (MDFs)<br>
                    <span>✓</span> Iluminação Padrão Global<br>
                    <span>✓</span> <b>2 Imagens Estáticas 4K</b><br>
                    <span style='color:#555;'>✗</span> <i style='color:#666;'>Sem alterações de marcenaria</i>
                </div>
                <a href='https://wa.me/5514998405046' class='btn-outline' style='margin-top:auto;'>SOLICITAR</a>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div class='pricing-card' style='border-color: #d4af37; position: relative;'>
                <div style='position:absolute; top:-15px; left:50%; transform:translateX(-50%); background:#d4af37; color:#000; padding:4px 15px; border-radius:20px; font-size:0.75rem; font-weight:bold;'>MAIS VENDIDO</div>
                <h3 class='pricing-title'>Premium Marcenaria</h3>
                <div class='pricing-subtitle'>Projetos Completos</div>
                <p style='color:#888; font-size:0.9rem; height:45px;'>O pacote definitivo para fechar propostas de alto padrão com clientes e arquitetos exigentes.</p>
                <div class='pricing-features'>
                    <span>✓</span> Modelagem Fina de Detalhes<br>
                    <span>✓</span> Produção e Decoração de Cena<br>
                    <span>✓</span> Iluminação Cenográfica<br>
                    <span>✓</span> <b>5 Imagens Estáticas 4K</b><br>
                    <span>✓</span> 1 Rodada de Alteração Inclusa
                </div>
                <a href='https://wa.me/5514998405046' class='btn-gold' style='margin-top:auto;'>CONTRATAR AGORA</a>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
            <div class='pricing-card'>
                <h3 class='pricing-title'>Imersão Absoluta</h3>
                <div class='pricing-subtitle'>Apresentação Interativa</div>
                <p style='color:#888; font-size:0.9rem; height:45px;'>Gere links para seu cliente olhar ao redor no celular (360º) ou encante-o com vídeos do projeto.</p>
                <div class='pricing-features'>
                    <span>✓</span> Modelagem Otimizada 360<br>
                    <span>✓</span> Renderização Esférica HDR<br>
                    <span>✓</span> Setup de Link Web Interativo<br>
                    <span>✓</span> <b>Ambiente 360 / Tour de Vídeo</b><br>
                    <span>✓</span> Servidor Ativo (6 meses)
                </div>
                <a href='https://wa.me/5514998405046' class='btn-outline' style='margin-top:auto;'>SABER MAIS</a>
            </div>
        """, unsafe_allow_html=True)

def page_metodologia():
    """Workflow do Estúdio"""
    st.markdown("<h1>Nossa Metodologia</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888;'>Pipeline técnico do Palladium Studio para garantir o mais puro fotorealismo, otimizando seu tempo.</p><br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
            <div class='timeline-step'><div class='timeline-title'>1. Briefing de Materiais</div><div class='timeline-desc'>Recebemos seu projeto (.SKP) e as referências de chapas (Arauco, Guararapes) e pedras.</div></div>
            <div class='timeline-step'><div class='timeline-title'>2. Setup PBR Físico</div><div class='timeline-desc'>Aplicamos os mapas de textura. A madeira terá o reflexo exato do catálogo, diferente do metal ou do couro.</div></div>
            <div class='timeline-step'><div class='timeline-title'>3. Clay Render de Aprovação</div><div class='timeline-desc'>Enviamos imagens "brancas" com iluminação natural para você aprovar o posicionamento das câmeras.</div></div>
            <div class='timeline-step' style='border-left: 2px solid transparent;'><div class='timeline-title'>4. Finalização 4K</div><div class='timeline-desc'>Processamento em servidor dedicado (V-Ray/Corona) e pós-produção profissional.</div></div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1542621323-23e5361b1716?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

def page_contato():
    """Página final otimizada para Desktop/Mobile (Sem erros de rodapé)"""
    st.markdown("<h1>Direto ao Ponto.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; margin-bottom:40px;'>Terceirize o estresse da renderização e foque no que importa: captar novos clientes de marcenaria.</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("""
            <div style='background:#111; padding:40px; border-radius:6px; border:1px solid #222;'>
                <h3 style='margin-top:0; color:#d4af37 !important;'>Central de Atendimento</h3>
                <p style='color:#aaa; line-height:2;'>
                    📍 <b>Operação Sede:</b> Ourinhos, SP<br>
                    🌍 <b>Atendimento Virtual:</b> Nível Nacional<br>
                    📧 <b>Contato Eletrônico:</b> comercial@palladiumstudio.com<br>
                    📱 <b>Link Direto WhatsApp:</b> (14) 99840-5046
                </p>
            </div>
        """, unsafe_allow_html=True)
        link = "https://wa.me/5514998405046"
        st.markdown(f'<a href="{link}" target="_blank" class="btn-gold" style="margin-top:20px;">CHAMAR EQUIPE NO WHATSAPP</a>', unsafe_allow_html=True)

    with c2:
        with st.expander("Fazem modelagem 3D do zero através da planta baixa?"):
            st.write("Sim. Levantamos as paredes 3D, inserimos o design de interiores baseando-se no seu croqui em DWG/PDF e aplicamos o layout solicitado.")
        with st.expander("Qual o prazo de entrega das perspectivas?"):
            st.write("Para projetos padrão (1 ou 2 ambientes de planejamento), a primeira prévia é entregue em até 48 horas úteis após o envio dos modelos base.")
        with st.expander("Vocês me entregam o arquivo SketchUp pronto?"):
            st.write("Nossa entrega comercial é a mídia renderizada (Imagens 4K, Vídeos ou Links 360). O arquivo raiz configurado não é comercializado por conter assets intelectuais proprietários do nosso banco de estúdio.")

# ==============================================================================
# 6. ROTEADOR PRINCIPAL E MENU LATERAL
# ==============================================================================
def main():
    injetar_css_premium()
    
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; font-size: 2.2rem; margin-bottom:0;'>PALLADIUM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#555; font-size:0.7rem; letter-spacing:5px; margin-top:0;'>ARCHVIZ STUDIO</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Limpeza profunda de estados inativos ao alternar telas
        if st.button("INÍCIO"): st.session_state.update({'projeto_selecionado': None, 'page': 'Início'})
        if st.button("PORTFÓLIO"): st.session_state.update({'projeto_selecionado': None, 'page': 'Portfólio'})
        if st.button("IMERSÃO 360 / VÍDEO"): st.session_state.update({'projeto_selecionado': None, 'page': 'Imersão'})
        if st.button("PLANOS E PACOTES"): st.session_state.update({'projeto_selecionado': None, 'page': 'Planos'})
        if st.button("METODOLOGIA TÉCNICA"): st.session_state.update({'projeto_selecionado': None, 'page': 'Metodologia'})
        if st.button("ORÇAMENTO & CONTATO"): st.session_state.update({'projeto_selecionado': None, 'page': 'Contato'})
        
        # FOOTER DA SIDEBAR LIVRE DE ERROS DE SOBREPOSIÇÃO
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<a href="https://wa.me/5514998405046" target="_blank" class="btn-gold">SOLICITAR ANÁLISE</a>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="sidebar-footer">
                <p style='color: #444; font-size: 0.65rem; letter-spacing: 1px; margin:0;'>
                    PALLADIUM STUDIO © 2026<br>
                    ARCHITECTURE VISUALIZATION
                </p>
            </div>
        """, unsafe_allow_html=True)

    page = st.session_state['page']
    
    with st.container():
        st.markdown("<div style='padding: 1% 4% 5% 4%;'>", unsafe_allow_html=True)
        if page == 'Início': page_home()
        elif page == 'Portfólio': page_portfolio()
        elif page == 'Detalhes do Projeto': page_projeto_detalhe()
        elif page == 'Imersão': page_imersao()
        elif page == 'Planos': page_planos()
        elif page == 'Metodologia': page_metodologia()
        elif page == 'Contato': page_contato()
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
