from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
Dictator game with the possibility of gender treatment.
In gender treatment the Dictators receive an information about the gender of Receivers.
"""


class Constants(BaseConstants):
    # ==============
    # oTree constants
    name_in_url = 'dg_gender'
    players_per_group = 2
    num_rounds = 1
    # ==============
    # game constants
    endowment = c(100)


class Subsession(BaseSubsession):
    treatment = models.StringField()
    def creating_session(self):
        if self.session.config.get('treatment_gender'):
            self.treatment = 'gender'
        else:
            self.treatment = 'baseline'

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
    # we would like to show to a Dictator (in some treatments) the gender of a Receiver
    # To test if gender affects the amount of donation
    gender = models.IntegerField(choices=
                                 ((0, 'Female'),
                                  (1, 'Male')),
                                 widget=widgets.RadioSelectHorizontal,
                                 label='What is your gender?'
                                 )

    def role(self):
        # the first player receives a role of dictator, and the second one becomes a receiver
        if self.id_in_group == 1:
            return 'dictator'
        else:
            return 'receiver'
