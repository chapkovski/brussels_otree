from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    # Base constants of oTree
    name_in_url = 'myotreeapp'
    players_per_group = 2
    num_rounds = 1
    # Any custom parameters:
    endowment = 100


import random


class Subsession(BaseSubsession):
    def creating_session(self):
        for g in self.get_groups():
            g.total_investment = random.randint(0, 100)
        for p in self.get_players():
            p.contribution = random.randint(0, 10)


class Group(BaseGroup):
    total_investment = models.IntegerField(initial=100)


class Player(BasePlayer):
    contribution = models.IntegerField(initial=10)
    def role(self):
        self.id_in_subsession