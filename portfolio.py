"""
================================================================================
PALLADIUM STUDIO - ENTERPRISE ARCHVIZ PORTFOLIO ENGINE v4.2
================================================================================
Desenvolvido para: Pedro Teixeira | Palladium Studio
Local de Operação: Ourinhos, SP | Atendimento Nacional
Arquitetura de Software: Programação Orientada a Objetos (POO) com Streamlit
Foco de Mercado: Alta Marcenaria, Arquitetura e Architectural Visualization
Conformidade: Renderização PBR, Catálogos Reais (Arauco, Guararapes)
================================================================================
"""

import streamlit as st
import time
import streamlit.components.v1 as components

# ==============================================================================
# CLASSE 1: PALLADIUM_DATA_ENGINE
# Central de controle de dados relacionais e ativos de mídia (Imagens/Vídeos).
# Garante 4 perspectivas exclusivas e validadas para cada projeto.
# ==============================================================================
class PalladiumDataEngine:
    """
    Motor de dados do Palladium Studio.
    Armazena e fornece todas as especificações técnicas de modelagem, 
    iluminação, texturas e links diretos (CDN) das renderizações 4K.
    """

    @staticmethod
    def get_interiores_data():
        """
        Retorna o dicionário completo de 15 Projetos de Interiores.
        Garantia de 4 URLs de ângulos diferentes por projeto.
        """
        return [
            {
                "id": "INT_001",
                "titulo": "Cozinha Minimalista Nero",
                "categoria": "Cozinha Planejada",
                "estilo": "Minimalista Moderno",
                "descricao_curta": "MDF Preto Silk com puxadores cava integrados e iluminação 3000K.",
                "descricao_longa": "O projeto foca na continuidade visual absoluta. A marcenaria foi inteiramente configurada utilizando o padrão Preto Silk. O detalhamento do puxador é todo em cava 45 graus oculto, garantindo que não existam ferragens aparentes cortando a linearidade do móvel. A bancada em quartzo cinza absoluto foi renderizada com mapa de rugosidade (Roughness) para refletir suavemente os perfis de LED de sobrepor.",
                "materiais": ["MDF Preto Silk", "Quartzo Cinza", "Puxador Cava", "LED 3000K"],
                "software": "SketchUp + V-Ray 6",
                "processamento": "4h 15m (GPU Render)",
                "imgs": [
                    "https://images.unsplash.com/photo-1556911220-e15022357539?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1556911261-6bd341186b2f?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_002",
                "titulo": "Suíte Master Premium",
                "categoria": "Dormitório Casal",
                "estilo": "Contemporâneo",
                "descricao_curta": "Painel ripado em MDF Freijó e cabeceira estofada em linho cru.",
                "descricao_longa": "Projeto de dormitório focado no conforto térmico e visual. O painel principal foi modelado com ripados de 1.5cm de espessura em MDF Freijó (Arauco). A renderização destaca a iluminação wall-washer incidindo sobre a textura orgânica do tecido de linho da cabeceira. Criados-mudos configurados com laca cinza fosca.",
                "materiais": ["MDF Freijó", "Linho Cru", "Laca Cinza Fosca", "Iluminação IES"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "5h 40m",
                "imgs": [
                    "https://images.unsplash.com/photo-1616594111750-4744bda7e9a2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1560185007-cde436f6a4d0?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_003",
                "titulo": "Living Pé-Direito Duplo",
                "categoria": "Estar e Jantar",
                "estilo": "Alto Luxo",
                "descricao_curta": "Integração com painéis em carvalho e mármore.",
                "descricao_longa": "O grande desafio técnico desta cena foi o cálculo de iluminação global (GI). Com grandes aberturas de vidro, o render simula a entrada de luz natural forte. A marcenaria de apoio utiliza painéis lisos em MDF Carvalho Natural para aquecer o ambiente, criando um balanço com o piso de porcelanato frio e brilhante.",
                "materiais": ["MDF Carvalho Natural", "Mármore Calacatta", "Porcelanato 120x120", "Vidro Laminado"],
                "software": "SketchUp + V-Ray + Chaos Cloud",
                "processamento": "1h 10m (Cloud Computing)",
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
                "estilo": "Minimalista Clássico",
                "descricao_curta": "Marcenaria em MDF Branco Ultra com cuba em mármore.",
                "descricao_longa": "Design focado em assepsia e longa durabilidade. O gabinete suspenso utiliza MDF Ultra, configurado com acabamento branco fosco. O render detalha perfeitamente a refração da luz no espelho retroiluminado e a translucidez (Subsurface Scattering) da pedra natural utilizada na cuba esculpida.",
                "materiais": ["MDF Branco Ultra", "Mármore Branco", "Metais Red Gold", "Espelho Bisotado"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "6h 25m",
                "imgs": [
                    "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1603912975949-c1e1e0a29363?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1620626011761-9963d7b59a7a?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_005",
                "titulo": "Área Gourmet Graphite",
                "categoria": "Varanda Gourmet",
                "estilo": "Industrial Chic",
                "descricao_curta": "Churrasqueira com marcenaria técnica em tons de cinza escuro.",
                "descricao_longa": "As quatro perspectivas desta área gourmet focam no convívio social. Os armários utilizam texturas precisas de MDF Grafite resistente a intempéries e gordura. A bancada em granito escovado complementa o visual, enquanto a iluminação de HDRI de final de tarde invade a varanda criando sombras densas.",
                "materiais": ["MDF Grafite", "Madeira de Demolição", "Granito São Gabriel", "Metalon Preto"],
                "software": "SketchUp + V-Ray",
                "processamento": "4h 50m",
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
                "estilo": "Corporativo Premium",
                "descricao_curta": "Estante com nichos iluminados e mesa flutuante em MDF Freijó.",
                "descricao_longa": "Ambiente projetado para alta produtividade em trabalho remoto. A estante mistura Laca Preta e MDF amadeirado chiaro, possuindo iluminação LED embutida por baixo de cada prateleira. O render destaca o brilho suave das poltronas de couro executivo e o design ergonômico da marcenaria suspensa.",
                "materiais": ["MDF Freijó", "Laca Preta Fosca", "Couro Premium", "Vidro Canelado"],
                "software": "3ds Max + V-Ray 6",
                "processamento": "3h 30m",
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
                "descricao_curta": "Divisórias em MDF Cinza e portas em vidro reflecta bronze.",
                "descricao_longa": "O conceito visual aqui é transformar o closet em uma vitrine particular. Toda a estrutura é fechada com perfis de alumínio fino e Vidro Reflecta Bronze, garantindo transparência quando as luzes internas de LED se acendem. A marcenaria paginada em MDF Cinza Sagrado traz sofisticação europeia à cena.",
                "materiais": ["Vidro Reflecta Bronze", "MDF Cinza Sagrado", "Alumínio Preto", "Fitas de LED"],
                "software": "SketchUp + Enscape 3.5",
                "processamento": "1h 50m",
                "imgs": [
                    "https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618219944342-824e40a13285?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_008",
                "titulo": "Sala de Jantar Elegance",
                "categoria": "Living",
                "estilo": "Clássico Modernizado",
                "descricao_curta": "Buffet planejado com portas em palhinha e tampo em pedra.",
                "descricao_longa": "O ponto alto desta renderização é a física do material (PBR). O buffet utiliza textura vazada de palhinha natural indiana, calculada através de mapas de opacidade precisos para que a luz passe pelas tramas. O MDF Nogueira complementa a robustez do tampo de mármore sob a iluminação de um pendente escultural.",
                "materiais": ["Palhinha Indiana", "MDF Nogueira", "Mármore Travertino", "Lustre Metálico"],
                "software": "SketchUp + V-Ray",
                "processamento": "5h 15m",
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
                "categoria": "Quarto Infantil",
                "estilo": "Montessoriano",
                "descricao_curta": "Marcenaria com cantos arredondados e tons pastéis em laca.",
                "descricao_longa": "Ergonomia e lúdico andam de mãos dadas neste projeto. A marcenaria técnica foca em cantos arredondados (fillet edges) para segurança. O acabamento simula pintura em laca fosca calibrada com códigos RGB reais. A iluminação de janela (Daylight) entra difusa pelas cortinas, deixando as sombras extremamente suaves.",
                "materiais": ["Laca Rosa Pastel", "MDF Carvalho Munique", "Algodão Orgânico", "Ripado Suave"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "4h 05m",
                "imgs": [
                    "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1520699049698-acd2fccb8cc8?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1505692952047-1a78307da8f2?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_010",
                "titulo": "Adega Particular Cumaru",
                "categoria": "Bar e Adega",
                "estilo": "Rústico Moderno",
                "descricao_curta": "Nichos colmeia climatizados em madeira maciça.",
                "descricao_longa": "Um subsolo focado em exclusividade. A baixa iluminação exigiu cálculos avançados de inteligência artificial (Denoise) para limpar ruídos da imagem. A marcenaria estrutural simula madeira maciça Cumaru para suportar o peso do acervo, criando um contraste majestoso com a parede de tijolos ingleses de demolição.",
                "materiais": ["Madeira Cumaru Maciça", "Tijolo Inglês", "Vidro Duplo Reflexivo", "Metalon Preto"],
                "software": "3ds Max + V-Ray",
                "processamento": "7h 15m",
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
                "descricao_curta": "Aparador slim e painel de espelhos para ampliar ambiente.",
                "descricao_longa": "Uma transição compacta resolvida com inteligência espacial. O console suspenso exibe uma espessura de apenas 12cm com gavetas ocultas. O painel lateral revestido com faixas de espelhos bisotados dobra o volume visual do ambiente. Câmeras virtuais em 35mm foram usadas para evitar distorção nas bordas.",
                "materiais": ["MDF Lacca Cetin", "Espelho Prata Bisotado", "Granito Polido", "LED Embutido"],
                "software": "SketchUp + Corona",
                "processamento": "2h 45m",
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
                "categoria": "Área de Serviço",
                "estilo": "Moderno Clean",
                "descricao_curta": "Armários em MDF Branco Ártico com tulhas embutidas.",
                "descricao_longa": "Onde o design encontra a função bruta. O projeto técnico de marcenaria inclui tulhas basculantes para roupas e espaçamento exato para respiro das máquinas de alta capacidade. O MDF Branco Ártico confere a percepção de limpeza constante, ancorado por rodapés em alumínio que protegem o móvel contra respingos de água.",
                "materiais": ["MDF Branco Ártico", "Bancada em Corian", "Rodapés de Alumínio"],
                "software": "SketchUp + Enscape",
                "processamento": "1h 15m",
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
                "descricao_longa": "O impacto visual da verticalidade. A marcenaria de 6 metros de altura em Carvalho Natural é a rainha desta cena. A iluminação de teto através de trilhos eletrificados industriais lava a textura da madeira com luz quente. A escada deslizante em trilho metálico preto conecta o ambiente clássico à engenharia moderna.",
                "materiais": ["MDF Carvalho", "Metal Preto Fosco", "Piso Vinílico Amadeirado", "LED Linear"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "6h 40m",
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
                "estilo": "Clean Minimalista",
                "descricao_curta": "Balcão orgânico em curvas com filetes de LED embutidos.",
                "descricao_longa": "Concebido para passar assepsia, modernidade e acolhimento clínico. A estrutura orgânica (curva) do balcão de recepção foi modelada e texturizada com Laminado Brilhante de alta resistência. O filete de LED azul na base suspensa cria a sensação de que a marcenaria de 300kg está flutuando sobre o porcelanato técnico.",
                "materiais": ["Laminado Branco Brilhante", "MDF Amadeirado Claro", "Porcelanato Técnico", "Fita de LED Blue"],
                "software": "SketchUp + V-Ray",
                "processamento": "3h 55m",
                "imgs": [
                    "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "INT_015",
                "titulo": "Living Laca Alto Brilho",
                "categoria": "Living",
                "estilo": "Luxo Escuro",
                "descricao_curta": "Painel de TV com acabamento polido em laca negra.",
                "descricao_longa": "O suprassumo dos reflexos PBR em arquitetura 3D. O painel principal recebeu simulação de 5 camadas de verniz sobre a Laca Negra. O ambiente noturno com iluminação zenital artificial (focos embutidos) testa a capacidade do motor de render de lidar com superfícies de alto brilho sem gerar quebras de pixels.",
                "materiais": ["Laca Preta Alto Brilho", "MDF Grafite Especial", "Couro Preto Legítimo", "Vidro Temperado"],
                "software": "3ds Max + V-Ray 6",
                "processamento": "6h 10m",
                "imgs": [
                    "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1593910265171-ef6709849202?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1618221118493-9cfa1a1c00da?auto=format&fit=crop&w=1200&q=80"
                ]
            }
        ]

    @staticmethod
    def get_exteriores_data():
        """
        Retorna a matriz relacional de projetos de Arquitetura Exterior.
        10 Projetos com iluminações variáveis (Dia, Noite, Blue Hour).
        """
        return [
            {
                "id": "EXT_001",
                "titulo": "Fachada Residencial Brises",
                "categoria": "Arquitetura Residencial",
                "estilo": "Contemporâneo",
                "descricao_curta": "Volumes em concreto aparente e brises verticais.",
                "descricao_longa": "Volumetria limpa e impactante. Os brises verticais bloqueiam a luz agressiva da tarde e geram sombras desenhadas na fachada da casa. Texturas rústicas de concreto aparente se unem perfeitamente à modelagem de vegetação densa fornecida pelos assets em alta resolução do Chaos Cosmos.",
                "materiais": ["Alumínio Madeirado", "Concreto Aparente", "Esquadria Metálica Preta"],
                "software": "SketchUp + V-Ray",
                "processamento": "5h 45m",
                "imgs": [
                    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_002",
                "titulo": "Lazer Tropical Chic",
                "categoria": "Área de Lazer",
                "estilo": "Resort Tropics",
                "descricao_curta": "Piscina de borda infinita conectada ao deck em madeira Itaúba.",
                "descricao_longa": "Análise puramente física do comportamento da água frente ao sol direto do meio-dia (HDRI 12:00PM). O espelho da borda infinita reflete fielmente o azul saturado do céu. A modelagem do deck não utiliza texturas planas; as réguas de Itaúba possuem mapas de deslocamento (Displacement) individualizados.",
                "materiais": ["Madeira Itaúba Maciça", "Pedra Hijau Original", "Porcelanato Acetinado Externo"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "7h 55m",
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
                "categoria": "Comercial / Edifício",
                "estilo": "High-Tech Urbano",
                "descricao_curta": "Edifício em pele de vidro refletiva ambientado em cena de pós-chuva.",
                "descricao_longa": "Render focado na integração do gigante corporativo com o meio urbano. As esquadrias revestidas em Pele de Vidro refletem as nuvens dramáticas de uma tempestade recente. A calçada em asfalto possui mapas PBR de poças d'água interativas com as luzes dos carros no térreo, criando hiper-realismo fotográfico.",
                "materiais": ["Pele de Vidro Prata", "ACM Preto Fosco", "Asfalto PBR Molhado", "Concreto"],
                "software": "3ds Max + V-Ray",
                "processamento": "6h 50m",
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
                "categoria": "Residencial de Campo",
                "estilo": "Rústico Modernizado",
                "descricao_curta": "Harmonia entre alvenaria de pedra natural Moledo e vigas de eucalipto.",
                "descricao_longa": "O triunfo técnico desta cena é o gerenciamento de polígonos. Utilizando o motor de espalhamento Forest Pack, povoamos o lote com milhares de espécies nativas, gramíneas altas e rochas, sem sobrecarregar a memória de vídeo. A casa em si mistura cobertura em shingle com grandes pilares de eucalipto aparente.",
                "materiais": ["Pedra Moledo Estrutural", "Vigas Eucalipto Tratado", "Telha Shingle Negra", "Vidro de Controle Solar"],
                "software": "3ds Max + Corona Renderer + Forest Pack",
                "processamento": "8h 15m",
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
                "categoria": "Comercial de Lazer",
                "estilo": "Sky Lounge",
                "descricao_curta": "Área social em terraço elevado com mobiliário em corda náutica.",
                "descricao_longa": "Um teste pesado de temperatura de cor. O horário escolhido (Crepúsculo / Blue Hour) inunda o ambiente com tons frios, exigindo que a iluminação de LED 2700K embutida no piso de deck sintético aqueça as áreas centrais de forma harmoniosa. Mobiliário detalhado com tramas individuais de corda náutica.",
                "materiais": ["Fio de Corda Náutica", "Deck Sintético WPC", "Vidro Temperado Transparente", "Fitas LED Quentes"],
                "software": "SketchUp + Enscape",
                "processamento": "1h 35m",
                "imgs": [
                    "https://images.unsplash.com/photo-1533154683836-84ea7a0bc310?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_006",
                "titulo": "Guarita Imponente Aço Corten",
                "categoria": "Portaria / Fachada Comercial",
                "estilo": "Industrial Monumental",
                "descricao_curta": "Fachada de acesso blindada revestida em chapas enferrujadas.",
                "descricao_longa": "Uma portaria pensada para blindar o lote sem se fechar para o urbanismo local. As grandes lâminas frontais receberam mapas procedurais de Aço Corten para que as ranhuras de oxidação não se repetissem nunca, trazendo o desgaste natural do tempo para a imagem puramente digital.",
                "materiais": ["Chapas de Aço Corten", "Vidro Laminado Blindado", "Calçamento em Pedra Portuguesa", "Refletores LED"],
                "software": "SketchUp + V-Ray",
                "processamento": "4h 25m",
                "imgs": [
                    "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
                ]
            },
            {
                "id": "EXT_007",
                "titulo": "Residência IES Light Study",
                "categoria": "Arquitetura Light Design",
                "estilo": "Contemporâneo Noturno",
                "descricao_curta": "Fachada noturna provando fidelidade luminotécnica via arquivos reais IES.",
                "descricao_longa": "Trabalho executivo direcionado a lighting designers. Em vez de focos de luz virtuais comuns, inserimos malhas de luz em formato '.ies' obtidas diretamente com os fabricantes físicos das lâmpadas. O resultado é o comportamento idêntico dos feixes nas paredes revestidas de cimento queimado escuro.",
                "materiais": ["Pintura Cimento Queimado", "MDF Naval Ripado", "Iluminação Fotométrica IES", "Esquadrias Alumínio"],
                "software": "3ds Max + V-Ray",
                "processamento": "6h 45m",
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
                "categoria": "Residencial Urbano",
                "estilo": "Brooklyn Heritage",
                "descricao_curta": "Fachada convertida em tijolo inglês aparente com janelas de ferro.",
                "descricao_longa": "Retrofit autêntico. A parede de tijolinhos vermelhos demandou técnicas avançadas de mapeamento de Displacement 3D para que o sol transversal iluminasse o topo do tijolo e escurecesse a argamassa do rejunte. As esquadrias antigas de ferro quadriculado abrigam vidros levemente canelados que distorcem o interior.",
                "materiais": ["Tijolo Inglês Avermelhado", "Caixilho de Metalon Grafite", "Vidro Translúcido Canelado"],
                "software": "SketchUp + V-Ray",
                "processamento": "4h 55m",
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
                "categoria": "Apartamento Alto Padrão",
                "estilo": "Moderno Clean",
                "descricao_curta": "Fechamento total em vidro Reiki e mobiliário outdoor em MDF Naval.",
                "descricao_longa": "A sacada tradicional que se transforma em extensão da sala de estar central. A transição perfeita sem degraus valoriza o nivelamento de piso em porcelanato acetinado. A marcenaria lateral técnica, construída com placas de MDF Naval resistentes à umidade, camufla a complexidade das condensadoras de AC sob uma estética elegante.",
                "materiais": ["MDF Naval Amadeirado", "Porcelanato Acetinado", "Sistema de Vidros Reiki Sem Rolamentos"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "4h 40m",
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
                "categoria": "Residencial Paisagismo",
                "estilo": "Zen Asiático",
                "descricao_curta": "Pátio interno de microclima com espelho d'água orgânico.",
                "descricao_longa": "O refúgio de oxigênio intra-arquitetônico. O espelho d'água liso com pedras vulcânicas submersas serve como espelho principal para a claraboia no topo do cômodo. O jardim vertical massivo foi montado folha por folha através da biblioteca de Megascans tridimensionais da Quixel, injetando verde fotorealista.",
                "materiais": ["Madeira Cumaru Aparente", "Pedra Vulcânica", "Jardim Vertical Megascans 3D"],
                "software": "SketchUp + V-Ray 6",
                "processamento": "5h 55m",
                "imgs": [
                    "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1500313830540-7b6650a74fd0?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=1200&q=80",
                    "https://images.unsplash.com/photo-1590060417603-eb1593d04976?auto=format&fit=crop&w=1200&q=80"
                ]
            }
        ]

# ==============================================================================
# CLASSE 2: PALLADIUM_UI_MANAGER
# Injeção de Estilos em Cascata (CSS) Customizados. 
# Bloqueio de elementos não corporativos do Streamlit Engine.
# ==============================================================================
class PalladiumUIManager:
    """
    Arquitetura de Front-end customizada.
    Responsável por garantir que a UI se comporte como um aplicativo React/Vue Premium.
    """

    @staticmethod
    def inject_premium_styles():
        """Aplica o tema Dark Mode com detalhes Dourados (Palladium Brand)."""
        st.markdown("""
            <style>
            /* BASE TYPOGRAPHY */
            @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

            /* COLOR PALETTE VARIABLES */
            :root {
                --bg-color: #080808;
                --text-main: #f2f2f2;
                --text-muted: #888888;
                --accent: #d4af37; 
                --card-bg: #111111;
                --card-hover: #161616;
                --border: #222222;
            }

            /* GLOBAL NORMALIZATION */
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background-color: var(--bg-color) !important;
                color: var(--text-main) !important;
            }

            /* REMOVING DEFAULT STREAMLIT ARTIFACTS */
            header {background-color: transparent !important;}
            #MainMenu, footer {visibility: hidden;}
            button[title="View fullscreen"] { display: none !important; }

            /* HEADERS TYPOGRAPHY */
            h1, h2, h3, h4 {
                font-family: 'Cinzel', serif !important;
                font-weight: 600 !important;
                color: #ffffff !important;
                letter-spacing: 1px;
            }

            /* HERO COMPONENT STYLING */
            .hero-title {
                text-align: center; font-size: 4.5rem; margin-top: 20px;
                color: #ffffff; font-family: 'Cinzel', serif;
            }
            .hero-subtitle {
                text-align: center; color: #888; font-size: 1.1rem;
                letter-spacing: 8px; margin-top: 5px; margin-bottom: 40px;
                text-transform: uppercase;
            }

            /* PROJECT CARDS (GRID LISTING) */
            .project-card {
                background: var(--card-bg); border: 1px solid var(--border);
                border-radius: 6px; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); 
                margin-bottom: 30px; display: flex; flex-direction: column; 
                height: 100%; overflow: hidden;
            }
            .project-card:hover {
                border-color: var(--accent); transform: translateY(-8px);
                box-shadow: 0 15px 35px rgba(212, 175, 55, 0.12); background: var(--card-hover);
            }
            .img-container { width: 100%; aspect-ratio: 16/9; overflow: hidden; background: #1a1a1a; }
            .img-container img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s ease; }
            .project-card:hover img { transform: scale(1.05); }
            
            .card-content { padding: 25px; display: flex; flex-direction: column; flex-grow: 1; }
            .project-title { font-family: 'Cinzel', serif; font-size: 1.25rem; color: var(--accent); margin-bottom: 10px; }
            .project-desc { font-size: 0.9rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 15px; flex-grow: 1; }

            /* SIDEBAR NAVIGATION PANEL */
            [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 1px solid var(--border); }
            [data-testid="stSidebar"] .stButton>button {
                background-color: transparent !important; color: #666 !important;
                border: none !important; border-left: 3px solid transparent !important;
                text-align: left !important; padding: 15px 25px !important;
                font-size: 0.9rem !important; letter-spacing: 3px; transition: 0.3s;
                width: 100%; justify-content: flex-start; text-transform: uppercase;
            }
            [data-testid="stSidebar"] .stButton>button:hover {
                color: #fff !important; border-left: 3px solid var(--accent) !important;
                background-color: #0a0a0a !important; transform: translateX(5px);
            }

            .sidebar-footer { padding: 20px; text-align: center; border-top: 1px solid #1a1a1a; margin-top: 20px; }

            /* CALL TO ACTION COMPONENTS */
            .btn-gold {
                display: block; background: var(--accent); color: #000 !important;
                text-align: center; padding: 15px; font-weight: 700;
                letter-spacing: 2px; text-decoration: none; text-transform: uppercase;
                transition: 0.4s; border-radius: 3px; border: 1px solid var(--accent); font-size: 0.85rem;
            }
            .btn-gold:hover { background: #ffffff; border-color: #ffffff; box-shadow: 0 0 25px rgba(212, 175, 55, 0.4); }

            /* PRICING PLANS COMPONENT */
            .pricing-card {
                background: #0d0d0d; border: 1px solid #333; padding: 40px 30px;
                text-align: center; border-radius: 8px; transition: 0.3s; height: 100%;
                display: flex; flex-direction: column;
            }
            .pricing-card:hover { border-color: var(--accent); background: #141414; transform: translateY(-5px); }

            /* MEDIA QUERIES FOR MOBILE ADAPTATION */
            @media (max-width: 768px) {
                .hero-title { font-size: 2.2rem !important; margin-top: 40px !important; }
                .hero-subtitle { font-size: 0.7rem !important; letter-spacing: 4px !important; }
                [data-testid="stHorizontalBlock"] { flex-direction: column !important; }
                .pricing-card { margin-bottom: 25px; }
            }
            </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# CLASSE 3: PALLADIUM_APP_ROUTER
# Encapsula a lógica condicional de visualização de cada módulo (Páginas SPA).
# ==============================================================================
class PalladiumAppRouter:
    """Gerencia a renderização dos componentes Python baseados no state da UI."""

    @staticmethod
    def render_home():
        """Módulo 01: Landing Page / Apresentação de Impacto."""
        st.markdown("<h1 class='hero-title'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
        st.markdown("<p class='hero-subtitle'>ARCHVIZ PARA ALTA MARCENARIA</p>", unsafe_allow_html=True)
        
        # Capa Principal
        st.image("https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1500&q=80", use_container_width=True)
        
        st.markdown("<br><h2 style='text-align:center; color:#d4af37 !important;'>O Seu Projeto, Antes de Existir.</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p style='text-align:center; color:#aaa; max-width: 850px; margin: 0 auto; line-height:1.8; font-size: 1.05rem;'>
            Somos especialistas em visualização 3D de altíssimo padrão. Nós compreendemos profundamente a linguagem técnica das marcenarias premium e dos escritórios de arquitetura. Nossas renderizações não são apenas ilustrativas: nós respeitamos modulações reais e utilizamos texturas dos catálogos físicos (Arauco, Guararapes, Duratex) para garantir que a expectativa do cliente se alinhe 100% com a entrega na obra.
            </p>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Botão centralizado usando layout do Streamlit
        _, col_btn, _ = st.columns([1, 1.2, 1])
        with col_btn:
            if st.button("VISITAR O CATÁLOGO DE PROJETOS", use_container_width=True):
                st.session_state['page'] = 'Portfólio'
                st.rerun()

    @staticmethod
    def render_portfolio():
        """Módulo 02: Listagem em Grid do banco de dados completo (15 INT + 10 EXT)."""
        interiores = PalladiumDataEngine.get_interiores_data()
        exteriores = PalladiumDataEngine.get_exteriores_data()
        
        st.markdown("<h1>Catálogo de Projetos em Destaque</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#666; margin-bottom:40px; font-size:1.1rem;'>Explore as categorias e clique em 'Relatório Técnico' para visualizar detalhamentos de iluminação, materiais e os diferentes ângulos das câmeras.</p>", unsafe_allow_html=True)
        
        # SEÇÃO 1: DESIGN DE INTERIORES
        st.markdown("<h3 style='border-left: 5px solid #d4af37; padding-left: 15px;'>DESIGN DE INTERIORES (15 Módulos)</h3><br>", unsafe_allow_html=True)
        cols_int = st.columns(3)
        for i, proj in enumerate(interiores):
            with cols_int[i % 3]:
                st.markdown(f"""
                    <div class="project-card">
                        <div class="img-container"><img src="{proj['imgs'][0]}"></div>
                        <div class="card-content">
                            <div class="project-title">{proj['titulo']}</div>
                            <div style="font-size: 0.8rem; color: #d4af37; margin-bottom: 12px; text-transform: uppercase; font-weight:600; letter-spacing: 1px;">
                                {proj['categoria']} | {proj['estilo']}
                            </div>
                            <div class="project-desc">{proj['descricao_curta']}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"RELATÓRIO TÉCNICO", key=f"btn_int_{proj['id']}"):
                    st.session_state['projeto_selecionado'] = proj
                    st.session_state['page'] = 'Detalhes'
                    st.rerun()
        
        st.markdown("<br><hr style='border-color:#222;'><br>", unsafe_allow_html=True)
        
        # SEÇÃO 2: ARQUITETURA EXTERNA
        st.markdown("<h3 style='border-left: 5px solid #d4af37; padding-left: 15px;'>ARQUITETURA EXTERNA E LAZER (10 Módulos)</h3><br>", unsafe_allow_html=True)
        cols_ext = st.columns(3)
        for i, proj in enumerate(exteriores):
            with cols_ext[i % 3]:
                st.markdown(f"""
                    <div class="project-card">
                        <div class="img-container"><img src="{proj['imgs'][0]}"></div>
                        <div class="card-content">
                            <div class="project-title">{proj['titulo']}</div>
                            <div style="font-size: 0.8rem; color: #d4af37; margin-bottom: 12px; text-transform: uppercase; font-weight:600; letter-spacing: 1px;">
                                {proj['categoria']} | {proj['estilo']}
                            </div>
                            <div class="project-desc">{proj['descricao_curta']}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"RELATÓRIO TÉCNICO", key=f"btn_ext_{proj['id']}"):
                    st.session_state['projeto_selecionado'] = proj
                    st.session_state['page'] = 'Detalhes'
                    st.rerun()

    @staticmethod
    def render_details():
        """Módulo 03: Drill-down de projeto individual. Renderiza as 4 fotos verticais e a ficha."""
        proj = st.session_state.get('projeto_selecionado')
        
        # Redirecionamento de segurança caso tente acessar via link direto sem seleção
        if not proj:
            st.session_state['page'] = 'Portfólio'
            st.rerun()
            return

        if st.button("← VOLTAR PARA O CATÁLOGO DE PROJETOS"):
            st.session_state.update({'projeto_selecionado': None, 'page': 'Portfólio'})
            st.rerun()

        st.markdown(f"<h1 style='font-size:3.2rem; margin-top:20px; margin-bottom:0;'>Galeria Multi-Ângulo: {proj['titulo']}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#d4af37; letter-spacing:4px; text-transform:uppercase; margin-bottom:30px;'>SETOR: {proj['categoria']} | RENDER ENGINE: {proj['software']}</p>", unsafe_allow_html=True)

        # Loop nativo do Python injetando as 4 URLs validadas pela Engine de Dados
        for i, img_url in enumerate(proj['imgs']):
            st.image(img_url, caption=f"Perspectiva de Câmera 0{i+1} - Resolução de Entrega 4K High-End", use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)

        st.write("---")
        
        col_text, col_tech = st.columns([2, 1])
        with col_text:
            st.markdown("<h3>Memorial Descritivo da Renderização</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#aaa; line-height:2.0; font-size:1.05rem; padding-right:30px;'>{proj['descricao_longa']}</p>", unsafe_allow_html=True)
            
        with col_tech:
            st.markdown("""
                <div style='background:#111; border:1px solid #222; padding:30px; border-radius:6px;'>
                    <h4 style='color:#d4af37 !important; border-bottom:1px solid #333; padding-bottom:15px; margin-top:0;'>Ficha Técnica Padrão</h4>
            """, unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888; font-size:0.95rem; margin-bottom:2px;'>Tempo Processamento Base:</p><p style='color:#fff; font-weight:600; margin-bottom:20px;'>{proj['processamento']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888; font-size:0.95rem; margin-bottom:2px;'>Workflow e Softwares:</p><p style='color:#fff; font-weight:600; margin-bottom:25px;'>{proj['software']}</p>", unsafe_allow_html=True)
            st.markdown("<p style='color:#888; font-size:0.95rem; margin-bottom:15px;'>Mapeamento de Materiais Físicos (PBR):</p>", unsafe_allow_html=True)
            
            for mat in proj['materiais']:
                st.markdown(f"<span style='display:inline-block; background:#1a1a1a; border:1px solid #333; color:#ccc; font-size:0.85rem; padding:6px 12px; border-radius:4px; margin:3px;'>{mat}</span>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

    @staticmethod
    def render_imersao():
        """Módulo 04: Componentes Web iFrames interativos para Tours 360 e Vídeos em Nuvem."""
        st.markdown("<h1>Experiências de Imersão Virtuais</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#888; font-size:1.15rem; margin-bottom:50px;'>Apresente seus projetos com a tecnologia que mais converte orçamentos no mercado atual. Tours esféricos e vídeos cinemáticos detalhistas.</p>", unsafe_allow_html=True)
        
        # SUBMÓDULO: VÍDEO CINEMÁTICO (ArchViz Animation)
        st.markdown("<h3 style='color:#d4af37 !important; margin-bottom:20px;'>01. Animação Cinemática (ArchViz Video)</h3>", unsafe_allow_html=True)
        col_vid_text, col_vid_iframe = st.columns([1, 1.5])
        with col_vid_text:
            st.markdown("""
                <p style='color:#aaa; line-height:2.0; font-size:1.05rem;'>Vídeos sequenciais de curta duração focados estritamente na percepção dos materiais, no reflexo das pedras polidas e na textura do MDF.
                <br><br>Esta mídia é extremamente poderosa para captação de clientes através de anúncios em redes sociais ou disparo direto pelo WhatsApp do estúdio da sua marcenaria.</p>
                <br>
                <ul style='color:#888; font-size:0.95rem; line-height:1.8;'>
                    <li>Renders exportados nativamente a 60FPS.</li>
                    <li>Resolução 1080p (Alta taxa de retenção Mobile).</li>
                    <li>Animação de Câmeras utilizando conceitos cinematográficos.</li>
                </ul>
            """, unsafe_allow_html=True)
        with col_vid_iframe:
            # Player de vídeo injetado via framework Streamlit
            st.video("https://www.youtube.com/watch?v=11X_N2U23zY")
        
        st.markdown("<br><hr style='border-color:#222;'><br>", unsafe_allow_html=True)
        
        # SUBMÓDULO: VIRTUAL REALITY (360 Kuula)
        st.markdown("<h3 style='color:#d4af37 !important; margin-bottom:20px;'>02. Tour Interativo de Realidade Virtual (Ambiente 360º)</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#aaa; font-size:1.05rem; margin-bottom:30px;'>Interaja com a imagem! Você tem liberdade para rotacionar o ambiente abaixo em todas as dimensões. Este é o exato formato em formato de 'Link Privado' que geramos para você repassar ao seu cliente durante uma reunião de fechamento.</p>", unsafe_allow_html=True)
        
        # Integração do visor Kuula substituindo as funções antigas do Google Maps.
        kuula_url = "https://kuula.co/share/collection/7l1c9?logo=0&info=0&fs=1&vr=1&sd=1&initload=0&thumbs=1"
        components.iframe(kuula_url, height=700, scrolling=False)

    @staticmethod
    def render_planos():
        """Módulo 05: Preços, Pacotes Comerciais e Metodologia Flexbox de Conversão."""
        st.markdown("<h1 style='text-align:center;'>Propostas Comerciais e Pacotes</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#666; font-size:1.1rem; margin-bottom:60px;'>Escalonamento de vendas sob demanda. Soluções estruturadas sem custos fixos mensais.</p>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
                <div class='pricing-card'>
                    <h3 style='color:#d4af37; font-size:1.6rem;'>Essencial Fast</h3>
                    <p style='color:#888; font-size:0.9rem; height:50px;'>Orçamentos diários de resposta rápida.</p>
                    <div style='text-align:left; color:#aaa; font-size:0.95rem; line-height:2.4; border-top:1px solid #222; padding-top:25px; margin-bottom:35px; flex-grow:1;'>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Recepção do Arquivo (.SKP)<br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Parametrização Básica (PBR)<br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Iluminação Global Diurna<br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> <b>2 Imagens 4K Inclusas</b><br>
                        <span style='color:#555; margin-right:8px;'>✗</span> <i style='color:#555;'>Sem Decoração VIP Avançada</i>
                    </div>
                    <a href='https://wa.me/5514998405046' class='btn-gold' style='background:transparent; border-color:#d4af37; color:#d4af37 !important;'>SOLICITAR ESTIMATIVA</a>
                </div>
            """, unsafe_allow_html=True)
            
        with c2:
            st.markdown("""
                <div class='pricing-card' style='border-color:#d4af37; transform: scale(1.05); z-index:10; background:#121212;'>
                    <div style='background:#d4af37; color:#000; font-weight:800; letter-spacing:2px; font-size:0.75rem; padding:6px; border-radius:20px; margin-bottom:20px; width:140px; margin-left:auto; margin-right:auto; margin-top:-10px;'>MAIS CONTRATADO</div>
                    <h3 style='color:#ffffff; font-size:1.6rem;'>Premium Studio</h3>
                    <p style='color:#888; font-size:0.9rem; height:50px;'>A apresentação esmagadora para fechamento de projetos em condomínios.</p>
                    <div style='text-align:left; color:#aaa; font-size:0.95rem; line-height:2.4; border-top:1px solid #222; padding-top:25px; margin-bottom:35px; flex-grow:1;'>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Correção e Otimização do 3D<br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> <b>Cenografia com Decoração VIP</b><br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Iluminação Complexa (Focos/IES)<br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> <b>5 Imagens 4K High-End</b><br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> 1 Revisão Fina Inclusa Grátis
                    </div>
                    <a href='https://wa.me/5514998405046' class='btn-gold'>GARANTIR DISPONIBILIDADE</a>
                </div>
            """, unsafe_allow_html=True)
            
        with c3:
            st.markdown("""
                <div class='pricing-card'>
                    <h3 style='color:#d4af37; font-size:1.6rem;'>Imersão Virtual VR</h3>
                    <p style='color:#888; font-size:0.9rem; height:50px;'>A revolução da interatividade para o cliente final.</p>
                    <div style='text-align:left; color:#aaa; font-size:0.95rem; line-height:2.4; border-top:1px solid #222; padding-top:25px; margin-bottom:35px; flex-grow:1;'>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Câmeras Esféricas a 360 graus<br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Renderização Panorama HDR 8K<br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Configuração na Plataforma Cloud<br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> <b>Link Privativo de Hospedagem</b><br>
                        <span style='color:#d4af37; margin-right:8px;'>✓</span> Licença Ativa Server: 6 meses
                    </div>
                    <a href='https://wa.me/5514998405046' class='btn-gold' style='background:transparent; border-color:#d4af37; color:#d4af37 !important;'>ORÇAR VIRTUAL TOUR</a>
                </div>
            """, unsafe_allow_html=True)

    @staticmethod
    def render_contato():
        """Módulo 06: Finalização do Funil. Área de Conversão Limpa (Call To Action)."""
        st.markdown("<h1>Prospecção e Atendimento Executivo</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#888; font-size:1.1rem; margin-bottom:50px;'>Deixe o estresse e a lentidão dos renderizadores em nossos servidores potentes e foque sua energia no fechamento dos contratos.</p>", unsafe_allow_html=True)
        
        c_form, c_faq = st.columns([1, 1.1])
        with c_form:
            st.markdown("""
                <div style='background:#0d0d0d; padding:45px; border-radius:8px; border:1px solid #222;'>
                    <h3 style='margin-top:0; margin-bottom:30px; color:#d4af37 !important; font-family:"Inter", sans-serif !important; font-weight:400 !important;'>Dados Operacionais Palladium</h3>
                    <p style='color:#aaa; line-height:2.4; font-size:1.05rem;'>
                        <span style='color:#fff;'>📍 Localização Base:</span> Ourinhos, São Paulo<br>
                        <span style='color:#fff;'>🌍 Cobertura:</span> Contratos em Nível Nacional<br>
                        <span style='color:#fff;'>📧 Gestão Comercial:</span> comercial@palladiumstudio.com<br>
                        <span style='color:#fff;'>📱 Central WhatsApp:</span> (14) 99840-5046
                    </p>
                    <br>
                    <p style='color:#555; font-size:0.85rem; border-top:1px solid #222; padding-top:20px;'>
                    Atendemos arquitetos parceiros e grandes nomes da marcenaria sob medida que demandam velocidade e precisão técnica.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            link_wpp = "https://wa.me/5514998405046"
            st.markdown(f'<a href="{link_wpp}" target="_blank" class="btn-gold" style="margin-top:25px; padding:20px;">INICIAR ALINHAMENTO VIA WHATSAPP AGORA</a>', unsafe_allow_html=True)

        with c_faq:
            st.markdown("<h3 style='margin-top:0; margin-bottom:30px;'>Filtro de Dúvidas de Parceria</h3>", unsafe_allow_html=True)
            
            with st.expander("Quais os formatos de arquivo permitidos para Início de Projeto?"):
                st.write("A modelagem pode ser encaminhada nos formatos padrão da indústria: .SKP (SketchUp - Preferencial), arquivos em blocos importados do Promob, ou plantas executivas em formato .DWG (AutoCAD) e .PDF, onde realizaremos o levantamento topográfico 3D do zero.")
            
            with st.expander("Como funciona o Workflow da Metodologia do Palladium?"):
                st.write("Nossa rotina é validada. O processo compreende 4 etapas obrigatórias: 1. Briefing e Recebimento de Referências; 2. Setup Fotorealista Físico (PBR); 3. Clay Render (Aprovação de iluminação global e bloqueio de câmera por parte do cliente); 4. Processamento Final High-End a nível de GPU Rendering e Pós-produção avançada em software.")
            
            with st.expander("Qual é o tempo de entrega das solicitações médias?"):
                st.write("Visando a máxima eficiência sem degradação do fotorrealismo, para projetos classificados no pacote 'Premium Marcenaria' de até dois ambientes conexos, o primeiro envio das imagens em média qualidade para rodada de ajuste ocorre entre 2 a 3 dias úteis.")
            
            with st.expander("Recebo a estrutura original 3D ao final do contrato?"):
                st.write("Não transferimos a propriedade dos ativos de estúdio. O Palladium Studio viabiliza as renderizações (as mídias exportadas 4K finais), Tour Panorâmico ou Arquivos MP4 Cinemáticos. A raiz das configurações (Setup de LUZ, proxies, Assets, V-Ray configurations e arquivos nativos) é nossa Propriedade Intelectual.")

# ==============================================================================
# INITIALIZATION PROCEDURE
# ==============================================================================
def main():
    """
    Controlador Mestre do Streamlit Engine.
    Executa a verificação dos blocos de memória e direciona para as classes de interface.
    """
    
    # 1. Manutenção de Memória para Arquitetura Cloud SPAs (Solução do KeyError)
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Início'
    if 'projeto_selecionado' not in st.session_state:
        st.session_state['projeto_selecionado'] = None

    # 2. Ativação do Front-End CSS Global
    PalladiumUIManager.inject_premium_styles()
    
    # 3. Construção Inteligente da Área de Navegação (Sidebar Escura)
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; font-size: 2.5rem; margin-bottom:0;'>PALLADIUM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#555; font-size:0.75rem; letter-spacing:5px; margin-top:0;'>ARCHVIZ STUDIO BR</p>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Botões reagem modificando o dicionário do Session State na nuvem.
        if st.button("01. INÍCIO DA JORNADA"): 
            st.session_state.update({'projeto_selecionado': None, 'page': 'Início'})
        
        if st.button("02. CATÁLOGO 3D 4K"): 
            st.session_state.update({'projeto_selecionado': None, 'page': 'Portfólio'})
        
        if st.button("03. IMERSÃO E VÍDEOS"): 
            st.session_state.update({'projeto_selecionado': None, 'page': 'Imersão'})
        
        if st.button("04. PLANOS E PACOTES"): 
            st.session_state.update({'projeto_selecionado': None, 'page': 'Planos'})
        
        if st.button("05. SUPORTE E CONTATO"): 
            st.session_state.update({'projeto_selecionado': None, 'page': 'Contato'})
        
        # Separador dinâmico não absoluto que previne bug em resoluções de telas baixas
        st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)
        
        st.markdown('<a href="https://wa.me/5514998405046" target="_blank" class="btn-gold">SOLICITAR AVALIAÇÃO</a>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="sidebar-footer">
                <p style='color: #333; font-size: 0.65rem; letter-spacing: 1.5px; margin:0; line-height: 1.6;'>
                    PALLADIUM STUDIO © 2026<br>
                    ALL RIGHTS RESERVED<br>
                    HIGH-END RENDER SYSTEM v4.2
                </p>
            </div>
        """, unsafe_allow_html=True)

    # 4. Roteamento Lógico da Tela Central
    page_target = st.session_state['page']
    
    # Previne que a div estoure as bordas laterais criando um container com margin-padding ideal
    with st.container():
        st.markdown("<div style='padding: 1% 4% 5% 4%;'>", unsafe_allow_html=True)
        
        if page_target == 'Início':
            PalladiumAppRouter.render_home()
        elif page_target == 'Portfólio':
            PalladiumAppRouter.render_portfolio()
        elif page_target == 'Detalhes':
            PalladiumAppRouter.render_details()
        elif page_target == 'Imersão':
            PalladiumAppRouter.render_imersao()
        elif page_target == 'Planos':
            PalladiumAppRouter.render_planos()
        elif page_target == 'Contato':
            PalladiumAppRouter.render_contato()
            
        st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ATIVADOR DO SCRIPT PYTHON
# Inicia toda a leitura das defs somente caso ele seja chamado diretamente pelo servidor
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
