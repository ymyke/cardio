
# Main concepts and terminology

Refer to the documentation with each class or module for details.

- **Card**
  - A card can have/produce (inner) fire and/or spirits as a resource.
  - A card can cost (inner) fire and/or spirits to bring into play.
  - A card can have 0-n skills.
- **Card Blueprints:** Used to instantiate concrete cards from.
- **Deck:** A collection of cards.
  - The human player has a "main" deck with all the cards she owns.
  - During a fight, the human player has 4 decks: the hand, the draw deck, the hamster
    deck, and the discard pile (used deck).
- **Skill:** A special ability of a card. Can be positive or negative or in-between.
- **Run:** A run is a single game.
  - A run starts with a starting deck that is determined according to a certain
    mechanism, see below. 
  - Runs are fully predetermined based on some seed, i.e., they don't adapt based on the
    player's behavior in any way.
  - Runs are indefinite. A player gets as far as she gets.
  - A run represents the entire map and keeps track of the current location and the path
    taken so far.
- **Map:** The visualization of a run. The map shows all the locations and paths in a
  run.
- **Location:** A location on the map that can be visited.
- **Path:** The path from one location to another.
- **Rung:** A location's distance from the start location. The start location has rung 0.
- **Fight:** A location type and the main interaction of the game.
- **Hamster Card:** A special card that can be used to bring other cards into play.
  Hamster cards are not part of the main deck, but are part of the hamster deck.
- **Hamster Deck:** A special deck that only contains hamster cards. Will be generated
  at the start and scrapped at the end of a fight.
- **Grid:** Where cards are placed during a fight. No grid outside of fights.
- **Gems:** Are created when the human player inflicts surplus damage on the computer
  player. Can be used in certain locations (maybe to buy cards, skills, or items?).
- **Agent:** The human player or computer player.
  - FIXME Is there still a need for the term agent? Check all occurences.
  - FIXME Maybe just player and computer? (Currently, it's mostly human vs computer)
- **Opponent:** In a fight, the opposing card to a card.
- **Damage:** The damage an agent has suffered. An agent loses 1 life when the damage
  reaches a certain threshold.
- **Lives:** An agent has a certain amount of lives. When all lives are lost, the agent
  is defeated (the run ends, if it is the human player).
- **Computer Strategy:** The strategy the computer player uses in a fight.
- **Item:** Some buff that can be used in a fight. (Currently not implemented.)

# Card "buckets"

There are the following broad "buckets" of cards:

1. All that conceptually exist. New cards (e.g., via lottery or similar) will typically
   be selected from this bucket.
   - This is the only bucket where the philosophies I vs II make any difference.
2. The ones the player owns.
3. The ones a player actually starts a run with.
   - Maybe she can choose? Based on a number of points (and maybe also gems and
     spirits)? (But at least one?) 
4. (The ones in different decks during a fight.)

## Example run

- I start the run with: ["Church Mouse", "Weasel", "Lynx", "Porcupine"]
- I visit a location that gives me a new card: Bison/3/5/TRAMPLE
  - Phil I: This card was selected from bucket 1.
  - Phil II: This card was randomly generated.
- I visit a location and boost my Porcupine to Porcupine/1/8/AIRDEFENSE
- I visit a location and lose my Weasel.
- I have a fight, which doesn't change my cards.
- I lose the fight, the run ends.
- Now, I have the following cards: ["Church Mouse", "Lynx", "Porcupine*", "Bison"]
- I can start the next run with a subset of these.


# Philosophy I: All cards pre-generated

- The game does not generate new cards dynamically. I.e., all cards are known (to the
  game at least, maybe not to the player) at the start of the game.


# Philosophy II: All cards randomly generated

- Locations, where the player can get a card, randomly generate cards.
- Computer strategy randomly generates cards.
- Need some way to generate the cards (including names) and especially a way to derive a
  score from a card, which should hint at the cards overall strength.
  - Such a score would require the skills to have a score as well.
- (Such a generator would make sense anyway to generate card proposals for Philosophy
  I.)

Details:

- Options on how to get the name a) live from ChatGPT, b) fully random from a
  pre-generated list, c) from a pre-generated list that is categorized by strength
  score.
- Maybe make sure that cards with the same attribute always get the same name?


# Philosophy III: Hybrid

- Cards are usually taken from a pre-generated list.
- But with a certain probability, a card is generated randomly.


# Philosophy IV: Options

- Maybe the player can choose between the philosophies at the start of a game (but not
  at the start of a run)?



# Possible score function

``` python
def calculate_strength_score(card) -> int:
    """
    Calculates the overall strength score of a card based on its initial power, initial health,
    skills, and the total costs of fire and spirits required to play and sacrifice the card.
    
    QQ: Can the score be normalized to [0, 1]? It might be possible for a certain version of the game, if all skills and their scores are known and if the max numbers for power, health, and costs are known.
    """
    # Calculate the total costs of fire and spirits required to play and sacrifice the card
    total_costs = card.costs_fire + card.costs_spirits
    
    # Calculate the overall strength score of the card
    strength_score = card.initial_power * 2 + card.initial_health * 3 - total_costs
    
    # Modify the strength score based on the skills of the card
    if card.skills:
        for skill in card.skills:
            if skill == TRAMPLE:
                strength_score += 2
            elif skill == LIFEDRAIN:
                strength_score += 1
            # Add more conditions for other skills as needed
            
    # Return the strength score
    return strength_score
```


