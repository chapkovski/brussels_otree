from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    ...


class Decision(Page):
    # we need to get player's desion about the number on this page, that's why we pass the model there (player)
    # and the field for getting their input
    form_model = 'group'
    form_fields = ['dg_decision']

    def is_displayed(self):
        return self.player.role() == 'dictator'


class BeforeResultsWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    ...


page_sequence = [
    Intro,
    Decision,
    BeforeResultsWP,
    Results,
]
