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
    offer_increment = c(10)

    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)
    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    amount_offered = models.CurrencyField(choices=Constants.offer_choices)

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted",
        widget=widgets.RadioSelectHorizontal,
    )

    def set_payoffs(self):
        sender = self.get_player_by_role('sender')
        receiver = self.get_player_by_role('receiver')
        if self.offer_accepted:
            sender.payoff = Constants.endowment - self.amount_offered
            receiver.payoff = self.amount_offered
        else:
            sender.payoff = Constants.payoff_if_rejected
            receiver.payoff = Constants.payoff_if_rejected


class Player(BasePlayer):
    def role(self):
        # the first player receives a role of sender, and the second one becomes a receiver
        if self.id_in_group == 1:
            return 'sender'
        else:
            return 'receiver'
