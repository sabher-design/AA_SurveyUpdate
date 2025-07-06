from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class p9a(Page):
      pass

class Task_round6(Page):
     timeout_seconds = Constants.timeout_seconds
     form_model = 'player'
     form_fields = ['solved_round6', 'notSolved_round6'] 
     

class p10b_interim(Page):
     pass
        
page_sequence = [Task_round6, p10b_interim]
