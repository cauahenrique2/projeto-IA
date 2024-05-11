
import google.generativeai as genai

# Substitua pelo seu API key real
GOOGLE_API_KEY = "digite sua API aqui"

def informative_research(prompt):
    """
    Fornece respostas informativas sobre partes do corpo humano em português.

    Args:
        prompt: A consulta do usuário.

    Returns:
        Uma string contendo informações relevantes em português ou uma mensagem de erro clara.
    """

    # Configurar a chave da API
    genai.configure(api_key=GOOGLE_API_KEY)

    # Lista expandida de palavras-chave relacionadas ao corpo humano
    palavras_chave_corpo = [
        "Cabeça","Crânio","Cocuruto","Testa","Nuca","Careca","Calota craniana","Olho",
        "Óculo","Vista","Bulbo ocular","Retina","Íris","Pupila","Córnea","Nariz","Órgão olfativo",
        "Narina","Olfato","Ponte nasal","Narinete","Orelha","Aurícula","Pavilhão auditivo",
        "Canal auditivo","Tímpano","Lóbulo da orelha","Boca","Cavidade bucal","Lábio",
        "Língua","Dente","Gengiva","Palato","Faringe","Tronco","Torso","Caixa torácica",
        "Abdômen","Coluna vertebral","Costela","Peito","Tórax","Seio","Mama","Mamilo"
        "Esterno","Abdômen","Barriga","Ventre","Umbigo","Região abdominal","Víscera",
        "Costas","Dorso","Coluna vertebral","Omoplata","Lombar","Membros Superiores",
        "Braço","Membro superior","Antebraço","Cotovelo","Punho","Mão","Dedo","Polegar",
        "Indicador","Médio","Anelar","Mindinho","Membros Inferiores","Perna","Membro inferior",
        "Coxa","Joelho","Canela","Tornozelo","Pé","Planta do pé","Dorso do pé",
        "Dedos do pé","Calcanhar","Dedão do pé","Órgãos Internos","Coração","Miocárdio",
        "Pericárdio","Válvulas cardíacas","Átrios","Ventrículos","Pulmão","Alvéolos pulmonares",
        "Brônquios","Traqueia","Fígado","Lóbulo hepático","Ducto biliar","Vesícula biliar",
        "Rim","Cápsula renal","Córtex renal","Medula renal","Ureter","Bexiga","Uretra",
        "Cérebro","Cérebro anterior","Cérebro médio","Cérebro posterior","Cerebelo",
        "Tronco encefálico","Medula espinhal","Pele","Epiderme","Derme","Hipoderme"
        ,"Sangue","Plasma","Glóbulos vermelhos","Glóbulos brancos","Plaquetas" 
    ]

    # Listar modelos disponíveis que suportam geração de conteúdo
    models = [m for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

    if not models:
        return "Erro: Nenhum modelo adequado encontrado para geração de conteúdo."

    # Escolher um modelo apropriado (considerar fatores como adequação à tarefa e desempenho)
    model = genai.GenerativeModel(model_name="gemini-1.0-pro")  # Escolha de exemplo

    generation_config = {
        "candidate_count": 1,
    }

    safety_settings = {
        "HARASSMENT": "BLOCK_NONE",
        "HATE": "BLOCK_NONE",
        "SEXUAL": "BLOCK_NONE",
        "DANGEROUS": "BLOCK_NONE",
    }

    chat = model.start_chat(history=[])

    # Manipulação aprimorada de prompts para melhor precisão
    palavra_relacionada = None
    prompt_lower = prompt.lower()
    for palavra in palavras_chave_corpo:
        if palavra.lower() in prompt_lower:
            palavra_relacionada = palavra
            break

    if palavra_relacionada:
        # Focar a geração em partes do corpo humano
        # Definir idioma para Português
        response = chat.send_message(f"conforme a anatomia'{palavra_relacionada}' a uma parte do corpo humano, em uma frase curta em português.")
    else:
        # Informar o erro se nenhuma palavra relacionada ao corpo humano for encontrada
        return "Erro: Nenhuma associação encontrada como uma partes do corpo humano."

    return response.text


while True:
    prompt = input("Esperando prompt (ou 'fim' para sair): ")
    if prompt == "fim":
        break

    response = informative_research(prompt)
    print("Resposta:", response, "\n")
