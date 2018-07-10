from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    ...


class Decision(Page):
    form_model = 'player'
    form_fields = ['guess']

    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):
    ...


page_sequence = [
    Intro,
    Decision,
    Results,
]
