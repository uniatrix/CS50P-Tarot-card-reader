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
    "The Fool": "The beginning of a new journey, innocence, spontaneity",
    "The Magician": "Manifestation, resourcefulness, power",
    "The High Priestess": "Intuition, unconscious knowledge, mystery",
    "The Empress": "Fertility, nurturing, abundance",
    "The Emperor": "Authority, stability, leadership",
    "The Hierophant": "Tradition, spirituality, conformity",
    "The Lovers": "Love, relationships, choices",
    "The Chariot": "Willpower, determination, victory",
    "Strength": "Courage, inner strength, patience",
    "The Hermit": "Solitude, inner guidance, introspection",
    "Wheel of Fortune": "Luck, destiny, cycles",
    "Justice": "Fairness, balance, truth",
    "The Hanged Man": "Letting go, surrender, new perspective",
    "Death": "Transformation, endings, beginnings",
    "Temperance": "Balance, harmony, moderation",
    "The Devil": "Materialism, bondage, temptation",
    "The Tower": "Sudden upheaval, chaos, revelation",
    "The Star": "Hope, inspiration, spiritual insight",
    "The Moon": "Illusion, intuition, the subconscious",
    "The Sun": "Success, joy, vitality",
    "Judgment": "Reckoning, rebirth, inner calling",
    "The World": "Completion, fulfillment, wholeness"
}


minor_arcana_wands = {
    "Ace of Wands": ["Inspiration, new beginnings, potential", "Wands", 1],
    "Two of Wands": ["Planning, choices, future vision", "Wands", 2],
    "Three of Wands": ["Expansion, exploration, foresight", "Wands", 3],
    "Four of Wands": ["Celebration, harmony, homecoming", "Wands", 4],
    "Five of Wands": ["Competition, conflict, challenges", "Wands", 5],
    "Six of Wands": ["Victory, recognition, achievement", "Wands", 6],
    "Seven of Wands": ["Defense, determination, perseverance", "Wands", 7],
    "Eight of Wands": ["Swiftness, progress, communication", "Wands", 8],
    "Nine of Wands": ["Resilience, inner strength, persistence", "Wands", 9],
    "Ten of Wands": ["Burden, responsibility, hard work", "Wands", 10],
    "Page of Wands": ["Enthusiasm, exploration, new opportunities", "Wands", "Page"],
    "Knight of Wands": ["Action, adventure, impulsiveness", "Wands", "Knight"],
    "Queen of Wands": ["Confidence, leadership, independence", "Wands", "Queen"],
    "King of Wands": ["Charisma, vision, inspiration", "Wands", "King"],
}


minor_arcana_cups = {
    "Ace of Cups": ["Emotional new beginnings, love, intuition", "Cups", 1],
    "Two of Cups": ["Love, partnership, harmony", "Cups", 2],
    "Three of Cups": ["Celebration, friendship, joy", "Cups", 3],
    "Four of Cups": ["Contemplation, apathy, introspection", "Cups", 4],
    "Five of Cups": ["Loss, grief, disappointment", "Cups", 5],
    "Six of Cups": ["Nostalgia, childhood, memories", "Cups", 6],
    "Seven of Cups": ["Illusion, choices, daydreams", "Cups", 7],
    "Eight of Cups": ["Walking away, searching for meaning", "Cups", 8],
    "Nine of Cups": ["Wishes fulfilled, contentment, satisfaction", "Cups", 9],
    "Ten of Cups": ["Emotional fulfillment, happiness, family", "Cups", 10],
    "Page of Cups": ["Creativity, intuitive messages, new insights", "Cups", "Page"],
    "Knight of Cups": ["Romantic, dreamy, chivalrous", "Cups", "Knight"],
    "Queen of Cups": ["Empathy, compassion, emotional security", "Cups", "Queen"],
    "King of Cups": ["Emotional maturity, control, balance", "Cups", "King"],
}


