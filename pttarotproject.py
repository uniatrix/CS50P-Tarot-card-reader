import random
import openai


class TarotCard:
    def __init__(self, name, meaning, category, suit=None, number=None):
        self.name = name
        self.meaning = meaning
        self.category = category
        self.suit = suit
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.meaning}"


class TarotDeck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def draw(self, num_cards):
        return random.sample(self.cards, num_cards)


major_arcana_cards = {
    "O Louco": "O início de uma nova jornada, inocência, espontaneidade",
    "O Mago": "Manifestação, engenhosidade, poder",
    "A Sacerdotisa": "Intuição, conhecimento inconsciente, mistério",
    "A Imperatriz": "Fertilidade, nutrição, abundância",
    "O Imperador": "Autoridade, estabilidade, liderança",
    "O Hierofante": "Tradição, espiritualidade, conformidade",
    "Os Enamorados": "Amor, relacionamentos, escolhas",
    "A Carruagem": "Força de vontade, determinação, vitória",
    "A Força": "Coragem, força interior, paciência",
    "O Eremita": "Solidão, orientação interior, introspecção",
    "A Roda da Fortuna": "Sorte, destino, ciclos",
    "A Justiça": "Justiça, equilíbrio, verdade",
    "O Enforcado": "Deixar ir, entrega, nova perspectiva",
    "A Morte": "Transformação, finais, começos",
    "A Temperança": "Equilíbrio, harmonia, moderação",
    "O Diabo": "Materialismo, escravidão, tentação",
    "A Torre": "Abalo repentino, caos, revelação",
    "A Estrela": "Esperança, inspiração, insight espiritual",
    "A Lua": "Ilusão, intuição, o subconsciente",
    "O Sol": "Sucesso, alegria, vitalidade",
    "O Julgamento": "Reckoning, renascimento, chamado interno",
    "O Mundo": "Conclusão, cumprimento, totalidade"
}


minor_arcana_wands = {
    "Ás de Paus": ["Inspiração, novos começos, potencial", "Paus", 1],
    "Dois de Paus": ["Planejamento, escolhas, visão futura", "Paus", 2],
    "Três de Paus": ["Expansão, exploração, previsão", "Paus", 3],
    "Quatro de Paus": ["Celebração, harmonia, volta para casa", "Paus", 4],
    "Cinco de Paus": ["Competição, conflito, desafios", "Paus", 5],
    "Seis de Paus": ["Vitória, reconhecimento, realização", "Paus", 6],
    "Sete de Paus": ["Defesa, determinação, perseverança", "Paus", 7],
    "Oito de Paus": ["Rapidez, progresso, comunicação", "Paus", 8],
    "Nove de Paus": ["Resiliência, força interior, persistência", "Paus", 9],
    "Dez de Paus": ["Fardo, responsabilidade, trabalho árduo", "Paus", 10],
    "Valete de Paus": ["Entusiasmo, exploração, novas oportunidades", "Paus", "Página"],
    "Cavaleiro de Paus": ["Ação, aventura, impulsividade", "Paus", "Cavaleiro"],
    "Rainha de Paus": ["Confiança, liderança, independência", "Paus", "Rainha"],
    "Rei de Paus": ["Carisma, visão, inspiração", "Paus", "Rei"],
}


minor_arcana_cups = {
    "Ás de Copas": ["Novos começos emocionais, amor, intuição", "Copas", 1],
    "Dois de Copas": ["Amor, parceria, harmonia", "Copas", 2],
    "Três de Copas": ["Celebração, amizade, alegria", "Copas", 3],
    "Quatro de Copas": ["Contemplação, apatia, introspecção", "Copas", 4],
    "Cinco de Copas": ["Perda, luto, desapontamento", "Copas", 5],
    "Seis de Copas": ["Nostalgia, infância, memórias", "Copas", 6],
    "Sete de Copas": ["Ilusão, escolhas, devaneios", "Copas", 7],
    "Oito de Copas": ["Seguir em frente, busca de significado", "Copas", 8],
    "Nove de Copas": ["Desejos realizados, contentamento, satisfação", "Copas", 9],
    "Dez de Copas": ["Realização emocional, felicidade, família", "Copas", 10],
    "Valete de Copas": ["Criatividade, mensagens intuitivas, novas percepções", "Copas", "Página"],
    "Cavaleiro de Copas": ["Romance, sonho, cavalheirismo", "Copas", "Cavaleiro"],
    "Rainha de Copas": ["Empatia, compaixão, segurança emocional", "Copas", "Rainha"],
    "Rei de Copas": ["Maturidade emocional, controle, equilíbrio", "Copas", "Rei"],
}


