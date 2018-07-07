from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range

from .models import Constants, Player


class Intro(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        base_points = 1  # / self.session.config['real_world_currency_per_point']
        lb = Constants.endowment * Constants.num_rounds
        ub = Constants.endowment * Constants.efficiency_factor * Constants.num_rounds
        lb = round(lb / base_points + \
                   self.session.config['participation_fee'])
        ub = round(ub / base_points + \
                   self.session.config['participation_fee'])
        return ({'partfee': self.session.config['participation_fee'],
                 'base_points': base_points,
                 'lb': lb,
                 'ub': ub
                 })


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class AfterContribWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """Players payoff: How much each has earned in this round"""

    def vars_for_template(self):
        partfee = self.session.config['participation_fee']
        bonus_in_currency = \
            self.player.participant.payoff.to_real_world_currency(self.session)
        total_currency_payoff = \
            self.player.participant.payoff_plus_participation_fee()
        return ({'total_earnings': round(self.group.total_contribution * Constants.efficiency_factor),
                 'real_currency_payoff': self.player.payoff.to_real_world_currency(self.session),
                 })


class FinalResults(Page):
    timeout_seconds = 120
    """Players payoff: How much each has earned in EACH round"""

    def extra_is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        partfee = self.session.config['participation_fee']
        bonus_in_currency = \
            self.player.participant.payoff.to_real_world_currency(self.session)
        total_currency_payoff = \
            self.player.participant.payoff_plus_participation_fee()
        return ({'partfee': partfee,
                 'bonus_in_currency': bonus_in_currency,
                 'total_currency_payoff': total_currency_payoff,
                 })


# from customwp.views import StartWP
page_sequence = [
    Intro,
    Contribute,
    AfterContribWP,
    Results,
    FinalResults,
]
