"""
PALLADIUM STUDIO - PORTFÓLIO WEB ENGINE v3.0
Desenvolvido para: Pedro Teixeira | Palladium Studio
Arquitetura: Programação Orientada a Objetos (POO) com Streamlit
Foco: Alta Marcenaria & Architectural Visualization (ArchViz)
"""

import streamlit as st
import time
import streamlit.components.v1 as components

# ==============================================================================
# CLASS: DATABASE_MANAGER
# Responsável pela gestão, curadoria e integridade dos dados dos projetos.
# ==============================================================================
class DatabaseManager:
    """
    Gerencia o repositório central de ativos (Imagens, Descrições e Dados Técnicos).
    Todos os 25 projetos são estruturados aqui com metadados detalhados.
    """

    @staticmethod
    def get_interiores():
        """
        Retorna a lista de 15 projetos de interiores com descrições técnicas precisas.
        Cada projeto contém 4 ângulos de câmera (IDs únicos).
        """
        return [
            {
                "id": "INT_001",
                "titulo": "Cozinha Minimalista Nero",
                "categoria": "Cozinha",
                "estilo": "Minimalista",
                "descricao_curta": "MDF Preto Silk com puxadores cava integrados e iluminação 3000K.",
                "descricao_longa": "O projeto foca na continuidade visual. A marcenaria utiliza o padrão Preto Silk (Guararapes) com detalhamento de puxador tipo cava 45 graus oculto, garantindo que nenhuma ferragem interfira no design monolítico. A bancada em quartzo cinza absoluto foi renderizada com mapa de rugosidade (Roughness) para reflexos realistas.",
                "materiais": ["MDF Preto Silk", "Quartzo Cinza", "Puxador Cava", "LED 3000K"],
                "software": "SketchUp + V-Ray 6 + Photoshop",
                "tempo_render": "3h 45m",
                "imgs": [
                    "https://images.unsplash.com/photo-1556911220-e15022357539?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556911261-6bd341186b2f?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556909190-eccf4a8bf97a?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_002",
                "titulo": "Suíte Master Premium",
                "categoria": "Dormitório",
                "estilo": "Contemporâneo",
                "descricao_curta": "Painel ripado em MDF Freijó e cabeceira em linho cru.",
                "descricao_longa": "Estudo de texturas orgânicas. O painel principal foi modelado com ripados de 1.5cm de espessura. A renderização destaca a iluminação wall-washer incidindo sobre a textura do linho da cabeceira. O uso de materiais PBR garante que o brilho da laca cinza nos criados-mudos seja fisicamente correto.",
                "materiais": ["MDF Freijó", "Linho Cru", "Laca Cinza Fosca"],
                "software": "3ds Max + Corona Renderer",
                "tempo_render": "5h 20m",
                "imgs": [
                    "https://images.unsplash.com/photo-1616594111750-4744bda7e9a2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1560185007-cde436f6a4d0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_003",
                "titulo": "Living Pé-Direito Duplo",
                "categoria": "Estar",
                "estilo": "Luxo",
                "descricao_curta": "Ambiente integrado com painéis de pedra e marcenaria em carvalho.",
                "descricao_longa": "O desafio técnico aqui foi a iluminação global. Com grandes aberturas envidraçadas, o render simula a entrada de luz natural das 16h. Os painéis de madeira em Carvalho Natural emolduram o pé-direito duplo, integrando-se ao porcelanato polido de grande formato no piso.",
                "materiais": ["MDF Carvalho", "Mármore Calacatta", "Vidro Laminado"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "4h 10m",
                "imgs": [
                    "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600607688066-2405894e4bd5?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_004",
                "titulo": "Gabinete SPA Banho",
                "categoria": "Banheiro",
                "estilo": "Clean",
                "descricao_curta": "Marcenaria técnica em MDF Branco Ultra com puxadores cava.",
                "descricao_longa": "Design focado em assepsia e durabilidade. O gabinete suspenso utiliza MDF Ultra (resistente à umidade) com acabamento branco fosco. A cuba é esculpida em mármore, exigindo configuração de reflexos complexos e refração no espelho infinito retroiluminado.",
                "materiais": ["MDF Ultra", "Mármore Branco", "Metais Gold"],
                "software": "3ds Max + Corona",
                "tempo_render": "6h 15m",
                "imgs": [
                    "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1603912975949-c1e1e0a29363?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1620626011761-9963d7b59a7a?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_005",
                "titulo": "Varanda Gourmet Graphite",
                "categoria": "Lazer",
                "estilo": "Moderno",
                "descricao_curta": "Churrasqueira integrada com acabamento em MDF Grafite.",
                "descricao_longa": "A varanda gourmet foi pensada para o convívio social. A marcenaria técnica em tons de cinza grafite (Duratex) oculta a área de serviço integrada. O render destaca o contraste entre a madeira rústica da mesa e o acabamento liso e técnico dos armários superiores.",
                "materiais": ["MDF Grafite", "Madeira de Demolição", "Metalon"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "4h 30m",
                "imgs": [
                    "https://images.unsplash.com/photo-1565538810643-b5bdb714032a?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556912998-c57cc6b63ce7?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1565183928294-7063f23ce0f8?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_006",
                "titulo": "Home Office Executivo",
                "categoria": "Escritório",
                "estilo": "Corporativo",
                "descricao_curta": "Estante com nichos iluminados e mesa em MDF Freijó.",
                "descricao_longa": "Otimizado para videoconferências e alta produtividade. A estante ao fundo possui iluminação técnica embutida que valoriza os objetos sem causar reflexos na tela do computador. A mesa flutuante em MDF Freijó (Arauco) reforça a sobriedade do ambiente corporativo.",
                "materiais": ["MDF Freijó", "Laca Preta", "LED Linear"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "3h 50m",
                "imgs": [
                    "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497215898141-86daaa72295d?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_007",
                "titulo": "Closet Walk-in Boutique",
                "categoria": "Dormitório",
                "estilo": "Luxo",
                "descricao_curta": "Portas em vidro reflecta e iluminação interna por sensores.",
                "descricao_longa": "Um closet transformado em vitrine. Não há portas cegas; a proteção é feita com esquadrias finas e Vidro Reflecta Bronze. A marcenaria interna em MDF Cinza Sagrado possui paginação rigorosa para otimização do corte das chapas na execução real.",
                "materiais": ["Vidro Reflecta", "MDF Cinza", "Esquadria Alumínio"],
                "software": "SketchUp + Enscape",
                "tempo_render": "1h 55m",
                "imgs": [
                    "https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618219944342-824e40a13285?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_008",
                "titulo": "Sala de Jantar Contemporânea",
                "categoria": "Estar",
                "estilo": "Elegante",
                "descricao_curta": "Buffet com palhinha indiana e tampo em pedra natural.",
                "descricao_longa": "O ponto focal é a marcenaria do buffet. O render foca no realismo da palhinha indiana vazada, utilizando mapas de opacidade precisos. O tampo em pedra natural recebe a luz direta de um pendente escultural, criando sombras suaves na cena.",
                "materiais": ["Palhinha Indiana", "Nogueira", "Mármore Travertino"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "5h 15m",
                "imgs": [
                    "https://images.unsplash.com/photo-1617806118233-18e16208a50a?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1540932239986-30128078f3b5?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_009",
                "titulo": "Dormitório Infantil Lúdico",
                "categoria": "Dormitório",
                "estilo": "Montessoriano",
                "descricao_curta": "Marcenaria arredondada em tons pastéis e laca premium.",
                "descricao_longa": "Foco total na segurança e ergonomia. A marcenaria técnica foi modelada com cantos arredondados e acabamento impecável em laca fosca. As cores pastéis foram calibradas no V-Ray para garantir a fidelidade técnica da pintura real solicitada.",
                "materiais": ["Laca Rosa", "MDF Carvalho Munique", "Algodão"],
                "software": "3ds Max + V-Ray",
                "tempo_render": "3h 40m",
                "imgs": [
                    "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1520699049698-acd2fccb8cc8?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1520699049698-acd2fccb8cc8?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1505692952047-1a78307da8f2?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_010",
                "titulo": "Adega em Madeira Cumaru",
                "categoria": "Lazer",
                "estilo": "Rústico Moderno",
                "descricao_curta": "Nichos colmeia climatizados em madeira maciça.",
                "descricao_longa": "Ambiente de baixa iluminação que exigiu processamento denso. A marcenaria em madeira maciça Cumaru contrasta com o revestimento de tijolo inglês ao fundo. O render foca na atmosfera aconchegante e nos reflexos das garrafas de vidro.",
                "materiais": ["Cumaru Maciço", "Tijolo Inglês", "Vidro Duplo"],
                "software": "3ds Max + V-Ray",
                "tempo_render": "6h 50m",
                "imgs": [
                    "https://images.unsplash.com/photo-1510626176961-4b57d4fbad03?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1585553616435-2dc0a54e271d?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1565183928294-7063f23ce0f8?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_011",
                "titulo": "Hall Minimal Bisotado",
                "categoria": "Circulação",
                "estilo": "Minimalista",
                "descricao_curta": "Aparador slim suspenso e painel espelhado.",
                "descricao_longa": "Tratamento de espaços pequenos. O aparador suspenso possui espessura de apenas 12cm com gavetas de toque. O uso de espelhos bisotados em toda a parede lateral amplia a percepção visual do ambiente de transição.",
                "materiais": ["MDF Lacca", "Espelho Prata", "Granito Polido"],
                "software": "SketchUp + Corona",
                "tempo_render": "2h 45m",
                "imgs": [
                    "https://images.unsplash.com/photo-1583847268964-b28dc2f51ac9?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618221118493-9cfa1a1c00da?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_012",
                "titulo": "Lavanderia Funcional",
                "categoria": "Serviço",
                "estilo": "Moderno",
                "descricao_curta": "Armários totais em MDF Branco Ártico com tulhas.",
                "descricao_longa": "Marcenaria técnica projetada para máxima organização. O render detalha os respiros necessários para máquinas de lavar e secar, além de tulhas embutidas para roupas. O MDF Branco Ártico confere limpeza visual ao ambiente de serviço.",
                "materiais": ["MDF Branco Ártico", "Bancada Corian", "Rodapés Alumínio"],
                "software": "SketchUp + Enscape",
                "tempo_render": "1h 10m",
                "imgs": [
                    "https://images.unsplash.com/photo-1521783593447-5702b9bfd267?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1584622781564-1d987f7333c1?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556911220-e15022357539?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_013",
                "titulo": "Biblioteca Pé-Direito Duplo",
                "categoria": "Escritório",
                "estilo": "Clássico Moderno",
                "descricao_curta": "Estante de 6 metros com escada metálica funcional.",
                "descricao_longa": "O destaque é a imponência da estante em Carvalho Natural que sobe dois níveis. O render utilizou proxies para povoar as estantes com livros 3D detalhados, iluminados por trilhos eletrificados pretos que emolduram a estrutura.",
                "materiais": ["MDF Carvalho", "Metal Preto", "Piso Vinílico"],
                "software": "3ds Max + Corona",
                "tempo_render": "6h 20m",
                "imgs": [
                    "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497215898141-86daaa72295d?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_014",
                "titulo": "Recepção Médica Premium",
                "categoria": "Comercial",
                "estilo": "Minimalista",
                "descricao_curta": "Balcão orgânico em marcenaria com filetes LED.",
                "descricao_longa": "Design comercial focado na recepção do paciente. O balcão possui curvas orgânicas revestidas em laminado melamínico de alta resistência. O render foca na iluminação suave e na assepsia transmitida pela paleta branca e amadeirada clara.",
                "materiais": ["Laminado Branco", "MDF Claro", "Porcelanato"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "3h 45m",
                "imgs": [
                    "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_015",
                "titulo": "Hometheater Laca Polida",
                "categoria": "Living",
                "estilo": "Luxo Moderno",
                "descricao_curta": "Painel de TV em laca alto brilho e detalhes em couro.",
                "descricao_longa": "Análise técnica de reflexividade. O painel principal em Laca Alto Brilho exige múltiplas camadas de polimento virtual no V-Ray para refletir a iluminação zenital sem distorções, conferindo profundidade e luxo ao ambiente.",
                "materiais": ["Laca Alto Brilho", "MDF Grafite", "Couro Preto"],
                "software": "3ds Max + V-Ray",
                "tempo_render": "5h 55m",
                "imgs": [
                    "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1593910265171-ef6709849202?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618221118493-9cfa1a1c00da?auto=format&fit=crop&w=1200&q=80"
                ]
            }
        ]

    @staticmethod
    def get_exteriores():
        """
        Retorna a lista de 10 projetos de arquitetura externa.
        Curadoria de IDs focados em fachadas residenciais e comerciais.
        """
        return [
            {
                "id": "EXT_001",
                "titulo": "Fachada Brises Amadeirados",
                "categoria": "Residencial",
                "estilo": "Contemporâneo",
                "descricao_curta": "Volumes sobrepostos com brises verticais e concreto.",
                "descricao_longa": "O projeto residencial destaca a volumetria limpa. Os brises verticais modelados individualmente criam um jogo de luz e sombra dinâmico na fachada ao longo do dia. O render utiliza assets Chaos Cosmos para vegetação realista integrada ao concreto aparente.",
                "materiais": ["Alumínio Amadeirado", "Concreto", "Esquadria Preta"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "5h 30m",
                "imgs": [
                    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_002",
                "titulo": "Área de Lazer Tropical",
                "categoria": "Externo",
                "estilo": "Tropical Chic",
                "descricao_curta": "Deck em madeira natural e piscina com borda infinita.",
                "descricao_longa": "Estudo físico da água. O render detalha as cáusticas geradas pelo sol no fundo da piscina e os reflexos do céu no espelho d'água. O deck em Itaúba possui texturas PBR que mostram veios e imperfeições naturais da madeira maciça.",
                "materiais": ["Madeira Itaúba", "Pastilha Cerâmica", "Mármore Branco"],
                "software": "3ds Max + Corona Renderer",
                "tempo_render": "7h 45m",
                "imgs": [
                    "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_003",
                "titulo": "Corporativo Pele de Vidro",
                "categoria": "Comercial",
                "estilo": "Urbano",
                "descricao_curta": "Edifício em vidro espelhado com asfalto realista PBR.",
                "descricao_longa": "Foco na integração urbana. O render destaca o reflexo dos edifícios vizinhos na pele de vidro do prédio comercial. A pós-produção foi trabalhada para criar uma cena de pós-chuva, com asfalto molhado e reflexos urbanos intensos.",
                "materiais": ["Vidro Refletivo", "ACM Preto", "Concreto"],
                "software": "3ds Max + V-Ray",
                "tempo_render": "6h 55m",
                "imgs": [
                    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497215898141-86daaa72295d?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_004",
                "titulo": "Casa de Campo Pedra Moledo",
                "categoria": "Residencial",
                "estilo": "Rústico Moderno",
                "descricao_curta": "Arquitetura integrada à natureza com revestimento em pedra Moledo.",
                "descricao_longa": "Harmonia ambiental. O uso de pedra Moledo na base da residência e vigas de eucalipto estruturais confere um ar orgânico ao projeto. O render utilizou Forest Pack para distribuir vegetação nativa densa de forma fotorrealista.",
                "materiais": ["Pedra Moledo", "Vigas Eucalipto", "Telha Shingle"],
                "software": "3ds Max + Corona Renderer",
                "tempo_render": "8h 10m",
                "imgs": [
                    "https://images.unsplash.com/photo-1500313830540-7b6650a74fd0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_005",
                "titulo": "Rooftop Urbano Blue Hour",
                "categoria": "Comercial",
                "estilo": "Lounge",
                "descricao_curta": "Terraço social com mobiliário externo em corda náutica.",
                "descricao_longa": "Renderização noturna avançada. O foco está no balanço de brancos entre as luzes quentes artificiais do terraço e o fundo azulado do skyline urbano no crepúsculo. Mobiliário em corda náutica com texturas de alta definição.",
                "materiais": ["Corda Náutica", "Deck Sintético", "Vidro Temperado"],
                "software": "SketchUp + Enscape",
                "tempo_render": "1h 35m",
                "imgs": [
                    "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_006",
                "titulo": "Guarita Aço Corten",
                "categoria": "Comercial",
                "estilo": "Imponente",
                "descricao_curta": "Fachada de acesso em chapas metálicas enferrujadas.",
                "descricao_longa": "Design de impacto para condomínio. O revestimento em Aço Corten foi mapeado individualmente para evitar repetições, criando uma pátina natural e realista. Iluminação embutida valoriza os volumes geométricos da portaria.",
                "materiais": ["Aço Corten", "Vidro Blindado", "Pedra Portuguesa"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "4h 05m",
                "imgs": [
                    "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_007",
                "titulo": "Residência IES Profile",
                "categoria": "Residencial",
                "estilo": "Luminotécnico",
                "descricao_curta": "Estudo de fachos de luz reais em fachada noturna.",
                "descricao_longa": "Fidelidade de iluminação. O render utiliza arquivos IES reais dos fabricantes de lâmpadas para garantir que o desenho da luz na fachada seja exatamente igual ao que o cliente terá na obra física após a instalação.",
                "materiais": ["Tinta Branca", "MDF Naval", "Iluminação IES"],
                "software": "3ds Max + V-Ray",
                "tempo_render": "6h 35m",
                "imgs": [
                    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_008",
                "titulo": "Loft Industrial Retrofit",
                "categoria": "Residencial",
                "estilo": "Brooklyn Style",
                "descricao_curta": "Fachada em tijolo aparente e janelas em ferro.",
                "descricao_longa": "Render de inspiração industrial. O desafio foi a configuração do displacement no tijolo inglês aparente para garantir profundidade realista nos rejuntes, em conjunto com as sombras marcadas das janelas de ferro quadradas.",
                "materiais": ["Tijolo Inglês", "Metalon Grafite", "Vidro Canelado"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "4h 55m",
                "imgs": [
                    "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1565538810643-b5bdb714032a?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_009",
                "titulo": "Varanda Integrada Reiki",
                "categoria": "Apartamento",
                "estilo": "Moderno",
                "descricao_curta": "Fechamento em vidro e painel ripado em MDF Naval.",
                "descricao_longa": "Otimização de área externa em apartamento. O render mostra a transição suave entre a sala e a sacada, protegida pelo sistema Reiki. A marcenaria técnica em MDF Naval oculta as condensadoras de ar-condicionado de forma elegante.",
                "materiais": ["MDF Naval", "Porcelanato Amadeirado", "Vidro Reiki"],
                "software": "3ds Max + Corona",
                "tempo_render": "4h 30m",
                "imgs": [
                    "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618219944342-824e40a13285?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_010",
                "titulo": "Jardim de Inverno Zen",
                "categoria": "Residencial",
                "estilo": "Asiático",
                "descricao_curta": "Pátio interno com espelho d'água e jardim vertical.",
                "descricao_longa": "O pulmão verde da residência. Um espaço dedicado ao relaxamento, com modelagem botânica densa e fotorrealista. O render destaca o reflexo das espécies da Mata Atlântica no espelho d'água escura sob a pérgola de Cumaru.",
                "materiais": ["Madeira Cumaru", "Pedra Vulcânica", "Jardim Vertical"],
                "software": "SketchUp + V-Ray",
                "tempo_render": "5h 50m",
                "imgs": [
                    "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1500313830540-7b6650a74fd0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80"
                ]
            }
        ]

# ==============================================================================
# CLASS: APP_INTERFACE
# Responsável pelo motor visual, injeção de CSS e estabilidade de layout.
# ==============================================================================
class AppInterface:
    """
    Define o framework visual do Palladium Studio.
    Garante que o design seja profissional em qualquer dispositivo.
    """

    @staticmethod
    def initialize_theme():
        """
        Injeta o código CSS customizado para forçar o Dark Mode Premium.
        Remove elementos indesejados da interface padrão do Streamlit.
        """
        st.markdown("""
            <style>
            /* Tipografia Corporativa */
            @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

            /* Framework de Cores Palladium */
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

            /* Configuração Global */
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background-color: var(--bg-color) !important;
                color: var(--text-main) !important;
            }

            /* Estabilidade de Header e Sidebar */
            header {background-color: transparent !important;}
            #MainMenu, footer {visibility: hidden;}

            /* Títulos e Tipografia */
            h1, h2, h3, h4 {
                font-family: 'Cinzel', serif !important;
                font-weight: 600 !important;
                color: #ffffff !important;
                letter-spacing: 1px;
            }

            /* HERO SECTION */
            .hero-title {
                text-align: center;
                font-size: 4.5rem;
                margin-top: 20px;
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

            /* GRID SYSTEM */
            .project-card {
                background: var(--card-bg);
                border: 1px solid var(--border);
                border-radius: 6px;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                margin-bottom: 30px;
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

            /* SIDEBAR CUSTOMIZATION */
            [data-testid="stSidebar"] { 
                background-color: #050505 !important; 
                border-right: 1px solid var(--border); 
            }
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

            .sidebar-footer {
                padding: 20px;
                text-align: center;
                border-top: 1px solid #1a1a1a;
                margin-top: 20px;
            }

            /* CALL TO ACTION BUTTONS */
            .btn-gold {
                display: block; background: var(--accent); color: #000 !important;
                text-align: center; padding: 15px; font-weight: 700;
                letter-spacing: 2px; text-decoration: none; text-transform: uppercase;
                transition: 0.4s; border-radius: 3px; border: 1px solid var(--accent);
                font-size: 0.85rem;
            }
            .btn-gold:hover { background: #fff; border-color: #fff; box-shadow: 0 0 20px rgba(212, 175, 55, 0.3); }
            
            /* PRICING TABLES */
            .pricing-card {
                background: #0d0d0d; border: 1px solid #333; padding: 40px 30px;
                text-align: center; border-radius: 8px; transition: 0.3s; height: 100%;
                display: flex; flex-direction: column;
            }
            .pricing-card:hover { border-color: var(--accent); background: #141414; transform: translateY(-5px); }

            /* MOBILE OPTIMIZATION */
            @media (max-width: 768px) {
                .hero-title { font-size: 2.2rem !important; margin-top: 40px !important; }
                .hero-subtitle { font-size: 0.7rem !important; letter-spacing: 4px !important; }
                [data-testid="stHorizontalBlock"] { flex-direction: column !important; }
                .pricing-card { margin-bottom: 25px; }
            }

            /* Hiding Streamlit full screen buttons */
            button[title="View fullscreen"] { display: none; }
            </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# CLASS: PAGE_RENDERER
# Contém a lógica de renderização de cada módulo do sistema.
# ==============================================================================
class PageRenderer:
    """
    Roteador de visualização. Cada método representa uma página independente.
    """

    @staticmethod
    def render_home():
        """Renderiza a Landing Page do Estúdio."""
        st.markdown("<h1 class='hero-title'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
        st.markdown("<p class='hero-subtitle'>ARCHVIZ PARA ALTA MARCENARIA</p>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1500&q=80", use_container_width=True)
        
        st.markdown("<br><h2 style='text-align:center; color:#d4af37 !important;'>O Seu Projeto, Antes de Existir.</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p style='text-align:center; color:#aaa; max-width: 850px; margin: 0 auto; line-height:1.8;'>
            Especialistas em visualização 3D de alto padrão. Compreendemos a linguagem técnica da marcenaria e dos escritórios de arquitetura, 
            respeitando modulações reais e catálogos físicos (Arauco, Guararapes, Duratex) para garantir aprovações rápidas e seguras.
            </p>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        _, col_btn, _ = st.columns([1, 1, 1])
        with col_btn:
            if st.button("VISITAR PORTFÓLIO COMPLETO", use_container_width=True):
                st.session_state['page'] = 'Portfólio'
                st.rerun()

    @staticmethod
    def render_portfolio():
        """Renderiza a Galeria de Projetos Interativos."""
        interiores = DatabaseManager.get_interiores()
        exteriores = DatabaseManager.get_exteriores()
        
        st.markdown("<h1>Catálogo de Visualização</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#666; margin-bottom:40px;'>Filtre e selecione projetos para visualizar detalhamentos e perspectivas extras.</p>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='border-left: 4px solid #d4af37; padding-left: 15px;'>DESIGN DE INTERIORES (15 PROJETOS)</h3><br>", unsafe_allow_html=True)
        cols_int = st.columns(3)
        for i, proj in enumerate(interiores):
            with cols_int[i % 3]:
                st.markdown(f"""
                    <div class="project-card">
                        <div class="img-container"><img src="{proj['imgs'][0]}"></div>
                        <div class="card-content">
                            <div class="project-title">{proj['titulo']}</div>
                            <div style="font-size: 0.8rem; color: #d4af37; margin-bottom: 10px; text-transform: uppercase;">
                                {proj['categoria']} | {proj['estilo']}
                            </div>
                            <div class="project-desc">{proj['descricao_curta']}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"RELATÓRIO TÉCNICO", key=f"btn_{proj['id']}"):
                    st.session_state['projeto_selecionado'] = proj
                    st.session_state['page'] = 'Detalhes'
                    st.rerun()
        
        st.markdown("<br><hr style='border-color:#333;'><br>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='border-left: 4px solid #d4af37; padding-left: 15px;'>ARQUITETURA EXTERNA (10 PROJETOS)</h3><br>", unsafe_allow_html=True)
        cols_ext = st.columns(3)
        for i, proj in enumerate(exteriores):
            with cols_ext[i % 3]:
                st.markdown(f"""
                    <div class="project-card">
                        <div class="img-container"><img src="{proj['imgs'][0]}"></div>
                        <div class="card-content">
                            <div class="project-title">{proj['titulo']}</div>
                            <div style="font-size: 0.8rem; color: #d4af37; margin-bottom: 10px; text-transform: uppercase;">
                                {proj['categoria']} | {proj['estilo']}
                            </div>
                            <div class="project-desc">{proj['descricao_curta']}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"RELATÓRIO TÉCNICO", key=f"btn_{proj['id']}"):
                    st.session_state['projeto_selecionado'] = proj
                    st.session_state['page'] = 'Detalhes'
                    st.rerun()

    @staticmethod
    def render_details():
        """Renderiza a visualização profunda de um projeto (Multi-ângulo)."""
        proj = st.session_state.get('projeto_selecionado')
        if not proj:
            st.session_state['page'] = 'Portfólio'
            st.rerun()
            return

        if st.button("← VOLTAR PARA O CATÁLOGO"):
            st.session_state.update({'projeto_selecionado': None, 'page': 'Portfólio'})
            st.rerun()

        st.markdown(f"<h1>Galeria Técnica: {proj['titulo']}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#d4af37; letter-spacing:3px; text-transform:uppercase;'>ESTILO: {proj['estilo']} | ENGINE: {proj['software']}</p><br>", unsafe_allow_html=True)

        # Galeria de 4 Fotos (Vertical)
        for i, img_url in enumerate(proj['imgs']):
            st.image(img_url, caption=f"Perspectiva de Câmera 0{i+1} - Renderização High-End 4K", use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)

        st.write("---")
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown("<h3>Memorial Descritivo do Render</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#aaa; line-height:1.8; font-size:1.1rem;'>{proj['descricao_longa']}</p>", unsafe_allow_html=True)
        with c2:
            st.markdown("""
                <div style='background:#111; border:1px solid #222; padding:30px; border-radius:6px;'>
                    <h4 style='color:#d4af37 !important; border-bottom:1px solid #333; padding-bottom:15px; margin-top:0;'>Ficha Técnica</h4>
            """, unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:0;'>Tempo de Renderização:</p><p style='color:#ccc; font-weight:600;'>{proj['tempo_render']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:0;'>Workflow:</p><p style='color:#ccc; font-weight:600;'>{proj['software']}</p>", unsafe_allow_html=True)
            st.markdown("<p style='color:#888; font-size:0.9rem; margin-bottom:10px;'>Materiais e PBR:</p>", unsafe_allow_html=True)
            for mat in proj['materiais']:
                st.markdown(f"<span style='display:inline-block; background:#1a1a1a; border:1px solid #333; color:#aaa; font-size:0.8rem; padding:5px 10px; border-radius:4px; margin:3px;'>{mat}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    @staticmethod
    def render_imersao():
        """Renderiza o módulo de Imersão: Vídeo 15s + Tour 360 Real."""
        st.markdown("<h1>Experiências de Imersão</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#888; font-size:1.1rem; margin-bottom:50px;'>Apresente seus projetos com tecnologias que vendem. Tours interativos e vídeos cinemáticos para marcenaria.</p>", unsafe_allow_html=True)
        
        # MÓDULO 1: VÍDEO ANIMADO
        st.markdown("<h3 style='color:#d4af37 !important; margin-bottom:20px;'>1. Cinematic Tour (Vídeo Animado)</h3>", unsafe_allow_html=True)
        col_vid_txt, col_vid_main = st.columns([1, 1.5])
        with col_vid_txt:
            st.markdown("""
                <p style='color:#aaa; line-height:1.8;'>Vídeos curtos de 15 a 30 segundos focados no detalhamento da marcenaria e iluminação. 
                Ideal para atrair atenção em redes sociais e facilitar a compreensão espacial do cliente final.</p>
                <ul style='color:#888; font-size:0.9rem;'>
                    <li>Resolução 1080p (Ideal para Reels/WhatsApp)</li>
                    <li>Renderização em tempo real</li>
                    <li>Edição de som ambiente profissional</li>
                </ul>
            """, unsafe_allow_html=True)
        with col_vid_main:
            # Exemplo de Animação ArchViz Real
            st.video("https://www.youtube.com/watch?v=11X_N2U23zY")
        
        st.markdown("<br><hr style='border-color:#333;'><br>", unsafe_allow_html=True)
        
        # MÓDULO 2: TOUR 360 INTERATIVO (Padrão ArchViz)
        st.markdown("<h3 style='color:#d4af37 !important; margin-bottom:20px;'>2. Tour 360º de Interior Real</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#aaa;'>Clique na imagem abaixo, arraste para explorar cada canto do projeto e use o scroll para dar zoom. O seu cliente recebe um link como este diretamente no WhatsApp.</p>", unsafe_allow_html=True)
        
        # Link do Kuula de um apartamento decorado real (Substituindo Street View por ArchViz)
        tour_url = "https://kuula.co/share/collection/7l1c9?logo=0&info=0&fs=1&vr=1&sd=1&initload=0&thumbs=1"
        components.iframe(tour_url, height=650, scrolling=False)
        
        st.markdown("<br><center><p style='color:#444; font-size:0.85rem;'>Desenvolvido com tecnologia de panorama esférico HDR.</p></center>", unsafe_allow_html=True)

    @staticmethod
    def render_planos():
        """Renderiza os pacotes comerciais do estúdio."""
        st.markdown("<h1 style='text-align:center;'>Nossos Pacotes</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#666; margin-bottom:50px;'>Soluções desenhadas para acelerar o fechamento de orçamentos de marcenarias de alto padrão.</p>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
                <div class='pricing-card'>
                    <h3 style='color:#d4af37; font-size:1.5rem;'>Essencial</h3>
                    <p style='color:#888; font-size:0.85rem; height:45px;'>Para ambientes unitários diários.</p>
                    <div style='text-align:left; color:#aaa; font-size:0.9rem; line-height:2.2; border-top:1px solid #222; padding-top:20px; margin-bottom:30px; flex-grow:1;'>
                        <span>✓</span> Otimização do 3D Base<br>
                        <span>✓</span> Texturas PBR de Catálogos<br>
                        <span>✓</span> Iluminação Natural Global<br>
                        <span>✓</span> <b>2 Imagens Estáticas 4K</b><br>
                        <span style='color:#444;'>✗ Sem revisões estruturais</span>
                    </div>
                    <a href='https://wa.me/5514998405046' class='btn-gold'>SOLICITAR AGORA</a>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
                <div class='pricing-card' style='border-color:#d4af37; transform: scale(1.03);'>
                    <div style='background:#d4af37; color:#000; font-weight:700; font-size:0.75rem; padding:5px; border-radius:20px; margin-bottom:15px; width:120px; margin-left:auto; margin-right:auto;'>MAIS BUSCADO</div>
                    <h3 style='color:#fff; font-size:1.5rem;'>Premium Marcenaria</h3>
                    <p style='color:#888; font-size:0.85rem; height:45px;'>Apresentação completa para casas planejadas.</p>
                    <div style='text-align:left; color:#aaa; font-size:0.9rem; line-height:2.2; border-top:1px solid #222; padding-top:20px; margin-bottom:30px; flex-grow:1;'>
                        <span>✓</span> Modelagem Fina de Ferragens<br>
                        <span>✓</span> Decoração e Cena VIP<br>
                        <span>✓</span> Iluminação Cenográfica IES<br>
                        <span>✓</span> <b>5 Imagens Estáticas 4K</b><br>
                        <span>✓</span> 1 Rodada de Ajustes Finos
                    </div>
                    <a href='https://wa.me/5514998405046' class='btn-gold'>FECHAR PACOTE</a>
                </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
                <div class='pricing-card'>
                    <h3 style='color:#d4af37; font-size:1.5rem;'>Imersão 360º</h3>
                    <p style='color:#888; font-size:0.85rem; height:45px;'>Experiência de tour interativo completa.</p>
                    <div style='text-align:left; color:#aaa; font-size:0.9rem; line-height:2.2; border-top:1px solid #222; padding-top:20px; margin-bottom:30px; flex-grow:1;'>
                        <span>✓</span> Modelagem Otimizada VR<br>
                        <span>✓</span> Render Esférico HDR<br>
                        <span>✓</span> Link Interativo Privado<br>
                        <span>✓</span> <b>1 Ambiente 360 / Tour Vídeo</b><br>
                        <span>✓</span> Hospedagem Ativa (6 meses)
                    </div>
                    <a href='https://wa.me/5514998405046' class='btn-gold'>CONHECER TOUR</a>
                </div>
            """, unsafe_allow_html=True)

    @staticmethod
    def render_contato():
        """Renderiza a página de contato e informações operacionais."""
        st.markdown("<h1>Prospecção & Atendimento</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#888; margin-bottom:50px;'>Pronto para elevar o nível da sua marcenaria? Entre em contato direto com nossa equipe técnica.</p>", unsafe_allow_html=True)
        
        c1, c2 = st.columns([1, 1])
        with c1:
            st.markdown("""
                <div style='background:#111; padding:40px; border-radius:6px; border:1px solid #222;'>
                    <h3 style='margin-top:0; color:#d4af37 !important;'>Central Palladium</h3>
                    <p style='color:#aaa; line-height:2.2;'>
                        📍 <b>Sede Física:</b> Ourinhos, SP<br>
                        🌍 <b>Atendimento:</b> Nível Nacional (Remoto)<br>
                        📧 <b>Comercial:</b> contato@palladiumstudio.com<br>
                        📱 <b>WhatsApp:</b> (14) 99840-5046
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            link_wpp = "https://wa.me/5514998405046"
            st.markdown(f'<a href="{link_wpp}" target="_blank" class="btn-gold">INICIAR CONVERSA NO WHATSAPP</a>', unsafe_allow_html=True)

        with c2:
            st.markdown("<h3 style='margin-top:0;'>Filtro de Dúvidas</h3>", unsafe_allow_html=True)
            with st.expander("Qual o formato de arquivo para envio?"):
                st.write("Aceitamos arquivos em .SKP (SketchUp), .MAX (3ds Max) ou plantas baixas em .DWG e .PDF para modelagem do zero.")
            with st.expander("Qual o prazo de entrega padrão?"):
                st.write("Para projetos de 1 ou 2 ambientes, a primeira prévia de baixa resolução é entregue em até 48 horas úteis.")
            with st.expander("Recebo o arquivo 3D configurado?"):
                st.write("Não. O Palladium Studio comercializa a mídia final renderizada. Os arquivos raiz configurados com nossos assets proprietários são de posse intelectual do estúdio.")

# ==============================================================================
# MAIN FUNCTION: CONTROLADOR DE EXECUÇÃO
# Responsável pelo ciclo de vida da aplicação.
# ==============================================================================
def main():
    """
    Função mestra que inicializa a interface e gerencia a navegação.
    """
    # 1. Inicializa visual
    AppInterface.initialize_theme()
    
    # 2. Configura Sidebar e Navegação (SEM ERROS DE SOBREPOSIÇÃO)
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; font-size: 2.2rem; margin-bottom:0;'>PALLADIUM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#555; font-size:0.7rem; letter-spacing:5px; margin-top:0;'>STUDIO ARCHVIZ</p>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Menu de Navegação via Botões
        if st.button("INÍCIO"): st.session_state.update({'projeto_selecionado': None, 'page': 'Início'})
        if st.button("CATÁLOGO 3D"): st.session_state.update({'projeto_selecionado': None, 'page': 'Portfólio'})
        if st.button("IMERSÃO & VÍDEO"): st.session_state.update({'projeto_selecionado': None, 'page': 'Imersão'})
        if st.button("PLANOS E PACOTES"): st.session_state.update({'projeto_selecionado': None, 'page': 'Planos'})
        if st.button("CONTATO & SUPORTE"): st.session_state.update({'projeto_selecionado': None, 'page': 'Contato'})
        
        # Espaçamento manual flexível em vez de absoluto
        st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
        
        st.markdown('<a href="https://wa.me/5514998405046" target="_blank" class="btn-gold">SOLICITAR ANÁLISE</a>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="sidebar-footer">
                <p style='color: #333; font-size: 0.65rem; letter-spacing: 1px; margin:0;'>
                    PALLADIUM STUDIO © 2026<br>
                    ARCHITECTURE VISUALIZATION ENGINE v3.0
                </p>
            </div>
        """, unsafe_allow_html=True)

    # 3. Router de Páginas
    page = st.session_state['page']
    
    # Renderizador centralizado em container seguro
    with st.container():
        st.markdown("<div style='padding: 1% 4% 5% 4%;'>", unsafe_allow_html=True)
        
        if page == 'Início':
            PageRenderer.render_home()
        elif page == 'Portfólio':
            PageRenderer.render_portfolio()
        elif page == 'Detalhes':
            PageRenderer.render_details()
        elif page == 'Imersão':
            PageRenderer.render_imersao()
        elif page == 'Planos':
            PageRenderer.render_planos()
        elif page == 'Contato':
            PageRenderer.render_contato()
            
        st.markdown("</div>", unsafe_allow_html=True)

# Ponto de entrada do script
if __name__ == "__main__":
    main()
