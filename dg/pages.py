from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    form_model = 'player'
    form_fields = ['gender']


class Decision(Page):
    # we need to get player's desion about the number on this page, that's why we pass the model there (player)
    # and the field for getting their input
    form_model = 'group'
    form_fields = ['dg_decision']
    def vars_for_template(self):
        receiver = self.group.get_player_by_role('receiver')

        return {'gender': receiver.get_gender_display()}
    def is_displayed(self):

        return self.player.role() == 'dictator'


class BeforeResultsWP(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        companies = ['Apple', 'Microsoft', 'Google', 'Facebook']
        return {'companies': companies}



page_sequence = [
    Intro,
    WaitPage,
    Decision,
    BeforeResultsWP,
    Results,
]
