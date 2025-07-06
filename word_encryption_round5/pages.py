from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class p9a(Page):
      pass      

class Task_round5(Page):
     timeout_seconds = Constants.timeout_seconds
     form_model = 'player'
     form_fields = ['solved_round5', 'notSolved_round5'] 
     

class p10a_interim(Page):
     pass
        
page_sequence = [Task_round5, p10a_interim]
