from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def vars_for_template(self):

        series = [{
            'name': 'My earnings',
            'type': 'pie',
            'data': [100, 20, 3, 4.6],
        }
        ]
        return {'series': series}

    def party_choices(self):
        if self.player.radical:
            return ['PAS', 'SVP']
        else:
            return ['BDP', 'EVP']


page_sequence = [
    MyPage,
]
