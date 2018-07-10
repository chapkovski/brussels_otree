from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range

from .models import Constants, Player


class Intro(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        ...


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class AfterContribWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()







class Results(Page):
    """Players payoff: How much each has earned in this round"""

    def vars_for_template(self):
        return {'highcharts_series': [self.group.get_chart_series(), self.player.get_chart_series()],
                'total_earnings': Constants.efficiency_factor * self.group.total_contribution,
                }



class FinalResults(Page):
    """Players payoff: How much each has earned in EACH round"""

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds


# from customwp.views import StartWP
page_sequence = [
    Intro,
    Contribute,
    AfterContribWP,
    Results,
    FinalResults,
]
