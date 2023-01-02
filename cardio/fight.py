from typing import Optional, List
from enum import Enum, auto
import logging
from . import session, Deck, CardList
from .card_blueprints import create_cards_from_blueprints
from .agent_strategies import AgentStrategy, HumanAgentStrategy

# FIXME Should get to a point where session is no longer needed in this module.

# FIXME Fight humanstrategy could be a different kind/subclass of fight instead of a
# strategy.
# FIXME And computerstrategy could be a callback or something.


class FightStatus(Enum):
    """
    INITIALIZED -> play_computer_cards -> HUMAN_DRAWING -> human_draws ->
    HUMAN_PLAYING -> [play card, use item, ..., end_turn] -> HUMAN_DONE -> fight ->
    [OVER | play_computer_cards] ...

    HUMAN_DRAWING
    HUMAN_PLAYING: pick card to play | open item menu | end turn
        HUMAN_PICKINGITEM: activate item | back
        HUMAN_PLACINGCARD: error message bc card not playable | pick card to sacrifice
                        | pick slot to play | back
    HUMAN_DONE
    """

    # FIXME This is a mix of fight-related vs UI-related states. Maybe rethink?

    # FIXME Try to push as many status changes to the class as possible?

    # FIXME Try to add more asserts to the class?

    INITIALIZED = auto()
    HUMAN_DRAWING = auto()
    HUMAN_PLAYING = auto()
    HUMAN_PICKINGITEM = auto()
    HUMAN_PLACINGCARD = auto()
    HUMAN_DONE = auto()
    OVER = auto()


class WhoWon(Enum):
    STILLFIGHTING = auto()
    HUMAN = auto()
    COMPUTER = auto()


class Fight:
    def __init__(
        self, grid, computeragent, humanagent, computerstrategy, humanstrategy=None
    ):
        self.grid = grid
        self.computeragent = computeragent
        self.humanagent = humanagent
        self.computerstrategy = computerstrategy
        self.humanstrategy = humanstrategy
        self.fighting = True  # FIXME Unnecessary?
        self.turn_number = 0
        # FIXME humancards set to session.humanagent.deck.cards
        # --- Prepare the decks ---
        # When a fight happens, 4 decks get created:
        # - fightdeck: copy of maindeck
        # - handdeck: the current hand, initially with 3(?) cards from the fight deck and 1
        #   card from the hamster deck
        # - hamsterdeck: with all the helper cards
        # - useddeck: with all the dead (or discarded?) cards (except cards from the
        #   hamsterdeck)
        self.fightdeck = Deck()
        self.fightdeck.cards = session.humanagent.deck.cards
        self.fightdeck.shuffle()
        self.hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
        self.handdeck = Deck(self.fightdeck.draw_cards(3))
        self.handdeck.add_card(self.hamsterdeck.draw_card())
        self.useddeck = Deck()
        self.status: FightStatus = FightStatus.INITIALIZED
        self.who_won: WhoWon = WhoWon.STILLFIGHTING

    def log_decks(self):
        """Assumes decks to be passed in order of Hand, Fight, Hamster, Used."""
        for deck, name in zip(
            [self.handdeck, self.fightdeck, self.hamsterdeck, self.useddeck],
            ["Hand", "Fight", "Hamster", "Used"],
        ):
            logging.debug(
                "%sdeck size: %s (%s)",
                name,
                len(deck.cards),
                ",".join([c.name for c in deck.cards]),
            )

    def end_fight(self):
        assert self.fighting == False
        session.humanagent.deck.cards = [
            c
            for c in self.useddeck.cards + self.handdeck.cards + self.fightdeck.cards
            if c.name != "Hamster"
        ]
        session.humanagent.deck.reset_cards()

    def play_computer_cards(self):
        # Computer plays cards:
        # (This can include more "world-style" cards such as trees or boulders etc.)
        # FIXME Simple callback?
        #
        # FIXME Assert some status here? But maybe not as below...
        #  assert self.status in (FightStatus.INITIALIZED, FightStatus.HUMAN_DRAWING)
        self.computerstrategy.play_cards(session.grid, self.turn_number)

    def handle_round_of_fight(self):
        assert self.status == FightStatus.HUMAN_DONE
        self.log_decks()

        # Activate all cards:
        self.grid.activate_line(2)
        self.grid.activate_line(1)
        self.grid.prepare_line()

        if self.humanagent.has_lost_life():
            self.humanagent.update_lives_and_health_after_death()
            # session.view.computer_wins_fight()
            self.status = FightStatus.OVER
            self.who_won = WhoWon.COMPUTER
        if self.computeragent.has_lost_life():
            overflow = self.computeragent.update_lives_and_health_after_death()
            # session.view.human_wins_fight()

            # FIXME Do something w overflow damage here -- maybe just store it in the
            # object right in the update_lives_and_health_after_death function but also
            # pass it to the view for some animation? -- Just store it in self?
            self.status = FightStatus.OVER
            self.who_won = WhoWon.HUMAN
        if session.grid.is_empty():
            # FIXME ^ should be `is_powerless` instead of `is_empty`
            # FIXME What should happen here when the grid is "powerless", i.e., no cards
            # with >0 power?
            pass

        self.turn_number += 1

        if self.status != FightStatus.OVER:
            self.play_computer_cards()
            self.status = FightStatus.HUMAN_DRAWING

    # --- Clean up after fight ---

    def handle_turn_BEING_DISMANTLED(self):
        assert self.fighting == True  # FIXME Remove
        self.log_decks()

        # ??????????
        # FIXME Do we need to split this into even smaller piecees????
        # ??????????

        # Human plays card(s):
        if self.humanstrategy is not None:
            self.humanstrategy.add_decks(
                self.fightdeck, self.hamsterdeck, self.handdeck, self.useddeck
            )
            whichdeck = self.humanstrategy.deck_to_draw_from(self.turn_number)
            if not whichdeck.is_empty():
                card = whichdeck.draw_card()
                self.handdeck.add_card(card)
                logging.debug("Human draws %s", card.name)
            # FIXME View needs to update with new card moving to handdeck
            posandcard = self.humanstrategy.card_to_play_from_hand(self.turn_number)
            if posandcard is not None:
                pos, card = posandcard
                session.grid[pos.line][pos.slot] = card
                self.useddeck.add_card(card)
                logging.debug("Human plays %s on %s", card.name, pos)
            else:
                logging.debug("Human plays no card.")
        else:
            pass  # This is the interactive part we have in the tui module now.
