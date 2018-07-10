from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """

"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 2
    num_rounds = 1
    instructions_template = 'ultimatum/Instructions.html'
    endowment = c(100)
    payoff_if_rejected = c(0)


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    amount_offered = models.CurrencyField()

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted",
        widget=widgets.RadioSelectHorizontal,
        choices = ((True, 'Accept'), (False, 'Reject'),)
    )

    def set_payoffs(self):
        proposer = self.get_player_by_role('proposer')
        responder = self.get_player_by_role('responder')
        if self.offer_accepted:
            proposer.payoff = Constants.endowment - self.amount_offered
            responder.payoff = Constants.endowment  + self.amount_offered
        else:
            proposer.payoff = Constants.payoff_if_rejected
            responder.payoff = Constants.payoff_if_rejected


class Player(BasePlayer):
    def role(self):
        # the first player receives a role of sender, and the second one becomes a receiver
        if self.id_in_group == 1:
            return 'proposer'
        else:
            return 'responder'