minor_arcana_swords = {
    "Ás de Espadas": ["Clareza, verdade, clareza mental", "Espadas", 1],
    "Dois de Espadas": ["Escolhas difíceis, indecisão, trégua", "Espadas", 2],
    "Três de Espadas": ["Desgosto, tristeza, luto", "Espadas", 3],
    "Quatro de Espadas": ["Descanso, recuperação, meditação", "Espadas", 4],
    "Cinco de Espadas": ["Conflito, derrota, manipulação", "Espadas", 5],
    "Seis de Espadas": ["Transição, seguir em frente, alívio", "Espadas", 6],
    "Sete de Espadas": ["Engano, traição, furtividade", "Espadas", 7],
    "Oito de Espadas": ["Sentir-se encurralado, restrições autoimpostas", "Espadas", 8],
    "Nove de Espadas": ["Ansiedade, pesadelos, preocupação", "Espadas", 9],
    "Dez de Espadas": ["Fundo do poço, fracasso, crise", "Espadas", 10],
    "Valete de Espadas": ["Curiosidade, novas ideias, energia jovem", "Espadas", "Página"],
    "Cavaleiro de Espadas": ["Ação, assertividade, determinação", "Espadas", "Cavaleiro"],
    "Rainha de Espadas": ["Clareza, independência, intelecto afiado", "Espadas", "Rainha"],
    "Rei de Espadas": ["Força mental, racionalidade, liderança", "Espadas", "Rei"],
}


minor_arcana_pentacles = {
    "Ás de Ouros": ["Manifestação, novas oportunidades, prosperidade", "Ouros", 1],
    "Dois de Ouros": ["Equilíbrio, adaptabilidade, malabarismo de prioridades", "Ouros", 2],
    "Três de Ouros": ["Trabalho em equipe, colaboração, artesanato", "Ouros", 3],
    "Quatro de Ouros": ["Estabilidade, segurança, possessividade", "Ouros", 4],
    "Cinco de Ouros": ["Dificuldades, pobreza, isolamento", "Ouros", 5],
    "Seis de Ouros": ["Generosidade, caridade, dar e receber", "Ouros", 6],
    "Sete de Ouros": ["Paciência, espera, investimento", "Ouros", 7],
    "Oito de Ouros": ["Diligência, artesanato, desenvolvimento de habilidades", "Ouros", 8],
    "Nove de Ouros": ["Abundância, luxo, autossuficiência", "Ouros", 9],
    "Dez de Ouros": ["Legado, herança, riqueza familiar", "Ouros", 10],
    "Valete de Ouros": ["Exploração, praticidade, aprendizado", "Ouros", "Página"],
    "Cavaleiro de Ouros": ["Responsabilidade, trabalho árduo, confiabilidade", "Ouros", "Cavaleiro"],
    "Rainha de Ouros": ["Cuidado, riqueza, praticidade", "Ouros", "Rainha"],
    "Rei de Ouros": ["Prosperidade, estabilidade, segurança financeira", "Ouros", "Rei"],
}


def create_card_objects():
    deck = TarotDeck()
    
    # Create major arcana cards
    for name, meaning in major_arcana_cards.items():
        card = TarotCard(name, meaning, "Major Arcana")
        deck.add_card(card)

    # Create minor arcana cards
    for suit in [minor_arcana_wands, minor_arcana_cups, minor_arcana_swords, minor_arcana_pentacles]:
        for name, card_data in suit.items():
            card = TarotCard(name, card_data[0], "Minor Arcana", card_data[1], card_data[2])
            deck.add_card(card)

    return deck


def gpt_integration(messages):
    openai.api_key = "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"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]

def get_user_input():
    question = input("\nO que gostaria de perguntar ao Tarot? ")
    
    while True:
        try:
            num_cards = int(input("\nCom quantas cartas deseja realizar a tiragem? "))
            if 1 <= num_cards <= 20:
                return question, num_cards
            else:
                print("Por favor selecione entre 1 e 20 cartas.")
        except ValueError:
            print("Comando invalido.")

def tarot_read():
    tarot_deck = create_card_objects()
    question, num_cards = get_user_input()

    # Randomly drawing cards
    selected_cards = tarot_deck.draw(num_cards)
    
    # Create a list of messages for the OpenAI chat
    messages = [{"role": "system", "content": "Você é um tarólogo experiente."}]
    messages.append({"role": "user", "content": f"Faça um jogo de Tarot detalhado que unifique as cartas citadas e que contenha especificamente este questionamento: '{question}'"})  # Add the user's question to messages
    
    # Include the drawn cards in the prompt
    card_details = "\n".join([f"Carta: {card.name}\nSignificado: {card.meaning}" for card in selected_cards])
    messages.append({"role": "user", "content": f"Cartas tiradas:\n{card_details}"})
    
    # Display cards and details
    print("\nCartas tiradas:\n")
    for card in selected_cards:
        print(f"Carta: {card.name}")
        print(f"Significado: {card.meaning}")
        if card.category == "Minor Arcana":
            print(f"Naipe: {card.suit}")
            print(f"Número/Tipo: {card.number}")
        print()
    
    print(f"Sua pergunta: {question}")
    print("\nGerando sua leitura, aguarde.")
    print("\n...")
    
    # Call the GPT integration function for the assistant's response
    response = gpt_integration(messages)
    print("\nLeitura do seu jogo do tarot:\n")
    print(f"{response}\n")


def main():
    tarot_read()


if __name__ == "__main__":
    main()