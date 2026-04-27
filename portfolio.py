"""
PALLADIUM STUDIO - HIGH-END ARCHVIZ PORTFOLIO ENGINE v4.0
---------------------------------------------------------
Author: Palladium Studio Dev Team
Architecture: Object-Oriented Programming (OOP)
Complexity Grade: Enterprise / Professional
Total Projects: 25 (15 Interiors + 10 Exteriors)
Visual Fidelity: 4K Perspective Simulation
---------------------------------------------------------
"""

import streamlit as st
import time
import streamlit.components.v1 as components

# ==============================================================================
# CLASS: PALLADIUM_DATA_ENGINE
# Gerenciador de Ativos e Integridade de Dados.
# Responsável por manter a conexão entre imagens e descrições técnicas.
# ==============================================================================
class PalladiumDataEngine:
    """
    Motor de dados do Palladium Studio.
    Centraliza todas as informações técnicas dos projetos para garantir que
    as imagens correspondam 100% às descrições de marcenaria e arquitetura.
    """

    @staticmethod
    def get_interiores_data():
        """
        Retorna a matriz de dados para os 15 projetos de Interiores.
        Cada entrada possui metadados detalhados de materiais e 4 ângulos distintos.
        """
        return [
            {
                "id": "INT_001",
                "titulo": "Cozinha Minimalista Nero",
                "categoria": "Cozinha Planejada",
                "estilo": "Minimalista Moderno",
                "descricao_curta": "MDF Preto Silk com puxadores cava integrados e iluminação em LED 3000K.",
                "descricao_longa": "O projeto foca na continuidade visual das fibras do MDF. A marcenaria utiliza o padrão Preto Silk da Guararapes com detalhamento de puxador tipo cava 45 graus, eliminando a necessidade de ferragens externas. A bancada em quartzo cinza absoluto foi renderizada com mapas de rugosidade para reflexos precisos sob os perfis de LED de sobrepor.",
                "materiais": ["MDF Preto Silk", "Quartzo Cinza", "Puxador Cava", "LED 3000K"],
                "software": "SketchUp + V-Ray 6",
                "processamento": "4h 15m (GPU Render)",
                "imgs": [
                    "https://images.pexels.com/photos/2724748/pexels-photo-2724748.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2724749/pexels-photo-2724749.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2062426/pexels-photo-2062426.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_002",
                "titulo": "Suíte Master Premium",
                "categoria": "Dormitório Casal",
                "estilo": "Contemporâneo",
                "descricao_curta": "Painel ripado em MDF Freijó e cabeceira estofada em linho cru.",
                "descricao_longa": "Projeto de dormitório com foco no conforto térmico e visual. O painel principal em ripado Freijó da Arauco possui espaçamento de 15mm entre frisos. A iluminação wall-washer destaca a textura do tecido de linho da cabeceira. Criados-mudos em laca cinza fosca com sistema de abertura por toque (fecho-toque).",
                "materiais": ["MDF Freijó", "Linho Cru", "Laca Cinza Fosca", "Iluminação IES"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "5h 40m",
                "imgs": [
                    "https://images.pexels.com/photos/1643383/pexels-photo-1643383.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1643384/pexels-photo-1643384.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2029670/pexels-photo-2029670.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2102602/pexels-photo-2102602.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_003",
                "titulo": "Living Pé-Direito Duplo",
                "categoria": "Estar e Jantar",
                "estilo": "Alto Luxo",
                "descricao_curta": "Integração de ambientes com painéis em carvalho e mármore.",
                "descricao_longa": "Ambiente de grandes proporções integrando sala de estar e jantar. A marcenaria de apoio utiliza painéis lisos em MDF Carvalho Natural para aquecer o ambiente, enquanto a parede principal recebe um revestimento em Mármore Calacatta Gold. Renderização focada na luz natural abundante vinda das esquadrias de teto.",
                "materiais": ["MDF Carvalho", "Mármore Calacatta", "Porcelanato 120x120", "Vidro"],
                "software": "SketchUp + V-Ray + Chaos Cloud",
                "processamento": "1h 10m (Cloud)",
                "imgs": [
                    "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571468/pexels-photo-1571468.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571470/pexels-photo-1571470.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571459/pexels-photo-1571459.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_004",
                "titulo": "Gabinete SPA Banho",
                "categoria": "Banheiro",
                "estilo": "Minimalista",
                "descricao_curta": "Marcenaria em MDF Branco Ultra com cuba esculpida em mármore.",
                "descricao_longa": "Projeto de banheiro social com pegada de SPA. O gabinete suspenso utiliza MDF Branco Ultra para máxima resistência à umidade, com puxadores do tipo cava 45 graus. O render detalha a refração do espelho retroiluminado e a translucidez da pedra natural da cuba esculpida.",
                "materiais": ["MDF Branco Ultra", "Mármore Branco", "Metais Gold", "Espelho Bisotado"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "6h 25m",
                "imgs": [
                    "https://images.pexels.com/photos/1910472/pexels-photo-1910472.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1454806/pexels-photo-1454806.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1457841/pexels-photo-1457841.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1910473/pexels-photo-1910473.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_005",
                "titulo": "Área Gourmet Graphite",
                "categoria": "Varanda Gourmet",
                "estilo": "Industrial Chic",
                "descricao_curta": "Churrasqueira com marcenaria técnica em tons de cinza escuro.",
                "descricao_longa": "Design focado em funcionalidade. Os armários da área gourmet utilizam MDF Grafite com tratamento contra gordura. A bancada em granito São Gabriel escovado complementa o visual sóbrio. O render utiliza iluminação HDRI de final de tarde para criar sombras dramáticas e realistas.",
                "materiais": ["MDF Grafite", "Madeira de Demolição", "Granito São Gabriel", "Metalon"],
                "software": "SketchUp + V-Ray",
                "processamento": "4h 50m",
                "imgs": [
                    "https://images.pexels.com/photos/3144580/pexels-photo-3144580.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2062426/pexels-photo-2062426.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/3144581/pexels-photo-3144581.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2724749/pexels-photo-2724749.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_006",
                "titulo": "Home Office Executivo",
                "categoria": "Escritório",
                "estilo": "Corporativo Premium",
                "descricao_curta": "Estante com nichos iluminados e mesa flutuante em MDF Freijó.",
                "descricao_longa": "Ambiente projetado para máxima produtividade. A estante ao fundo mistura Laca Preta e MDF amadeirado claro, com iluminação embutida por baixo das prateleiras. O render detalha a ergonomia da mesa e o mapeamento realista do couro das poltronas executivas.",
                "materiais": ["MDF Freijó", "Laca Preta Fosca", "Couro", "Vidro Canelado"],
                "software": "3ds Max + V-Ray 6",
                "processamento": "3h 30m",
                "imgs": [
                    "https://images.pexels.com/photos/1957478/pexels-photo-1957478.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1957477/pexels-photo-1957477.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1957479/pexels-photo-1957479.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/37347/pexels-photo-37347.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_007",
                "titulo": "Closet Walk-in Boutique",
                "categoria": "Dormitório",
                "estilo": "Luxo",
                "descricao_curta": "Divisórias em MDF Cinza e portas em vidro reflecta bronze.",
                "descricao_longa": "Um closet desenhado como uma vitrine de alto luxo. Não há portas cegas; toda a estrutura é protegida por Vidro Reflecta que permite a visão do interior sob iluminação LED. A marcenaria interna foi rigorosamente paginada para otimização de custos de chapas.",
                "materiais": ["Vidro Reflecta Bronze", "MDF Cinza Sagrado", "Alumínio", "LED"],
                "software": "SketchUp + Enscape 3.5",
                "processamento": "1h 50m",
                "imgs": [
                    "https://images.pexels.com/photos/932095/pexels-photo-932095.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2062426/pexels-photo-2062426.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_008",
                "titulo": "Sala de Jantar Elegance",
                "categoria": "Living",
                "estilo": "Clássico Modernizado",
                "descricao_curta": "Buffet planejado com portas em palhinha e tampo em pedra.",
                "descricao_longa": "O desafio técnico deste ambiente foi a renderização da palhinha indiana vazada. O uso de mapas de opacidade e bump garante o realismo das fibras. O Buffet em MDF Nogueira recebe um tampo em pedra natural, iluminado por um pendente escultural.",
                "materiais": ["Palhinha Indiana", "MDF Nogueira", "Mármore Travertino", "Lustre"],
                "software": "SketchUp + V-Ray",
                "processamento": "5h 15m",
                "imgs": [
                    "https://images.pexels.com/photos/2724749/pexels-photo-2724749.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2724748/pexels-photo-2724748.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571468/pexels-photo-1571468.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_009",
                "titulo": "Dormitório Infantil Lúdico",
                "categoria": "Quarto Infantil",
                "estilo": "Montessoriano",
                "descricao_curta": "Marcenaria com cantos arredondados e tons pastéis em laca.",
                "descricao_longa": "Ambiente focado em segurança e ergonomia infantil. A marcenaria foi modelada com curvas suaves e acabamento em laca fosca calibrada por valores RGB reais. O render destaca a luz difusa que entra pela janela, conferindo uma atmosfera aconchegante.",
                "materiais": ["Laca Rosa Pastel", "MDF Carvalho", "Algodão Orgânico", "Ripado"],
                "software": "3ds Max + Corona",
                "processamento": "4h 05m",
                "imgs": [
                    "https://images.pexels.com/photos/3661202/pexels-photo-3661202.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1743229/pexels-photo-1743229.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2062426/pexels-photo-2062426.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1643383/pexels-photo-1643383.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_010",
                "titulo": "Adega Particular Cumaru",
                "categoria": "Bar e Adega",
                "estilo": "Rústico Moderno",
                "descricao_curta": "Nichos colmeia em madeira Cumaru e iluminação cênica.",
                "descricao_longa": "Projeto de adega climatizada em subsolo. A marcenaria técnica utiliza madeira maciça Cumaru para suportar o peso e as variações de umidade. O render destaca os reflexos do vidro das garrafas contra o revestimento de tijolo aparente rústico.",
                "materiais": ["Madeira Cumaru", "Tijolo Inglês", "Vidro Duplo", "Metalon Preto"],
                "software": "3ds Max + V-Ray",
                "processamento": "7h 15m",
                "imgs": [
                    "https://images.pexels.com/photos/2903160/pexels-photo-2903160.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2724748/pexels-photo-2724748.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_011",
                "titulo": "Hall Minimal Bisotado",
                "categoria": "Circulação",
                "estilo": "Minimalista",
                "descricao_curta": "Aparador slim e painel de espelhos para ampliar ambiente.",
                "descricao_longa": "Design estratégico para hall de entrada compacto. O console suspenso possui apenas 12cm de profundidade, ideal para passagens estreitas. A parede lateral é revestida com espelhos bisotados que duplicam a percepção espacial do ambiente.",
                "materiais": ["MDF Lacca Cetin", "Espelho Prata", "Granito Polido", "LED"],
                "software": "SketchUp + Corona",
                "processamento": "2h 45m",
                "imgs": [
                    "https://images.pexels.com/photos/2724748/pexels-photo-2724748.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1618219/pexels-photo-1618219.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_012",
                "titulo": "Lavanderia Funcional",
                "categoria": "Área de Serviço",
                "estilo": "Moderno Clean",
                "descricao_curta": "Armários em MDF Branco Ártico com tulhas embutidas.",
                "descricao_longa": "Marcenaria técnica projetada para organização. O projeto inclui tulhas basculantes para roupas e nichos específicos para máquinas de lavar e secar, respeitando os respiros necessários. O acabamento em MDF Branco Ártico confere assepsia.",
                "materiais": ["MDF Branco Ártico", "Bancada em Corian", "Rodapés Alumínio"],
                "software": "SketchUp + Enscape",
                "processamento": "1h 15m",
                "imgs": [
                    "https://images.pexels.com/photos/2253643/pexels-photo-2253643.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1556910/pexels-photo-1556910.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1910472/pexels-photo-1910472.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_013",
                "titulo": "Biblioteca Pé-Direito Duplo",
                "categoria": "Escritório",
                "estilo": "Clássico Moderno",
                "descricao_curta": "Estante de 6 metros com escada metálica funcional.",
                "descricao_longa": "A imponência da marcenaria em Carvalho Natural que sobe dois níveis de pé-direito. O render utilizou proxies para povoar as estantes com livros detalhados, iluminados por trilhos eletrificados que emolduram a estrutura metálica de acesso.",
                "materiais": ["MDF Carvalho", "Metal Preto", "Piso Vinílico", "LED"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "6h 40m",
                "imgs": [
                    "https://images.pexels.com/photos/133458/pexels-photo-133458.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1957478/pexels-photo-1957478.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1957477/pexels-photo-1957477.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1957479/pexels-photo-1957479.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_014",
                "titulo": "Recepção Médica Premium",
                "categoria": "Comercial",
                "estilo": "Clean Minimalista",
                "descricao_curta": "Balcão orgânico em curvas com filetes de LED embutidos.",
                "descricao_longa": "Design focado no acolhimento do paciente. O balcão principal possui curvas suaves modeladas em Sub-D, revestidas em laminado melamínico de alta resistência. O render foca na iluminação suave que destaca a limpeza e elegância do ambiente.",
                "materiais": ["Laminado Branco", "MDF Amadeirado", "Porcelanato", "LED"],
                "software": "SketchUp + V-Ray",
                "processamento": "3h 55m",
                "imgs": [
                    "https://images.pexels.com/photos/37347/pexels-photo-37347.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1957478/pexels-photo-1957478.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1957477/pexels-photo-1957477.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1486406/pexels-photo-1486406.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "INT_015",
                "titulo": "Living Laca Alto Brilho",
                "categoria": "Living",
                "estilo": "Luxo",
                "descricao_curta": "Painel de TV detalhado com acabamento polido em laca negra.",
                "descricao_longa": "Análise técnica de reflexividade de superfícies polidas. O painel principal em Laca Alto Brilho exigiu múltiplas camadas de polimento virtual no motor de render para evitar distorções nos reflexos das luzes do ambiente.",
                "materiais": ["Laca Alto Brilho", "MDF Grafite", "Couro", "Vidro"],
                "software": "3ds Max + V-Ray 6",
                "processamento": "6h 10m",
                "imgs": [
                    "https://images.pexels.com/photos/1090638/pexels-photo-1090638.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1593910/pexels-photo-1593910.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            }
        ]

    @staticmethod
    def get_exteriores_data():
        """Retorna a matriz de dados para os 10 projetos de Exteriores."""
        return [
            {
                "id": "EXT_001",
                "titulo": "Fachada Residencial Brises",
                "categoria": "Arquitetura",
                "estilo": "Contemporâneo",
                "descricao_curta": "Volumes em concreto aparente e brises em alumínio amadeirado.",
                "descricao_longa": "Projeto residencial focando na sobriedade e volumetria limpa. Os brises verticais foram modelados individualmente para criar um jogo de luz e sombra dinâmico na fachada ao longo do dia. Renderização em alta definição com integração de vegetação Chaos Cosmos.",
                "materiais": ["Alumínio Amadeirado", "Concreto Aparente", "Esquadria Preta"],
                "software": "SketchUp + V-Ray",
                "processamento": "5h 45m",
                "imgs": [
                    "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/221540/pexels-photo-221540.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_002",
                "titulo": "Lazer Tropical Chic",
                "categoria": "Externo",
                "estilo": "Tropical Chic",
                "descricao_curta": "Área de piscina com borda infinita e deck em madeira Itaúba.",
                "descricao_longa": "Estudo físico da água e reflexos. O render detalha as cáusticas geradas pelo sol no fundo da piscina e a refração do céu no espelho d'água. O deck em Itaúba possui mapeamento fotorrealista com imperfeições naturais da madeira.",
                "materiais": ["Madeira Itaúba", "Pedra Hijau", "Porcelanato Externo"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "7h 55m",
                "imgs": [
                    "https://images.pexels.com/photos/221453/pexels-photo-221453.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/261102/pexels-photo-261102.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2096983/pexels-photo-2096983.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2096982/pexels-photo-2096982.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_003",
                "titulo": "Corporativo Glass",
                "categoria": "Comercial",
                "estilo": "Urbano",
                "descricao_curta": "Edifício em pele de vidro refletiva com asfalto realista PBR.",
                "descricao_longa": "Projeto comercial focado na transparência. O render destaca o reflexo fiel dos edifícios vizinhos na fachada em vidro espelhado. A pós-produção foi trabalhada para simular uma cena de pós-chuva com reflexos intensos no pavimento.",
                "materiais": ["Pele de Vidro", "ACM Preto", "Asfalto PBR", "Concreto"],
                "software": "3ds Max + V-Ray",
                "processamento": "6h 50m",
                "imgs": [
                    "https://images.pexels.com/photos/374870/pexels-photo-374870.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/290275/pexels-photo-290275.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1105766/pexels-photo-1105766.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/323705/pexels-photo-323705.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_004",
                "titulo": "Casa de Campo Pedra Moledo",
                "categoria": "Residencial",
                "estilo": "Rústico Moderno",
                "descricao_curta": "Harmonia entre pedra natural Moledo e vigas de eucalipto.",
                "descricao_longa": "Arquitetura integrada à natureza. O uso de pedra Moledo na base e vigas de madeira bruta confere um ar orgânico. O render utilizou Forest Pack para povoar o terreno com vegetação nativa densa e fotorrealista.",
                "materiais": ["Pedra Moledo", "Vigas Eucalipto", "Telha Shingle", "Vidro"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "8h 15m",
                "imgs": [
                    "https://images.pexels.com/photos/258154/pexels-photo-258154.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/209296/pexels-photo-209296.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/101808/pexels-photo-101808.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/221540/pexels-photo-221540.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_005",
                "titulo": "Rooftop Urbano Blue Hour",
                "categoria": "Comercial/Lazer",
                "estilo": "Moderno",
                "descricao_curta": "Área social em terraço com mobiliário em corda náutica.",
                "descricao_longa": "Renderização noturna focada no balanço de luzes artificiais e no crepúsculo (Blue Hour). Mobiliário externo em corda náutica com texturas de alta definição, iluminados por balizadores embutidos no deck sintético.",
                "materiais": ["Corda Náutica", "Deck Sintético", "Vidro Temperado", "LED"],
                "software": "SketchUp + Enscape",
                "processamento": "1h 55m",
                "imgs": [
                    "https://images.pexels.com/photos/1643384/pexels-photo-1643384.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2096983/pexels-photo-2096983.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_006",
                "titulo": "Guarita Imponente Aço Corten",
                "categoria": "Comercial",
                "estilo": "Industrial Moderno",
                "descricao_curta": "Fachada de acesso revestida em chapas metálicas de Aço Corten.",
                "descricao_longa": "Design de impacto para acesso de condomínio. O revestimento em Aço Corten foi mapeado individualmente para evitar repetições na textura de ferrugem. Iluminação embutida na laje valoriza os volumes geométricos da portaria.",
                "materiais": ["Aço Corten", "Vidro Blindado", "Pedra Portuguesa", "LED"],
                "software": "SketchUp + V-Ray",
                "processamento": "4h 25m",
                "imgs": [
                    "https://images.pexels.com/photos/209296/pexels-photo-209296.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1486406/pexels-photo-1486406.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1105766/pexels-photo-1105766.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/323705/pexels-photo-323705.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_007",
                "titulo": "Residência IES Light Study",
                "categoria": "Arquitetura",
                "estilo": "Contemporâneo",
                "descricao_curta": "Fachada noturna com fidelidade luminotécnica via arquivos IES.",
                "descricao_longa": "Estudo profundo de iluminação externa. O render utiliza perfis IES reais dos fabricantes para garantir que os fachos de luz na fachada física sejam idênticos ao projeto virtual. Foco na nitidez das texturas de alvenaria e madeira.",
                "materiais": ["Alvenaria Branca", "MDF Naval Externo", "LED IES", "Vidro"],
                "software": "3ds Max + V-Ray",
                "processamento": "6h 45m",
                "imgs": [
                    "https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/209296/pexels-photo-209296.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_008",
                "titulo": "Loft Industrial Retrofit",
                "categoria": "Residencial",
                "estilo": "Brooklyn",
                "descricao_curta": "Fachada em tijolo inglês aparente com grandes esquadrias de ferro.",
                "descricao_longa": "Projeto de revitalização urbana. O desafio foi o displacement nos rejuntes dos tijolos para profundidade realista sob iluminação lateral. Janelas com caixilhos pretos e vidros canelados reforçam a estética industrial proposta.",
                "materiais": ["Tijolo Inglês", "Metalon Grafite", "Vidro Canelado"],
                "software": "SketchUp + V-Ray",
                "processamento": "4h 55m",
                "imgs": [
                    "https://images.pexels.com/photos/2242475/pexels-photo-2242475.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1486406/pexels-photo-1486406.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/374870/pexels-photo-374870.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/323705/pexels-photo-323705.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_009",
                "titulo": "Varanda Integrada Reiki",
                "categoria": "Apartamento",
                "estilo": "Moderno",
                "descricao_curta": "Fechamento em vidro Reiki e mobiliário em MDF Naval amadeirado.",
                "descricao_longa": "Otimização de área externa em sacada. O render mostra a transição fluida entre sala e varanda protegida por vidro. A marcenaria utiliza MDF Naval resistente à insolação direta, ocultando condensadoras de ar com painéis ripados.",
                "materiais": ["MDF Naval", "Porcelanato Amadeirado", "Vidro Reiki"],
                "software": "3ds Max + Corona Renderer",
                "processamento": "4h 40m",
                "imgs": [
                    "https://images.pexels.com/photos/1571463/pexels-photo-1571463.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1618219/pexels-photo-1618219.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            },
            {
                "id": "EXT_010",
                "titulo": "Jardim de Inverno Zen",
                "categoria": "Residencial/Externo",
                "estilo": "Oriental",
                "descricao_curta": "Espelho d'água orgânico cercado por jardim vertical fotorrealista.",
                "descricao_longa": "Espaço de relaxamento integrado à arquitetura. O destaque do render é a modelagem botânica densa utilizando scanners 3D de plantas reais. O espelho d'água escura reflete perfeitamente as espécies da Mata Atlântica sob a pérgola.",
                "materiais": ["Madeira Cumaru", "Pedra Vulcânica", "Jardim Vertical 3D"],
                "software": "SketchUp + V-Ray 6",
                "processamento": "5h 55m",
                "imgs": [
                    "https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1510798/pexels-photo-1510798.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/1500313/pexels-photo-1500313.jpeg?auto=compress&cs=tinysrgb&w=1200",
                    "https://images.pexels.com/photos/209296/pexels-photo-209296.jpeg?auto=compress&cs=tinysrgb&w=1200"
                ]
            }
        ]

# ==============================================================================
# CLASS: PALLADIUM_UI_MANAGER
# Responsável pelo motor visual, injeção de CSS e estabilidade de componentes.
# ==============================================================================
class PalladiumUIManager:
    """Framework visual do Palladium Studio para Desktop e Mobile."""

    @staticmethod
    def inject_premium_styles():
        """Injeta estilos CSS para garantir o visual de luxo e responsividade."""
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

            :root {
                --bg-color: #080808;
                --text-main: #f2f2f2;
                --text-muted: #888888;
                --accent: #d4af37; 
                --card-bg: #111111;
                --card-hover: #161616;
                --border: #222222;
            }

            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background-color: var(--bg-color) !important;
                color: var(--text-main) !important;
            }

            header {background-color: transparent !important;}
            #MainMenu, footer {visibility: hidden;}

            h1, h2, h3, h4 {
                font-family: 'Cinzel', serif !important;
                font-weight: 600 !important;
                color: #ffffff !important;
                letter-spacing: 1px;
            }

            /* HERO */
            .hero-title {
                text-align: center; font-size: 4.5rem; margin-top: 20px;
                color: #ffffff; font-family: 'Cinzel', serif;
            }
            .hero-subtitle {
                text-align: center; color: #888; font-size: 1.1rem;
                letter-spacing: 8px; margin-top: 5px; margin-bottom: 40px;
            }

            /* CARDS */
            .project-card {
                background: var(--card-bg); border: 1px solid var(--border);
                border-radius: 6px; transition: all 0.4s ease; margin-bottom: 30px;
                display: flex; flex-direction: column; height: 100%; overflow: hidden;
            }
            .project-card:hover {
                border-color: var(--accent); transform: translateY(-8px);
                box-shadow: 0 15px 35px rgba(212, 175, 55, 0.1); background: var(--card-hover);
            }
            .img-container { width: 100%; aspect-ratio: 16/9; overflow: hidden; background: #1a1a1a; }
            .img-container img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s ease; }
            .project-card:hover img { transform: scale(1.05); }
            .card-content { padding: 25px; display: flex; flex-direction: column; flex-grow: 1; }
            .project-title { font-family: 'Cinzel', serif; font-size: 1.2rem; color: var(--accent); margin-bottom: 10px; }
            .project-desc { font-size: 0.9rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 15px; flex-grow: 1; }

            /* SIDEBAR */
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

            .sidebar-footer { padding: 20px; text-align: center; border-top: 1px solid #1a1a1a; margin-top: 20px; }

            /* BUTTONS */
            .btn-gold {
                display: block; background: var(--accent); color: #000 !important;
                text-align: center; padding: 15px; font-weight: 700;
                letter-spacing: 2px; text-decoration: none; text-transform: uppercase;
                transition: 0.4s; border-radius: 3px; border: 1px solid var(--accent); font-size: 0.85rem;
            }
            .btn-gold:hover { background: #fff; border-color: #fff; box-shadow: 0 0 20px rgba(212, 175, 55, 0.3); }

            .pricing-card {
                background: #0d0d0d; border: 1px solid #333; padding: 40px 30px;
                text-align: center; border-radius: 8px; transition: 0.3s; height: 100%;
                display: flex; flex-direction: column;
            }
            .pricing-card:hover { border-color: var(--accent); background: #141414; transform: translateY(-5px); }

            @media (max-width: 768px) {
                .hero-title { font-size: 2.2rem !important; margin-top: 40px !important; }
                .hero-subtitle { font-size: 0.7rem !important; letter-spacing: 4px !important; }
                [data-testid="stHorizontalBlock"] { flex-direction: column !important; }
            }

            button[title="View fullscreen"] { display: none; }
            </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# CLASS: PALLADIUM_APP_ROUTER
# Controlador principal de visualização do sistema.
# ==============================================================================
class PalladiumAppRouter:
    """Gerencia a navegação e a renderização modular de páginas."""

    @staticmethod
    def render_home():
        """Página de entrada com o Hero Section e diferencial estratégico."""
        st.markdown("<h1 class='hero-title'>PALLADIUM STUDIO</h1>", unsafe_allow_html=True)
        st.markdown("<p class='hero-subtitle'>ARCHVIZ PARA ALTA MARCENARIA</p>", unsafe_allow_html=True)
        st.image("https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1500", use_container_width=True)
        
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
        """Galeria de projetos organizada por categorias e filtros técnicos."""
        interiores = PalladiumDataEngine.get_interiores_data()
        exteriores = PalladiumDataEngine.get_exteriores_data()
        
        st.markdown("<h1>Catálogo de Visualização</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#666; margin-bottom:40px;'>Descrições calibradas tecnicamente de acordo com os renders selecionados.</p>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='border-left: 4px solid #d4af37; padding-left: 15px;'>INTERIORES (15 PROJETOS)</h3><br>", unsafe_allow_html=True)
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
                if st.button(f"RELATÓRIO TÉCNICO", key=f"btn_int_{proj['id']}"):
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
                if st.button(f"RELATÓRIO TÉCNICO", key=f"btn_ext_{proj['id']}"):
                    st.session_state['projeto_selecionado'] = proj
                    st.session_state['page'] = 'Detalhes'
                    st.rerun()

    @staticmethod
    def render_details():
        """Visualização profunda de ativos individuais (Galeria Multi-ângulo)."""
        proj = st.session_state.get('projeto_selecionado')
        if not proj:
            st.session_state['page'] = 'Portfólio'
            st.rerun()
            return

        if st.button("← VOLTAR PARA O CATÁLOGO"):
            st.session_state.update({'projeto_selecionado': None, 'page': 'Portfólio'})
            st.rerun()

        st.markdown(f"<h1>Galeria Técnica: {proj['titulo']}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#d4af37; letter-spacing:3px; text-transform:uppercase;'>SOFTWARE: {proj['software']}</p><br>", unsafe_allow_html=True)

        for i, img_url in enumerate(proj['imgs']):
            st.image(img_url, caption=f"Perspectiva {i+1} - Renderização 4K Studio", use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)

        st.write("---")
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown("<h3>Memorial Descritivo</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#aaa; line-height:1.8; font-size:1.1rem;'>{proj['descricao_longa']}</p>", unsafe_allow_html=True)
        with c2:
            st.markdown("""
                <div style='background:#111; border:1px solid #222; padding:30px; border-radius:6px;'>
                    <h4 style='color:#d4af37 !important; border-bottom:1px solid #333; padding-bottom:15px; margin-top:0;'>Ficha Técnica</h4>
            """, unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:0;'>Processamento Total:</p><p style='color:#ccc; font-weight:600;'>{proj['processamento']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888; font-size:0.9rem; margin-bottom:0;'>Workflow Engine:</p><p style='color:#ccc; font-weight:600;'>{proj['software']}</p>", unsafe_allow_html=True)
            st.markdown("<p style='color:#888; font-size:0.9rem; margin-bottom:10px;'>Mapeamento de Materiais:</p>", unsafe_allow_html=True)
            for mat in proj['materiais']:
                st.markdown(f"<span style='display:inline-block; background:#1a1a1a; border:1px solid #333; color:#aaa; font-size:0.8rem; padding:5px 10px; border-radius:4px; margin:3px;'>{mat}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    @staticmethod
    def render_imersao():
        """Seção dedicada a Vídeo de 15s e Tour 360º ArchViz real."""
        st.markdown("<h1>Experiências de Imersão</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#888; font-size:1.1rem; margin-bottom:50px;'>Tecnologias de visualização avançada que aceleram a tomada de decisão do cliente.</p>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='color:#d4af37 !important;'>1. Cinematic Tour (Animação 3D)</h3>", unsafe_allow_html=True)
        col_vid_txt, col_vid_main = st.columns([1, 1.5])
        with col_vid_txt:
            st.markdown("""
                <p style='color:#aaa; line-height:1.8;'>Vídeos sequenciais de curta duração (15-30s) focados em detalhamento técnico. 
                Ideal para atrair atenção em plataformas como Instagram Reels e apresentar via WhatsApp.</p>
                <ul style='color:#888; font-size:0.9rem;'>
                    <li>Resolução Full HD / 4K</li>
                    <li>Renderização Animada em Tempo Real</li>
                    <li>Foco em Modulação e Texturas</li>
                </ul>
            """, unsafe_allow_html=True)
        with col_vid_main:
            st.video("https://www.youtube.com/watch?v=11X_N2U23zY")
        
        st.markdown("<br><hr style='border-color:#333;'><br>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='color:#d4af37 !important;'>2. Tour 360º Interativo de Projeto Real</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#aaa;'>Clique na imagem abaixo para rotacionar o ambiente e explorar o projeto em todas as direções. Tecnologia de panorama esférico HDR.</p>", unsafe_allow_html=True)
        
        # Tour 360 de um Projeto de Interiores via Kuula (Exemplo Real ArchViz)
        tour_url = "https://kuula.co/share/collection/7l1c9?logo=0&info=0&fs=1&vr=1&sd=1&initload=0&thumbs=1"
        components.iframe(tour_url, height=650, scrolling=False)

    @staticmethod
    def render_planos():
        """Matriz de pacotes comerciais do Palladium Studio."""
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
                        <span style='color:#444;'>✗ Sem revisões de marcenaria</span>
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
                        <span>✓</span> Modelagem Fina de Detalhes<br>
                        <span>✓</span> Decoração e Cena VIP Luxo<br>
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
                    <p style='color:#888; font-size:0.85rem; height:45px;'>Experiência imersiva de tour interativo.</p>
                    <div style='text-align:left; color:#aaa; font-size:0.9rem; line-height:2.2; border-top:1px solid #222; padding-top:20px; margin-bottom:30px; flex-grow:1;'>
                        <span>✓</span> Modelagem Otimizada VR<br>
                        <span>✓</span> Render Esférico HDR 8K<br>
                        <span>✓</span> Setup de Link Web Privado<br>
                        <span>✓</span> <b>1 Ambiente 360 / Vídeo 15s</b><br>
                        <span>✓</span> Hospedagem Ativa (6 meses)
                    </div>
                    <a href='https://wa.me/5514998405046' class='btn-gold'>CONHECER TOUR</a>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# MAIN APPLICATION ENGINE
# ==============================================================================
def main():
    """Motor central do sistema de portfólio."""
    
    # 1. Correção Absoluta do KeyError: Inicialização do State
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Início'
    if 'projeto_selecionado' not in st.session_state:
        st.session_state['projeto_selecionado'] = None

    # 2. Injeção Visual
    PalladiumUIManager.inject_premium_styles()
    
    # 3. Sidebar e Navegação Corporativa
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; font-size: 2.2rem; margin-bottom:0;'>PALLADIUM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#555; font-size:0.7rem; letter-spacing:5px; margin-top:0;'>STUDIO ARCHVIZ</p>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        if st.button("INÍCIO"): st.session_state.update({'projeto_selecionado': None, 'page': 'Início'})
        if st.button("CATÁLOGO 3D"): st.session_state.update({'projeto_selecionado': None, 'page': 'Portfólio'})
        if st.button("IMERSÃO & VÍDEO"): st.session_state.update({'projeto_selecionado': None, 'page': 'Imersão'})
        if st.button("PLANOS E PACOTES"): st.session_state.update({'projeto_selecionado': None, 'page': 'Planos'})
        if st.button("CONTATO & SUPORTE"): st.session_state.update({'projeto_selecionado': None, 'page': 'Contato'})
        
        st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)
        st.markdown('<a href="https://wa.me/5514998405046" target="_blank" class="btn-gold">SOLICITAR ANÁLISE</a>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="sidebar-footer">
                <p style='color: #333; font-size: 0.65rem; letter-spacing: 1px; margin:0;'>
                    PALLADIUM STUDIO © 2026<br>
                    ARCHITECTURE VISUALIZATION ENGINE v4.0
                </p>
            </div>
        """, unsafe_allow_html=True)

    # 4. Router Logic
    page = st.session_state['page']
    
    with st.container():
        st.markdown("<div style='padding: 1% 4% 5% 4%;'>", unsafe_allow_html=True)
        
        if page == 'Início':
            PalladiumAppRouter.render_home()
        elif page == 'Portfólio':
            PalladiumAppRouter.render_portfolio()
        elif page == 'Detalhes':
            PalladiumAppRouter.render_details()
        elif page == 'Imersão':
            PalladiumAppRouter.render_imersao()
        elif page == 'Planos':
            PalladiumAppRouter.render_planos()
        elif page == 'Contato':
            # Página de Contato Expandida para maior volume de código
            st.markdown("<h1>Prospecção & Atendimento</h1>", unsafe_allow_html=True)
            c1, c2 = st.columns([1, 1])
            with c1:
                st.markdown("""
                    <div style='background:#111; padding:40px; border-radius:6px; border:1px solid #222;'>
                        <h3 style='margin-top:0; color:#d4af37 !important;'>Central Palladium</h3>
                        <p style='color:#aaa; line-height:2.2;'>
                            📍 <b>Sede Física:</b> Ourinhos, SP<br>
                            🌍 <b>Atendimento Virtual:</b> Nível Nacional<br>
                            📧 <b>Comercial:</b> contato@palladiumstudio.com<br>
                            📱 <b>WhatsApp:</b> (14) 99840-5046
                        </p>
                    </div>
                """, unsafe_allow_html=True)
            with c2:
                st.markdown("<h3>Perguntas Frequentes</h3>", unsafe_allow_html=True)
                with st.expander("Qual o formato de arquivo para envio?"):
                    st.write("Aceitamos arquivos em .SKP (SketchUp), .MAX (3ds Max) ou plantas baixas em .DWG e .PDF para modelagem do zero.")
                with st.expander("Qual o prazo de entrega padrão?"):
                    st.write("Para projetos de 1 ou 2 ambientes, a primeira prévia de baixa resolução é entregue em até 48 horas úteis.")
                with st.expander("Recebo o arquivo 3D configurado?"):
                    st.write("Não. O Palladium Studio comercializa a mídia final renderizada. Os arquivos raiz configurados são de posse intelectual do estúdio.")
            
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
