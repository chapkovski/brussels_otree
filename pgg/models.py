from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
public good game 
"""


class Constants(BaseConstants):
    name_in_url = 'pgg'
    players_per_group = 3
    num_others_per_group = players_per_group - 1
    num_rounds = 10
    instructions_template = 'pgg/Instructions.html'
    endowment = c(100)
    efficiency_factor = 2


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    total_contribution = models.IntegerField()
    average_contribution = models.FloatField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.average_contribution = round(self.total_contribution / Constants.players_per_group, 2)
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            p.payoff = sum([+ Constants.endowment,
                            - p.contribution,
                            + self.individual_share,
                            ])

    def get_chart_series(self):
        groupaverages = [[p.round_number, p.average_contribution, ] for p in self.in_all_rounds()]

        return {
            'name': 'Your group average',
            'type': 'line',
            'data': groupaverages}


class Player(BasePlayer):
    contribution = models.IntegerField(
        min=0,
        max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )

    def get_chart_series(self):
        contributions = [[p.round_number, p.contribution, ] for p in self.in_all_rounds()]
        return {'name': 'Your contributions',
                'type': 'line',
                'data': contributions,
                'marker': {
                    'radius': 5,
                }}
