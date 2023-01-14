import os
from abc import ABC, abstractmethod
from typing import Literal
from . import session, Card, Deck, Grid, GridPos
from .agent_strategies import AgentStrategy
from .card_blueprints import create_cards_from_blueprints
from .tui.decks import Decks  # FIXME tui should not be known here

# FIXME This is not nice: On one hand, the view has a link to the model as an attribute.
# On the other, it accesses the session directly. Use only one of these mechanisms!

# FIXME Rename draw methods to show (except where card drawing is meant)?


class FightViewAndController(ABC):
    """
    - All the `card_` methods should be able to rely on the precondition that the `card`
      is still in the grid when the method is called.
    """

    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        # FIXME Should we also set the computerstrategy here?
        # FIXME We _do_ have the grid! 1) Use it! 2) Do we really have it when we look
        # at how the view is created?

    # --- Called by Card class ---

    def card_about_to_die(self, card: Card) -> None:
        pass

    def card_lost_health(self, card: Card) -> None:
        pass

    def card_getting_attacked(self, target: Card, attacker: Card) -> None:
        pass

    def card_activate(self, card: Card) -> None:
        pass

    def card_prepare(self, card: Card) -> None:
        pass

    def pos_card_deactivate(self, pos: GridPos) -> None:
        pass

    # --- Controller-related ---

    def draw_empty_grid(self, grid_width: int) -> None:
        pass

    def draw_drawdecks(self, drawdeck: Deck, hamsterdeck: Deck) -> None:
        pass

    def draw_card_to_handdeck(
        self, handdeck: Deck, card: Card, whichdeck: Literal["draw", "hamster"]
    ) -> None:
        pass

    def draw_computer_plays_card(self, card: Card, to: GridPos) -> None:
        """Play a computer card to `to`, which can be in line 0 or 1."""
        pass

    def draw_human_places_card(self, card: Card, from_slot: int, to_slot: int) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        pass

    def handle_human_draws_new_card(self) -> None:
        # FIXME Does this rely on the class having more attributes such as decks? Which
        # should be set in init?
        pass

    def handle_human_plays_card(self) -> None:
        pass

    # --- Misc ---

    def update(self) -> None:
        # FIXME Is this still necessary? Still used anywhere?
        pass

    # --- Controller ---

    def _safe_draw_card_to_deck(
        self, draw_from: Deck, from_name: Literal["draw", "hamster"]
    ) -> None:
        """Safe way to draw a card from a deck that doesn't break when the deck is
        empty. Important for tests.
        """
        try:
            card = draw_from.draw_card()
        except IndexError:
            return
        self.draw_card_to_handdeck(self.decks.handdeck, card, from_name)
        self.decks.handdeck.add_card(card)

    def handle_round_of_fight(self) -> bool:
        self.decks.log()

        # Play computer cards and animate how they appear:
        for pos, card in self.computerstrategy.cards_to_be_played(
            session.grid, self.round_num
        ):
            self.draw_computer_plays_card(card, pos)
        # Now also place them in the model:
        self.computerstrategy.play_cards(session.grid, self.round_num)

        # Let human draw a card:
        self.handle_human_draws_new_card()

        # Let human play card(s) from handdeck or items in his collection:
        self.handle_human_plays_card()

        self.decks.log()
        session.grid.log()

        # Activate all cards:
        session.grid.activate_line(2)
        session.grid.activate_line(1)
        session.grid.prepare_line()

        # FIXME Still some things missing below:
        if session.humanagent.has_lost_life():
            session.humanagent.update_lives_and_health_after_death()
            self.computer_wins_fight()
            return False
        if session.computeragent.has_lost_life():
            overflow = session.computeragent.update_lives_and_health_after_death()
            self.human_wins_fight()
            # FIXME Do something w overflow damage here -- maybe just store it in the
            # object right in the update_lives_and_health_after_death function but also
            # pass it to the view for some animation?
            return False
        if session.grid.is_empty():
            # QQ: Should this also break when the grid is "powerless", i.e., no cards
            # with >0 power?
            return False

        session.grid.log()
        return True

    def handle_fight(self, computerstrategy: AgentStrategy) -> None:
        self.computerstrategy = computerstrategy
        # ^ FIXME Should this be in __init__? And/or the entire ComputerAgent object,
        # which could contain the computerstrategy? It will be used for one fight only
        # anyway...
        self.draw_empty_grid(4)  # FIXME Parametrize grid with somehow

        # Set up the 4 decks for the fight:
        drawdeck = Deck()
        drawdeck.cards = session.humanagent.deck.cards
        drawdeck.shuffle()
        hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
        self.decks = Decks(drawdeck, hamsterdeck, Deck(), Deck())

        # Draw the decks and show how the first cards get drawn:
        self.draw_drawdecks(self.decks.drawdeck, self.decks.hamsterdeck)
        for _ in range(3):
            self._safe_draw_card_to_deck(self.decks.drawdeck, "draw")
        self._safe_draw_card_to_deck(self.decks.hamsterdeck, "hamster")
        # Redraw because size of decks changed:
        self.draw_drawdecks(self.decks.drawdeck, self.decks.hamsterdeck)

        # Run the fight:
        fighting = True
        self.round_num = 0
        while fighting:
            fighting = self.handle_round_of_fight()
            self.round_num += 1

        # Reset human deck after the fight:
        session.humanagent.deck.cards = [
            c
            for c in self.decks.useddeck.cards
            + self.decks.handdeck.cards
            + self.decks.drawdeck.cards
            if c.name != "Hamster"
        ]
        session.humanagent.deck.reset_cards()


class SimpleView(FightViewAndController):
    frames: dict = {}
    msg: str = ""
    non_blocking: bool = False

    def update(self) -> None:
        repr = ""
        for i, line in enumerate(self.grid):
            repr += f"{i}   "
            for sloti, slot in enumerate(line):
                frame = self.frames.get(f"{i}:{sloti}", "[]")
                slotstr = ""
                if slot is not None:
                    slotstr = f"{slot.name[0:6]}|{slot.power}|{slot.health}"
                    skillstr = "".join(s.value.symbol for s in slot.skills)
                    slotstr = slotstr + skillstr
                repr += f"{frame[0]}{slotstr:13s}{frame[1]}"
            repr += "\n"
        print(repr)

        print(
            f"\nYour health: {session.humanagent.health} | His health: {session.computeragent.health}"
        )

        print(
            f"\nYour lives: {session.humanagent.lives} | His lives: {session.computeragent.lives}"
        )

        if self.msg != "":
            print(f"\n{self.msg}")

        print()
        if not self.non_blocking:
            input()
        os.system("cls")

        self.frames = {}
        self.msg = ""

    def card_activate(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, (
            f"{card.name} gets gets activated and "
            "needs a view update but has no position on the grid"
        )
        self.frames[f"{pos.line}:{pos.slot}"] = "**"
        self.update()

    def card_getting_attacked(self, target: Card, attacker: Card) -> None:
        pos = self.grid.find_card(target)
        assert pos is not None, (
            f"{target.name} gets attacked by {attacker.name} and "
            "needs a view update but has no position on the grid"
        )
        self.frames[f"{pos.line}:{pos.slot}"] = "><"
        self.update()

    def human_wins_fight(self) -> None:
        # FIXME Still necessary?
        self.msg = "You won!"

    def computer_wins_fight(self) -> None:
        # FIXME Still necessary?
        # QQ: Boss fights will work differently.
        self.msg = "You lost!"
