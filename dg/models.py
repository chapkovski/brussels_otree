from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
Dictator game
"""


class Constants(BaseConstants):
    # ==============
    # oTree constants
    name_in_url = 'dg'
    players_per_group = 2
    num_rounds = 1
    # ==============
    # game constants
    endowment = c(100)


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    # we store the dictator's decision on group level because it is valid for both players in group
    dg_decision = models.CurrencyField(min=0,
                                       max=Constants.endowment,
                                       label='How much money you would like to give to a receiver?',
                                       doc="dictator's decision")

    def set_payoffs(self):
        dictator = self.get_player_by_role('dictator')
        receiver = self.get_player_by_role('receiver')
        dictator.payoff = Constants.endowment - self.dg_decision
        receiver.payoff = self.dg_decision


class Player(BasePlayer):
    def role(self):
        # the first player receives a role of dictator, and the second one becomes a receiver
        if self.id_in_group == 1:
            return 'dictator'
        else:
            return 'receiver'
