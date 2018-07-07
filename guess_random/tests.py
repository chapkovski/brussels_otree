from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
# if we want to test how the game reacts on different inputs we need to use random values
import random

class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Intro)
        # we generate a random number in boundaries and submit it
        random_guess=random.randint(Constants.minguess, Constants.maxguess)
        yield (pages.Decision, {'guess': random_guess})
        yield (pages.Results)
