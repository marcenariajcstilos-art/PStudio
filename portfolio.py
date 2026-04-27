import streamlit as st
import time

# ==============================================================================
# 1. CONFIGURAÇÃO DE AMBIENTE E ESTADO DO SISTEMA
# ==============================================================================
st.set_page_config(
    page_title="Palladium Studio | Premium ArchViz",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização de variáveis de estado para navegação complexa
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

        #MainMenu, header, footer {visibility: hidden;}

        /* Tipografia de Títulos */
        h1, h2, h3, h4 {
            font-family: 'Cinzel', serif !important;
            font-weight: 600 !important;
            color: #ffffff !important;
            letter-spacing: 1px;
        }

        /* --- SISTEMA DE GRID E CARDS DE PROJETOS --- */
        .project-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 6px;
            padding: 0px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            margin-bottom: 30px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        .project-card:hover {
            border-color: var(--accent);
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(212, 175, 55, 0.08);
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
            font-size: 1.3rem; 
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
        .project-tags {
            font-size: 0.75rem;
            color: #aaaaaa;
            background: #1a1a1a;
            padding: 6px 10px;
            border-radius: 4px;
            display: inline-block;
            margin-top: 5px;
            margin-right: 8px;
            border: 1px solid #333;
            letter-spacing: 0.5px;
        }

        /* --- SIDEBAR CUSTOMIZADA --- */
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

        /* --- BOTÕES PREMIUM (CALL TO ACTION) --- */
        .btn-gold {
            display: block;
            background: var(--accent);
            color: #000 !important;
            text-align: center;
            padding: 18px 25px;
            font-weight: 700;
            letter-spacing: 3px;
            text-decoration: none;
            text-transform: uppercase;
            margin-top: 20px;
            transition: 0.4s;
            font-size: 0.9rem;
            border-radius: 3px;
            border: 1px solid var(--accent);
        }
        .btn-gold:hover { 
            background: #fff; 
            border-color: #fff;
            box-shadow: 0 0 25px rgba(212, 175, 55, 0.3); 
        }
        .btn-outline {
            display: block;
            background: transparent;
            color: var(--accent) !important;
            text-align: center;
            padding: 18px 25px;
            font-weight: 600;
            letter-spacing: 2px;
            text-decoration: none;
            text-transform: uppercase;
            margin-top: 20px;
            transition: 0.3s;
            border: 1px solid var(--accent);
            border-radius: 3px;
        }
        .btn-outline:hover {
            background: var(--accent);
            color: #000 !important;
        }

        /* --- TABELAS DE PREÇO / PACOTES --- */
        .pricing-card {
            background: #0f0f0f;
            border: 1px solid #333;
            padding: 40px 30px;
            text-align: center;
            border-radius: 8px;
            transition: 0.3s;
        }
        .pricing-card:hover {
            border-color: var(--accent);
            background: #141414;
        }
        .pricing-title {
            font-family: 'Cinzel', serif;
            color: var(--accent);
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        .pricing-price {
            font-size: 2.5rem;
            font-weight: 700;
            color: #fff;
            margin-bottom: 20px;
        }
        .pricing-features {
            text-align: left;
            color: #aaa;
            line-height: 2;
            margin-bottom: 30px;
            font-size: 0.9rem;
            border-top: 1px solid #222;
            padding-top: 20px;
        }

        /* --- TIMELINE DE METODOLOGIA --- */
        .timeline-step {
            border-left: 2px solid var(--accent);
            padding-left: 25px;
            position: relative;
            margin-bottom: 40px;
        }
        .timeline-step::before {
            content: '';
            position: absolute;
            left: -8px;
            top: 0;
            width: 14px;
            height: 14px;
            background: var(--accent);
            border-radius: 50%;
        }
        .timeline-title { color: #fff; font-size: 1.2rem; font-weight: 600; margin-bottom: 10px; }
        .timeline-desc { color: #888; line-height: 1.6; font-size: 0.95rem; }

        /* Esconder botão de expandir imagem nativo do Streamlit */
        button[title="View fullscreen"] { display: none; }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. BANCO DE DADOS RELACIONAL (25 PROJETOS DETALHADOS)
# ==============================================================================
def carregar_banco_de_dados():
    """
    Simula uma requisição a um banco de dados real.
    Contém metadados complexos para cada projeto arquitetônico.
    """
    interiores = [
        {
            "id": "INT-001",
            "titulo": "Cozinha Minimalista Nero",
            "categoria": "Cozinha",
            "estilo": "Minimalista",
            "descricao_curta": "MDF Preto Silk com iluminação embutida de 3000K e bancada em quartzo.",
            "descricao_longa": "Projeto de cozinha linear desenvolvido para destacar a elegância do minimalismo escuro. A marcenaria foi inteiramente configurada utilizando o padrão Preto Silk da Guararapes, contrastando perfeitamente com a bancada e frontão em Quartzo Cinza Absoluto. O desafio técnico deste render foi configurar corretamente a absorção de luz dos materiais escuros sem gerar granulação (noise), utilizando iluminação cenográfica nos perfis de LED de 3000K.",
            "materiais": ["MDF Preto Silk", "Quartzo Cinza", "Perfis LED"],
            "software": "SketchUp + V-Ray 6",
            "tempo_render": "3h 45m (4K)",
            "img": "https://images.unsplash.com/photo-1556911220-e15022357539?q=80&w=1200"
        },
        {
            "id": "INT-002",
            "titulo": "Suíte Master com Ripado",
            "categoria": "Dormitório",
            "estilo": "Contemporâneo",
            "descricao_curta": "Painel amadeirado ripado, laca cinza e cabeceira estofada em linho.",
            "descricao_longa": "Uma suíte master projetada para oferecer máximo conforto visual. A parede principal recebe um painel ripado em MDF Freijó Puro da Arauco, com espaçamento técnico de 15mm. A cabeceira estofada em linho cru recebe iluminação indireta no formato 'wall washer', destacando a textura do tecido. A modelagem 3D incluiu simulação física de tecidos no Marvelous Designer para criar caimento realista nos lençóis.",
            "materiais": ["MDF Freijó", "Laca Cinza Fosca", "Linho Cru"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "5h 20m (4K)",
            "img": "https://images.unsplash.com/photo-1616594111750-4744bda7e9a2?q=80&w=1200"
        },
        {
            "id": "INT-003",
            "titulo": "Home Theater Premium",
            "categoria": "Living",
            "estilo": "Luxo Moderno",
            "descricao_curta": "Móvel suspenso em laca e painel com perfis metálicos dourados.",
            "descricao_longa": "O ponto focal desta sala de estar é o imponente Home Theater. A marcenaria inferior foi desenhada como um bloco monolítico suspenso em Laca Fosca Off-White, enquanto o painel principal mescla MDF madeirado com finos perfis de metalon dourado. O render exigiu configuração avançada de PBR (Physically Based Rendering) para garantir reflexos corretos na tela da TV e nos metais.",
            "materiais": ["Laca Off-White", "Metalon Dourado", "MDF Nogueira"],
            "software": "SketchUp + Enscape 3.5",
            "tempo_render": "1h 10m (4K)",
            "img": "https://images.unsplash.com/photo-1593910265171-ef6709849202?q=80&w=1200"
        },
        {
            "id": "INT-004",
            "titulo": "Gourmet Integrado",
            "categoria": "Área de Lazer",
            "estilo": "Industrial Chic",
            "descricao_curta": "Churrasqueira nivelada com marcenaria em tons grafite e madeira de demolição.",
            "descricao_longa": "Espaço projetado para receber convidados, integrando a área de churrasco com o living interno. A marcenaria foi pensada para alta durabilidade, simulando chapas de MDF Grafite da Duratex. O grande destaque do render é a iluminação diurna (HDRI de final de tarde), que invade o ambiente projetando sombras suaves e destacando a textura rústica da mesa central em madeira de demolição.",
            "materiais": ["MDF Grafite", "Madeira Maciça", "Cimento Queimado"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "4h 30m (4K)",
            "img": "https://images.unsplash.com/photo-1565538810643-b5bdb714032a?q=80&w=1200"
        },
        {
            "id": "INT-005",
            "titulo": "Home Office Executivo",
            "categoria": "Escritório",
            "estilo": "Corporativo",
            "descricao_curta": "Estante com nichos iluminados, mesa flutuante e cadeiras em couro.",
            "descricao_longa": "Com a nova realidade do trabalho híbrido, este espaço foi otimizado para conferências de vídeo e concentração. A estante ao fundo mistura nichos fechados em Laca Preta e abertos em MDF Carvalho Hannover. A modelagem detalhada incluiu a fiação invisível e a textura realista do couro da cadeira executiva. Renderizado utilizando Chaos Cloud para agilidade na entrega.",
            "materiais": ["Laca Preta", "MDF Carvalho Hannover", "Couro Natural"],
            "software": "SketchUp + V-Ray Cloud",
            "tempo_render": "45m (Cloud 4K)",
            "img": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=1200"
        },
        {
            "id": "INT-006",
            "titulo": "Banheiro SPA em Mármore",
            "categoria": "Banheiro",
            "estilo": "Clássico Modernizado",
            "descricao_curta": "Gabinete em MDF Branco Ultra com cuba esculpida em mármore Calacatta.",
            "descricao_longa": "Projeto de sala de banho focado em relaxamento. A marcenaria técnica simulou o uso de MDF Ultra (resistente à umidade) com acabamento branco fosco e puxadores do tipo cava 45 graus. O desafio foi a configuração complexa dos materiais translúcidos (Subsurface Scattering) do mármore Calacatta Gold na bancada e o espelho com borda infinita retroiluminada.",
            "materiais": ["Mármore Calacatta Gold", "MDF Branco Ultra", "Metais Red Gold"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "6h 15m (4K)",
            "img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=1200"
        },
        {
            "id": "INT-007",
            "titulo": "Living Contemporâneo",
            "categoria": "Living",
            "estilo": "Contemporâneo",
            "descricao_curta": "Sala de pé-direito duplo com grandes aberturas e mobiliário de design.",
            "descricao_longa": "Este living de pé-direito duplo exigiu precisão absoluta na volumetria. O render tira partido da luz natural abundante, estudando como o sol das 15h interage com o piso em porcelanato polido de grande formato. A marcenaria de apoio é discreta, focando em painéis lisos em MDF Areia que não roubam a atenção do mobiliário de design assinado.",
            "materiais": ["MDF Areia", "Porcelanato Polido", "Vidro Laminado"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "3h 00m (4K)",
            "img": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?q=80&w=1200"
        },
        {
            "id": "INT-008",
            "titulo": "Closet Walk-in Iluminado",
            "categoria": "Dormitório",
            "estilo": "Boutique",
            "descricao_curta": "Divisórias em MDF cinza, portas em vidro reflecta e cabideiros em LED.",
            "descricao_longa": "Um closet desenhado para parecer uma boutique de luxo. Não há portas cegas; toda a proteção é feita com esquadrias finas pretas e Vidro Reflecta Bronze. A marcenaria interna (MDF Cinza Sagrado) foi rigorosamente paginada no 3D para otimizar os cortes das chapas na vida real. Iluminação interna acionada por sensores em cada prateleira.",
            "materiais": ["Vidro Reflecta Bronze", "MDF Cinza Sagrado", "Alumínio Preto"],
            "software": "SketchUp + Enscape",
            "tempo_render": "1h 20m (4K)",
            "img": "https://images.unsplash.com/photo-1595428774223-ef52624120d2?q=80&w=1200"
        },
        {
            "id": "INT-009",
            "titulo": "Quarto Infantil Lúdico",
            "categoria": "Dormitório",
            "estilo": "Lúdico",
            "descricao_curta": "Marcenaria funcional com nichos coloridos, bicama e cantinho de estudos.",
            "descricao_longa": "Projeto infantil focado em ergonomia e segurança. O render detalha os cantos arredondados da marcenaria, simulando o acabamento impecável em laca. A paleta de cores pastéis foi configurada com valores exatos de RGB para garantir a fidelidade da tinta no render final. Destaque para a iluminação suave e sombras difusas para passar aconchego.",
            "materiais": ["Laca Rosa Pastel", "MDF Carvalho Munique", "Algodão Orgânico"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "3h 10m (4K)",
            "img": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?q=80&w=1200"
        },
        {
            "id": "INT-010",
            "titulo": "Sala de Jantar Elegance",
            "categoria": "Living",
            "estilo": "Clássico",
            "descricao_curta": "Buffet sob medida com portas em palhinha natural indiana e tampo de pedra.",
            "descricao_longa": "Uma sala de jantar que respira sofisticação. A marcenaria do buffet apresenta um dos maiores desafios do 3D: a renderização realista da textura da palhinha natural indiana vazada. O uso de mapas de Opacidade e Normal Bump garantiu o realismo fotográfico. A cena é iluminada por um pendente escultural que lança sombras desenhadas na parede.",
            "materiais": ["Palhinha Indiana", "MDF Nogueira Borges", "Mármore Travertino"],
            "software": "SketchUp + V-Ray 6",
            "tempo_render": "4h 40m (4K)",
            "img": "https://images.unsplash.com/photo-1617806118233-18e16208a50a?q=80&w=1200"
        },
        {
            "id": "INT-011",
            "titulo": "Adega Privativa",
            "categoria": "Área de Lazer",
            "estilo": "Rústico Moderno",
            "descricao_curta": "Nichos tipo colmeia para vinhos, climatização e revestimento em tijolos.",
            "descricao_longa": "Subsolo transformado em uma adega de alto padrão. O espaço exige pouca luz para a conservação dos vinhos, o que no 3D gera ruído (noise). Utilizamos algoritmos avançados de Denoising de Inteligência Artificial do V-Ray para limpar a imagem. A marcenaria foi simulada com lâminas de madeira natural Cumaru, destacando seus veios fortes e orgânicos.",
            "materiais": ["Madeira Maciça Cumaru", "Tijolo Inglês", "Vidro Duplo Termoacústico"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "5h 50m (4K)",
            "img": "https://images.unsplash.com/photo-1510626176961-4b57d4fbad03?q=80&w=1200"
        },
        {
            "id": "INT-012",
            "titulo": "Hall de Entrada Minimal",
            "categoria": "Circulação",
            "estilo": "Minimalista",
            "descricao_curta": "Aparador suspenso slim e painel inteiriço de espelhos bisotados.",
            "descricao_longa": "O desafio de renderizar espaços pequenos é a distorção da câmera. Utilizamos lentes de 35mm no software para evitar a aparência de 'olho de peixe', mantendo a elegância. O aparador suspenso possui apenas 12cm de espessura com gavetas de toque (fecho-toque). A parede lateral inteira é um espelho que duplica visualmente a passagem.",
            "materiais": ["MDF Lacca Cetin", "Espelho Prata Bisotado", "Piso em Granito"],
            "software": "SketchUp + Corona",
            "tempo_render": "2h 15m (4K)",
            "img": "https://images.unsplash.com/photo-1583847268964-b28dc2f51ac9?q=80&w=1200"
        },
        {
            "id": "INT-013",
            "titulo": "Lavanderia Organizada",
            "categoria": "Serviço",
            "estilo": "Funcional",
            "descricao_curta": "Armários aéreos totais, tulhas embutidas e cabideiro de secagem rápida.",
            "descricao_longa": "Provar que áreas de serviço também podem ser de alto padrão. Marcenaria técnica desenhada respeitando as áreas de ventilação das máquinas de lavar. Simulação do uso de chapa em MDF Branco Ártico, com rodapés em alumínio para evitar danos por água. Modelagem altamente detalhada, incluindo cesto de roupas basculante interno.",
            "materiais": ["MDF Branco Ártico", "Bancada em Corian", "Rodapés de Alumínio"],
            "software": "SketchUp + Enscape",
            "tempo_render": "40m (4K)",
            "img": "https://images.unsplash.com/photo-1521783593447-5702b9bfd267?q=80&w=1200"
        },
        {
            "id": "INT-014",
            "titulo": "Biblioteca Home",
            "categoria": "Escritório",
            "estilo": "Clássico Modernizado",
            "descricao_curta": "Estante de pé-direito duplo com escada rolante metálica e iluminação linear.",
            "descricao_longa": "A obra-prima deste ambiente é a estante do piso ao teto com quase 6 metros de altura. O render utilizou instanciamento proxy para popular as estantes com centenas de livros 3D sem travar o processamento da máquina. A marcenaria foi renderizada usando textura de Carvalho Natural, iluminada uniformemente por trilhos eletrificados pretos.",
            "materiais": ["MDF Carvalho Natural", "Estrutura Metálica Preta", "Piso Vinílico"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "6h 30m (4K)",
            "img": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?q=80&w=1200"
        },
        {
            "id": "INT-015",
            "titulo": "Recepção de Clínica Médica",
            "categoria": "Comercial",
            "estilo": "Comercial Premium",
            "descricao_curta": "Balcão orgânico em curvas com filetes de LED e materiais laváveis.",
            "descricao_longa": "Marcenaria comercial de alta exigência higiênica. O balcão principal foi desenhado com curvas suaves (modelagem em SubD) revestidas em Fórmica Branca Brilhante. A base do balcão possui um recuo com LED azul para criar sensação de flutuação. O render teve pós-produção focada em realçar a limpeza e assepsia do ambiente sem parecer um hospital frio.",
            "materiais": ["Laminado Melamínico Branco", "MDF madeirado claro", "Piso Porcelanato"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "2h 45m (4K)",
            "img": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?q=80&w=1200"
        }
    ]

    exteriores = [
        {
            "id": "EXT-001",
            "titulo": "Residência Contemporânea",
            "categoria": "Fachada",
            "estilo": "Contemporâneo",
            "descricao_curta": "Fachada com brises amadeirados e iluminação externa cênica.",
            "descricao_longa": "Projeto arquitetônico residencial destacando volumes sobrepostos. O grande diferencial desta imagem é o uso de brises verticais em imitação de madeira, modelados individualmente para gerar sombras perfeitamente anguladas no pôr do sol. A vegetação foi renderizada utilizando assets da biblioteca Chaos Cosmos em altíssima resolução.",
            "materiais": ["Brises em Alumínio Madeirado", "Concreto Aparente", "Esquadrias Pretas"],
            "software": "SketchUp + V-Ray + Chaos Cloud",
            "tempo_render": "40m (Cloud 4K)",
            "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=1200"
        },
        {
            "id": "EXT-002",
            "titulo": "Área de Lazer e Piscina",
            "categoria": "Área de Lazer",
            "estilo": "Tropical Chic",
            "descricao_curta": "Deck em madeira natural nivelado com borda infinita da piscina.",
            "descricao_longa": "Renderização externa complexa focada na física da água. Os reflexos do céu HDRI, as cáusticas geradas pela luz do sol atravessando a água da piscina e o mapeamento realista do deck de madeira Itaúba com imperfeições criaram um resultado hiper-realista. A marcenaria de apoio da área de churrasco integra-se perfeitamente ao deck.",
            "materiais": ["Deck Madeira Itaúba", "Pastilha Cerâmica", "Mármore Branco"],
            "software": "3ds Max + Corona",
            "tempo_render": "7h 00m (4K)",
            "img": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?q=80&w=1200"
        },
        {
            "id": "EXT-003",
            "titulo": "Fachada Corporativa Glass",
            "categoria": "Comercial",
            "estilo": "Corporativo",
            "descricao_curta": "Uso intensivo de pele de vidro e perfis de alumínio preto no contexto urbano.",
            "descricao_longa": "Edifício comercial focado na transparência e reflexo. A fachada em Pele de Vidro Refletivo exigiu a modelagem do ambiente interno (escritórios falsos) para que o vidro não parecesse 'cego' no render. Adicionamos contexto urbano, carros, asfalto realista com texturas PBR molhadas e pedestres desfocados no Photoshop para dar movimento à cena.",
            "materiais": ["Pele de Vidro Prata", "ACM Preto", "Concreto"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "5h 45m (4K)",
            "img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1200"
        },
        {
            "id": "EXT-004",
            "titulo": "Casa de Campo Sustentável",
            "categoria": "Fachada",
            "estilo": "Rústico",
            "descricao_curta": "Integração total com a natureza, pedras irregulares e cobertura em telha shingle.",
            "descricao_longa": "O desafio arquitetônico desta cena de campo foi a integração com o bioma ao redor. Usamos o Forest Pack (Plugin do 3ds Max) para distribuir milhares de árvores, gramíneas e pedras no terreno sem travar o computador. A casa mistura madeira maciça nas vigas e revestimento em pedra Moledo na base.",
            "materiais": ["Pedra Moledo", "Vigas de Eucalipto", "Telha Shingle"],
            "software": "3ds Max + Corona + Forest Pack",
            "tempo_render": "8h 30m (4K)",
            "img": "https://images.unsplash.com/photo-1500313830540-7b6650a74fd0?q=80&w=1200"
        },
        {
            "id": "EXT-005",
            "titulo": "Rooftop Lounge Urbano",
            "categoria": "Área de Lazer",
            "estilo": "Urbano Moderno",
            "descricao_curta": "Mobiliário externo resistente a intempéries e vista skyline noturna.",
            "descricao_longa": "Área social localizada no 20º andar de um edifício. O render explora a iluminação noturna (Blue Hour), contrastando as luzes frias da cidade ao fundo com a iluminação quente e acolhedora dos cordões de luz e balizadores embutidos na marcenaria de piso (deck sintético).",
            "materiais": ["Deck Sintético Ecológico", "Mobiliário Corda Náutica", "Vidro Temperado"],
            "software": "SketchUp + Enscape",
            "tempo_render": "1h 15m (4K)",
            "img": "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?q=80&w=1200"
        },
        {
            "id": "EXT-006",
            "titulo": "Entrada de Condomínio",
            "categoria": "Comercial",
            "estilo": "Imponente",
            "descricao_curta": "Guarita blindada com fachada frontal revestida em chapa de aço corten.",
            "descricao_longa": "Apresentação para lançamento imobiliário. O projeto de portaria exigia um ar de extrema segurança sem perder a elegância. O revestimento em Aço Corten foi mapeado cuidadosamente no 3D para evitar repetições na textura de ferrugem, criando um padrão altamente orgânico. As palmeiras iluminadas de baixo para cima orientam o olhar.",
            "materiais": ["Aço Corten", "Vidro Blindado Escuro", "Pedra Portuguesa"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "3h 40m (4K)",
            "img": "https://images.unsplash.com/photo-1590060417603-eb1593d04976?q=80&w=1200"
        },
        {
            "id": "EXT-007",
            "titulo": "Residência Estudo Luminotécnico",
            "categoria": "Fachada",
            "estilo": "Contemporâneo Noturno",
            "descricao_curta": "Fachada noturna com ênfase no estudo de fachos de luz e perfis embutidos.",
            "descricao_longa": "Este render não focou apenas na arquitetura, mas no estudo luminotécnico. Foram configurados IES Profiles (arquivos reais das lâmpadas de fabricantes de iluminação) para garantir que os fachos de luz que banham a textura da fachada no render sejam exatamente iguais ao que acontecerá na obra real à noite.",
            "materiais": ["Tinta Acrílica Branca", "MDF Naval Externo", "Iluminação LED IES"],
            "software": "3ds Max + V-Ray",
            "tempo_render": "6h 10m (4K)",
            "img": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=1200"
        },
        {
            "id": "EXT-008",
            "titulo": "Industrial Loft Exterior",
            "categoria": "Fachada",
            "estilo": "Industrial Style",
            "descricao_curta": "Retrofit de galpão transformado em loft de luxo com janelas quadriculadas.",
            "descricao_longa": "Render de inspiração nova-iorquina (Brooklyn Style). O desafio foi construir a textura dos tijolinhos ingleses aparentes desgastados pelo tempo. Utilizamos técnicas avançadas de Displacement no V-Ray para que os rejuntes dos tijolos realmente tivessem profundidade 3D, interagindo com as sombras lançadas pelos perfis metálicos das janelas.",
            "materiais": ["Tijolo de Demolição", "Metalon Grafite", "Vidro Canelado"],
            "software": "SketchUp + V-Ray 6",
            "tempo_render": "4h 50m (4K)",
            "img": "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?q=80&w=1200"
        },
        {
            "id": "EXT-009",
            "titulo": "Varanda Gourmet de Apartamento",
            "categoria": "Área de Lazer",
            "estilo": "Moderna",
            "descricao_curta": "Nivelamento de piso, fechamento em vidro tipo Reiki e painel ripado externo.",
            "descricao_longa": "Uma sacada de 18m² transformada em extensão da sala. A marcenaria projetada aqui utiliza MDF Naval resistente à insolação, com o painel ripado escondendo as máquinas de ar-condicionado. A iluminação de final de tarde entra pelas frestas dos fechamentos de vidro, criando um jogo de luz no piso de porcelanato amadeirado.",
            "materiais": ["MDF Naval Amadeirado", "Porcelanato Amadeirado", "Sistema Reiki"],
            "software": "3ds Max + Corona Renderer",
            "tempo_render": "4h 20m (4K)",
            "img": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?q=80&w=1200"
        },
        {
            "id": "EXT-010",
            "titulo": "Pátio Interno e Jardim de Inverno",
            "categoria": "Área Externa",
            "estilo": "Zen Asiático",
            "descricao_curta": "Criação de microclima com espelho d'água, pérgola de cumaru e jardim vertical.",
            "descricao_longa": "O pulmão da casa. Um espaço no meio da arquitetura dedicado ao relaxamento. O render inclui um espelho d'água escuro que reflete o céu e uma pérgola em vigas de Cumaru protegida por vidro. A modelagem botânica foi intensa, simulando espécies da Mata Atlântica no jardim vertical anexado ao muro principal.",
            "materiais": ["Madeira Cumaru Maciça", "Pedra Vulcânica", "Jardim Vertical Realista"],
            "software": "SketchUp + V-Ray",
            "tempo_render": "5h 15m (4K)",
            "img": "https://images.unsplash.com/photo-1510798831971-661eb04b3739?q=80&w=1200"
        }
    ]
    return interiores, exteriores

# ==============================================================================
# 4. COMPONENTES VISUAIS REUTILIZÁVEIS
# ==============================================================================
def render_project_card(proj, tipo):
    """Gera um card de projeto clicável que altera o estado para detalhamento."""
    with st.container():
        st.markdown(f"""
            <div class="project-card">
                <div class="img-container">
                    <img src="{proj['img']}" alt="{proj['titulo']}">
                </div>
                <div class="card-content">
                    <div class="project-title">{proj['titulo']}</div>
                    <div style="font-size: 0.8rem; color: #d4af37; margin-bottom: 10px; text-transform: uppercase;">{proj['categoria']} | {proj['estilo']}</div>
                    <div class="project-desc">{proj['descricao_curta']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        # O botão invisível do Streamlit sobreposto via colunas para acionar navegação
        if st.button(f"VER DETALHES", key=f"btn_{proj['id']}"):
            st.session_state['projeto_selecionado'] = proj
            st.session_state['page'] = 'Detalhes do Projeto'
            st.rerun()

# ==============================================================================
# 5. PÁGINAS DO SISTEMA
# ==============================================================================
def page_home():
    """Tela Inicial do Palladium Studio"""
    st.markdown("<h1 style='text-align:center; font-size:4.5rem; margin-bottom:0; margin-top:20px;'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; font-size:1.1rem; letter-spacing:8px; margin-top:5px; margin-bottom:40px;'>ARCHVIZ DE ALTO PADRÃO</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?q=80&w=1500", use_container_width=True)
    
    st.markdown("<br><h2 style='text-align:center; color:#d4af37 !important;'>O Seu Projeto, Antes de Existir.</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align:center; color:#aaa; max-width: 900px; margin: 0 auto; line-height:1.8;'>
        Compreendemos a linguagem das marcenarias e dos escritórios de arquitetura. O Palladium Studio não apenas gera imagens, 
        nós construímos simulações fotorealistas. Mapeamos os catálogos reais (Arauco, Guararapes, Duratex), 
        estudamos o comportamento da luz natural e artificial, e entregamos uma ferramenta de vendas implacável 
        que garante a aprovação rápida do seu cliente final.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: 
        st.markdown("<div style='text-align:center; padding:30px; background:#111; border-radius:6px; border:1px solid #222;'><h1 style='color:#d4af37 !important; font-size:3.5rem; margin:0;'>4K</h1><p style='color:#888; letter-spacing:2px; font-size:0.9rem;'>ULTRA RESOLUÇÃO</p></div>", unsafe_allow_html=True)
    with c2: 
        st.markdown("<div style='text-align:center; padding:30px; background:#111; border-radius:6px; border:1px solid #222;'><h1 style='color:#d4af37 !important; font-size:3.5rem; margin:0;'>25+</h1><p style='color:#888; letter-spacing:2px; font-size:0.9rem;'>PROJETOS ENTREGUES</p></div>", unsafe_allow_html=True)
    with c3: 
        st.markdown("<div style='text-align:center; padding:30px; background:#111; border-radius:6px; border:1px solid #222;'><h1 style='color:#d4af37 !important; font-size:3.5rem; margin:0;'>100%</h1><p style='color:#888; letter-spacing:2px; font-size:0.9rem;'>FIDELIDADE TÉCNICA</p></div>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("VISITAR A GALERIA DE PROJETOS", use_container_width=True):
            st.session_state['page'] = 'Portfólio'
            st.rerun()

def page_portfolio():
    """Tela de Catálogo de Projetos em Grid"""
    int_db, ext_db = carregar_banco_de_dados()
    
    st.markdown("<h1 style='font-size:2.5rem; margin-bottom:5px;'>Portfólio Seletivo</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666; margin-bottom:40px;'>Clique em 'Ver Detalhes' em qualquer projeto para acessar o relatório técnico do render.</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='border-left: 4px solid #d4af37; padding-left: 15px; margin-bottom:20px;'>DESIGN DE INTERIORES E MARCENARIA</h2>", unsafe_allow_html=True)
    
    # Criando o sistema de Grid para Interiores
    cols_int = st.columns(3)
    for i, proj in enumerate(int_db):
        with cols_int[i % 3]:
            render_project_card(proj, "int")
            
    st.markdown("<br><hr style='border-color:#333;'><br>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='border-left: 4px solid #d4af37; padding-left: 15px; margin-bottom:20px;'>ARQUITETURA EXTERIOR</h2>", unsafe_allow_html=True)
    
    # Criando o sistema de Grid para Exteriores
    cols_ext = st.columns(3) # Mantive 3 colunas para padronizar e dar volume na tela
    for i, proj in enumerate(ext_db):
        with cols_ext[i % 3]:
            render_project_card(proj, "ext")

def page_projeto_detalhe():
    """Tela de visualização profunda de um único projeto"""
    proj = st.session_state.get('projeto_selecionado')
    
    if not proj:
        st.session_state['page'] = 'Portfólio'
        st.rerun()
        return

    # Botão de voltar elegante
    if st.button("← VOLTAR PARA O PORTFÓLIO"):
        st.session_state['projeto_selecionado'] = None
        st.session_state['page'] = 'Portfólio'
        st.rerun()
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.image(proj['img'], use_container_width=True)
    
    st.markdown(f"<h1 style='font-size:3rem; margin-top:20px; margin-bottom:0;'>{proj['titulo']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#d4af37; letter-spacing:2px; text-transform:uppercase;'>{proj['categoria']} | {proj['estilo']}</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    col_desc, col_tech = st.columns([2, 1])
    
    with col_desc:
        st.markdown("<h3>O Desafio e a Solução</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#aaa; line-height:1.8; font-size:1.05rem;'>{proj['descricao_longa']}</p>", unsafe_allow_html=True)
        
    with col_tech:
        st.markdown("""
            <div style='background:#111; border:1px solid #222; padding:25px; border-radius:6px;'>
                <h4 style='color:#d4af37 !important; border-bottom:1px solid #333; padding-bottom:10px; margin-top:0;'>Ficha Técnica do Render</h4>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:2px;'><b>Software Engine:</b></p><p style='color:#ccc; margin-bottom:15px;'>{proj['software']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:2px;'><b>Tempo de Renderização:</b></p><p style='color:#ccc; margin-bottom:15px;'>{proj['tempo_render']}</p>", unsafe_allow_html=True)
        
        st.markdown("<p style='color:#888; font-size:0.9rem; margin-bottom:8px;'><b>Materiais Simulados (PBR):</b></p>", unsafe_allow_html=True)
        for mat in proj['materiais']:
            st.markdown(f"<span style='display:inline-block; background:#1a1a1a; border:1px solid #333; color:#aaa; font-size:0.8rem; padding:4px 8px; border-radius:4px; margin:2px;'>{mat}</span>", unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)

def page_servicos():
    """Tela de Pacotes e Valores do Estúdio"""
    st.markdown("<h1 style='text-align:center;'>Nossos Pacotes</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; margin-bottom:50px;'>Soluções direcionadas para quem busca escalar as vendas de projeto.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
            <div class='pricing-card'>
                <h3 class='pricing-title'>ArchViz Marcenaria</h3>
                <p style='color:#aaa; font-size:0.9rem; min-height:40px;'>Ideal para quem já tem o projeto em Promob/SketchUp.</p>
                <div class='pricing-features'>
                    • Limpeza e Otimização da Malha<br>
                    • Aplicação de Texturas Reais (MDF)<br>
                    • Estudo de Iluminação<br>
                    • 3 Imagens Estáticas em 4K<br>
                    • 1 Rodada de Alteração (Baixa Res.)
                </div>
            </div>
        """, unsafe_allow_html=True)
        link = "https://wa.me/5514998405046?text=Gostaria%20de%20saber%20mais%20sobre%20o%20pacote%20ArchViz%20Marcenaria."
        st.markdown(f'<a href="{link}" target="_blank" class="btn-outline">SOLICITAR AVALIAÇÃO</a>', unsafe_allow_html=True)

    with c2:
        st.markdown("""
            <div class='pricing-card' style='border-color: #d4af37; transform: scale(1.05); box-shadow: 0 0 30px rgba(212,175,55,0.1);'>
                <div style='background:#d4af37; color:#000; font-weight:bold; font-size:0.8rem; padding:5px; margin-top:-40px; margin-bottom:20px; border-radius:4px;'>MAIS VENDIDO</div>
                <h3 class='pricing-title'>ArchViz Arquiteto</h3>
                <p style='color:#aaa; font-size:0.9rem; min-height:40px;'>Criação completa a partir da sua planta baixa ou DWG.</p>
                <div class='pricing-features'>
                    • Modelagem 3D Completa (Paredes, Teto, Móveis)<br>
                    • Decoração e Produção de Cena VIP<br>
                    • Iluminação Cenográfica Avançada<br>
                    • 4 Imagens Estáticas em 4K<br>
                    • 2 Rodadas de Alterações Inclusas
                </div>
            </div>
        """, unsafe_allow_html=True)
        link = "https://wa.me/5514998405046?text=Gostaria%20de%20saber%20mais%20sobre%20o%20pacote%20ArchViz%20Arquiteto."
        st.markdown(f'<a href="{link}" target="_blank" class="btn-gold">FALAR COM O ESTÚDIO</a>', unsafe_allow_html=True)

    with c3:
        st.markdown("""
            <div class='pricing-card'>
                <h3 class='pricing-title'>Imersão 360º</h3>
                <p style='color:#aaa; font-size:0.9rem; min-height:40px;'>O máximo impacto comercial para o seu cliente.</p>
                <div class='pricing-features'>
                    • Modelagem 3D Otimizada<br>
                    • Renderização Esférica Panorâmica<br>
                    • Link Interativo (O cliente olha ao redor no celular)<br>
                    • 2 Imagens Estáticas em 4K de bônus<br>
                    • Hospedagem do Tour Virtual por 6 meses
                </div>
            </div>
        """, unsafe_allow_html=True)
        link = "https://wa.me/5514998405046?text=Gostaria%20de%20saber%20mais%20sobre%20o%20pacote%20Imersao%20360."
        st.markdown(f'<a href="{link}" target="_blank" class="btn-outline">SOLICITAR AVALIAÇÃO</a>', unsafe_allow_html=True)

def page_metodologia():
    """Tela Explicativa do Funil e Pipeline 3D"""
    st.markdown("<h1>Nossa Metodologia</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; font-size:1.1rem;'>Do recebimento do arquivo à entrega do render fotorealista.</p><br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("""
            <div class='timeline-step'>
                <div class='timeline-title'>1. Briefing e Recebimento do Arquivo</div>
                <div class='timeline-desc'>Recebemos seu projeto em SketchUp, Promob ou apenas a planta baixa. Discutimos referências, estilo de decoração e paleta de materiais do seu cliente.</div>
            </div>
            <div class='timeline-step'>
                <div class='timeline-title'>2. Clay Render (Aprovação de Câmera)</div>
                <div class='timeline-desc'>Realizamos a otimização da malha 3D e enviamos imagens "brancas" (Clay Render) apenas com o estudo da luz natural e posição das câmeras para sua aprovação geométrica.</div>
            </div>
            <div class='timeline-step'>
                <div class='timeline-title'>3. Setup de Materiais PBR e Decoração</div>
                <div class='timeline-desc'>Aplicamos os mapas de textura físicos (PBR - Physically Based Rendering). Isso significa que uma madeira terá reflexo diferente de um metal ou couro, garantindo realismo. Populamos a cena com decorações de alto nível.</div>
            </div>
            <div class='timeline-step'>
                <div class='timeline-title'>4. Prévias em Baixa Resolução</div>
                <div class='timeline-desc'>Enviamos as primeiras imagens já texturizadas e iluminadas (em qualidade baixa, para ser rápido) para que você faça os ajustes finos antes do render final pesado.</div>
            </div>
            <div class='timeline-step' style='border-left: 2px solid transparent;'>
                <div class='timeline-title'>5. Processamento 4K e Pós-Produção</div>
                <div class='timeline-desc'>Rodamos as imagens no motor de renderização (V-Ray, Corona). O material bruto vai para o Photoshop para correção de cores, contraste, brilho global (LUTs) e adição de nitidez. O projeto final é entregue via link de alta velocidade.</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("https://images.unsplash.com/photo-1542621323-23e5361b1716?q=80&w=800", caption="Configuração de Materiais no Engine", use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?q=80&w=800", caption="Foco e Enquadramento Técnico", use_container_width=True)

def page_contato():
    """Tela de Contato Profissional"""
    st.markdown("<h1>Direto ao Ponto.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; font-size:1.1rem; margin-bottom:40px;'>Entre em contato para avaliar projetos ou discutir parcerias de longo prazo.</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1.2])
    
    with c1:
        st.markdown("""
            <div style='background:#111; padding:40px; border-radius:6px; border:1px solid #222;'>
                <h3 style='margin-top:0; color:#d4af37 !important;'>Central de Atendimento</h3>
                <p style='color:#aaa; line-height:2;'>
                    📍 <b>Sede Física:</b> Ourinhos, SP<br>
                    🌍 <b>Atendimento:</b> Todo o Brasil (Remoto)<br>
                    📧 <b>E-mail:</b> comercial@palladiumstudio.com<br>
                    📱 <b>WhatsApp Oficial:</b> (14) 99840-5046
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        link = "https://wa.me/5514998405046"
        st.markdown(f'<a href="{link}" target="_blank" class="btn-gold" style="margin-top:20px;">INICIAR CONVERSA NO WHATSAPP</a>', unsafe_allow_html=True)

    with c2:
        st.markdown("<h3 style='margin-top:0;'>Informações Comuns</h3>", unsafe_allow_html=True)
        with st.expander("Qual o prazo médio de entrega?"):
            st.write("Para projetos de pacote 'ArchViz Marcenaria' (1 a 2 ambientes), a primeira prévia é entregue em até 48 horas úteis após o recebimento completo dos arquivos e briefing.")
        with st.expander("Quais os métodos de pagamento aceitos?"):
            st.write("Trabalhamos com Pix ou Transferência Bancária. O formato padrão do mercado é 50% de sinalização para início dos trabalhos e 50% após a aprovação final, na entrega dos arquivos 4K sem marca d'água.")
        with st.expander("Fazem modelagem do zero apenas com planta baixa?"):
            st.write("Sim! No pacote 'ArchViz Arquiteto' nós levantamos as paredes 3D, inserimos os móveis conforme as medidas do seu croqui e aplicamos o layout solicitado.")
        with st.expander("Vocês entregam o arquivo fonte (3D)?"):
            st.write("A entrega padrão do estúdio é a mídia final (Imagens JPG 4K ou Links 360). O arquivo fonte (.skp, .max) configurado com nossos assets de estúdio não é comercializado, sendo propriedade intelectual do Palladium Studio.")

# ==============================================================================
# 6. ROTEADOR PRINCIPAL E MENU LATERAL
# ==============================================================================
def main():
    injetar_css_premium()
    
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; font-size: 2.2rem;'>PALLADIUM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#555; font-size:0.7rem; letter-spacing:5px;'>ARCHVIZ STUDIO</p>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Sistema de navegação que limpa seleções de projetos antigos ao mudar de aba
        if st.button("INÍCIO"): 
            st.session_state['projeto_selecionado'] = None
            st.session_state['page'] = 'Início'
        if st.button("PORTFÓLIO"): 
            st.session_state['projeto_selecionado'] = None
            st.session_state['page'] = 'Portfólio'
        if st.button("PACOTES"): 
            st.session_state['projeto_selecionado'] = None
            st.session_state['page'] = 'Pacotes'
        if st.button("METODOLOGIA"): 
            st.session_state['projeto_selecionado'] = None
            st.session_state['page'] = 'Metodologia'
        if st.button("CONTATO"): 
            st.session_state['projeto_selecionado'] = None
            st.session_state['page'] = 'Contato'
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        link_wpp = "https://wa.me/5514998405046"
        st.markdown(f'<a href="{link_wpp}" target="_blank" class="btn-gold" style="padding: 15px;">FALAR COM EQUIPE</a>', unsafe_allow_html=True)
        
        st.markdown("""
            <div style='position: absolute; bottom: 20px; width: 100%; text-align: center; color: #333; font-size: 0.65rem; letter-spacing: 1px;'>
                PALLADIUM STUDIO © 2026<br>
                ARCHITECTURE VISUALIZATION
            </div>
        """, unsafe_allow_html=True)

    # Roteador de Telas principal
    page = st.session_state['page']
    
    with st.container():
        st.markdown("<div style='padding: 1% 4% 5% 4%;'>", unsafe_allow_html=True)
        if page == 'Início':
            page_home()
        elif page == 'Portfólio':
            page_portfolio()
        elif page == 'Detalhes do Projeto':
            page_projeto_detalhe()
        elif page == 'Pacotes':
            page_servicos()
        elif page == 'Metodologia':
            page_metodologia()
        elif page == 'Contato':
            page_contato()
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
