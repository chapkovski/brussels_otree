from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    # after a player reads the instructions we need to generate the number they will guess
    # EXERCISE:
    # Exercise 1: move the random number generation within a player's model
    # Exercise 2: generate the number before the game starts (in Subsession)
    def before_next_page(self):
        toguess = random.randint(Constants.minguess, Constants.maxguess)
        self.player.toguess = toguess


class Decision(Page):
    form_model = 'player'
    form_fields = ['guess']

    def before_next_page(self):
        diff = abs(self.player.guess - self.player.toguess)
        self.player.payoff = Constants.endowment - diff


class Results(Page):
    ...


page_sequence = [

    Intro,
    Decision,
    Results,
]
