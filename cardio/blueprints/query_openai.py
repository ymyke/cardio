import openai

openai.api_key = "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"
# FIXME ^ remove and revoke!

query_blueprint = """\
I'm developing a card game where cards have different attributes and looking to name some new cards.


EXAMPLES:
Card(name='1', power=0, health=1, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]) -> ANSWER: 1: Hamster [small, weak, cheap, non-skilled]
Card(name='2', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Spines]) -> ANSWER: 2: Porcupine [small, low power/health, spines]
Card(name='3', power=6, health=4, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]) -> ANSWER: 3: Grizzly Bear [very strong, quite expensive]
Card(name='4', power=1, health=4, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]) -> ANSWER: 4: Armadillo [low power, high health, no skills]
Card(name='5', power=0, health=1, costs_fire=1, costs_spirits=0, has_spirits=10, has_fire=1, skills=[]) -> ANSWER: 5: Unicorn [highly spirited]


TASK: Suggest a name for the following cards:
{}

RULES: 
- The name must have no more than 12 characters. 
- Use only animal names, but fantastical ones. Names of other cards in the game are: Hamster, Koala, Porcupine, Lynx, Weasel, Church Mouse. 
- Take the attribute values (and their min/max) and the skill names into account and suggest a name that fits with the overall character of a card. 
- Keep in mind the min max values per attribute and relate to these as well: power: [0-10], health: [1-10], costs_fire: [0-6], costs_spirits: [0-8], has_spirits: [0-8], has_fire: [0-6], and a card can have up to 6 skills.
- Answer only with the number and the name for each card and a short explanation, nothing else.
- The explanation should argue how the name is related to the card's attributes and skills.
- Make sure the name is not any of these: Hedgehog, Hamster, Koala, Porcupine
"""

# TODO Start adding all the existing cards to the query?


def query_openai(cards_str: str) -> str:
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query_blueprint.format(cards_str)}],
    )
    return chat_completion.choices[0].message.content
