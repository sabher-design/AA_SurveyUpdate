from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class p9a(Page):
     def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False

class Task_ct(Page):
     timeout_seconds = Constants.timeout_seconds
     form_model = 'player'
     form_fields = ['solved', 'notSolved'] 
     def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False

class p10_results(Page):
     def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False


page_sequence = [p9a, Task_ct, p10_results]