minor_arcana_swords = {
    "Ace of Swords": ["Clarity, truth, mental clarity", "Swords", 1],
    "Two of Swords": ["Difficult choices, indecision, truce", "Swords", 2],
    "Three of Swords": ["Heartbreak, sorrow, grief", "Swords", 3],
    "Four of Swords": ["Rest, recuperation, meditation", "Swords", 4],
    "Five of Swords": ["Conflict, defeat, manipulation", "Swords", 5],
    "Six of Swords": ["Transition, moving on, relief", "Swords", 6],
    "Seven of Swords": ["Deception, betrayal, stealth", "Swords", 7],
    "Eight of Swords": ["Feeling trapped, self-imposed restrictions", "Swords", 8],
    "Nine of Swords": ["Anxiety, nightmares, worry", "Swords", 9],
    "Ten of Swords": ["Rock bottom, failure, crisis", "Swords", 10],
    "Page of Swords": ["Curiosity, new ideas, youthful energy", "Swords", "Page"],
    "Knight of Swords": ["Action, assertiveness, determination", "Swords", "Knight"],
    "Queen of Swords": ["Clarity, independence, sharp intellect", "Swords", "Queen"],
    "King of Swords": ["Mental strength, rationality, leadership", "Swords", "King"],
}


minor_arcana_pentacles = {
    "Ace of Pentacles": ["Manifestation, new opportunities, prosperity", "Pentacles", 1],
    "Two of Pentacles": ["Balance, adaptability, juggling priorities", "Pentacles", 2],
    "Three of Pentacles": ["Teamwork, collaboration, craftsmanship", "Pentacles", 3],
    "Four of Pentacles": ["Stability, security, possessiveness", "Pentacles", 4],
    "Five of Pentacles": ["Hardship, poverty, isolation", "Pentacles", 5],
    "Six of Pentacles": ["Generosity, charity, giving and receiving", "Pentacles", 6],
    "Seven of Pentacles": ["Patience, waiting, investment", "Pentacles", 7],
    "Eight of Pentacles": ["Diligence, craftsmanship, skill development", "Pentacles", 8],
    "Nine of Pentacles": ["Abundance, luxury, self-reliance", "Pentacles", 9],
    "Ten of Pentacles": ["Legacy, inheritance, family wealth", "Pentacles", 10],
    "Page of Pentacles": ["Exploration, practicality, learning", "Pentacles", "Page"],
    "Knight of Pentacles": ["Responsibility, hard work, reliability", "Pentacles", "Knight"],
    "Queen of Pentacles": ["Nurturing, wealth, practicality", "Pentacles", "Queen"],
    "King of Pentacles": ["Prosperity, stability, financial security", "Pentacles", "King"],
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
    openai.api_key = "PROVIVE HERE YOUR API KEY"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]

def get_user_input():
    question = input("\nWhat would you like to ask the Tarot? ")
    
    while True:
        try:
            num_cards = int(input("\nHow many cards do you want to draw? "))
            if 1 <= num_cards <= 20:
                return question, num_cards
            else:
                print("Please select between 1 and 20 cards.")
        except ValueError:
            print("Invalid input.")

def tarot_read():
    tarot_deck = create_card_objects()
    question, num_cards = get_user_input()

    # Randomly drawing cards
    selected_cards = tarot_deck.draw(num_cards)
    
    # Create a list of messages for the OpenAI chat
    messages = [{"role": "system", "content": "You are a tarot card reader expert."}]
    messages.append({"role": "user", "content": f"Make a detailed tarot reading that unifies the cards mentioned and specifically contains this question: '{question}'"})  # Add the user's question to messages
    
    # Include the drawn cards in the prompt
    card_details = "\n".join([f"Card: {card.name}\nMeaning: {card.meaning}" for card in selected_cards])
    messages.append({"role": "user", "content": f"Cards Drawn:\n{card_details}"})
    
    # Display cards and details
    print("\nYour Tarot Reading:\n")
    for card in selected_cards:
        print(f"Card: {card.name}")
        print(f"Meaning: {card.meaning}")
        if card.category == "Minor Arcana":
            print(f"Suit: {card.suit}")
            print(f"Number/Type: {card.number}")
        print()
    
    print(f"What you asked the Tarot: {question}")
    print("\nGenerating your tarot reading, please wait.")
    print("\n...")
    
    # Call the GPT integration function for the assistant's response
    response = gpt_integration(messages)
    print("\nYour tarot reading:\n")
    print(f"{response}\n")


def main():
    tarot_read()


if __name__ == "__main__":
    main()