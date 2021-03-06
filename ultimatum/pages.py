from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants


class Introduction(Page):
    ...


class Offer(Page):
    form_model = 'group'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.role() == 'proposer'



class WaitForProposer(WaitPage):
    pass


class Accept(Page):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.role() == 'responder'



class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [Introduction,
                 Offer,
                 WaitForProposer,
                 Accept,
                 ResultsWaitPage,
                 Results]
