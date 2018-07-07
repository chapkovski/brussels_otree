from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""

import random
class Constants(BaseConstants):
    name_in_url = 'political'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.endowment = random.randint(0,100)
            p.radical = random.choice([True, False])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    endowment = models.IntegerField()
    personal_A = models.BooleanField()
    personal_B = models.BooleanField()

    party = models.StringField(widget=widgets.RadioSelectHorizontal)
    polit_views = models.IntegerField(choices=list(range(11)),
                                      widget=widgets.RadioSelectHorizontal)
