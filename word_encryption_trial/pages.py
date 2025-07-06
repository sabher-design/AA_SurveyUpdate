from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Task(Page):
    def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False

    timeout_seconds = Constants.timeout_seconds
    form_model = 'player'
    form_fields = ['solved_trial', 'notSolved_trial']


class Results(Page):
    def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False


page_sequence = [Task,Results]
