from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class p9a(Page):
      pass
        

class Task_round1(Page):
     timeout_seconds = Constants.timeout_seconds
     form_model = 'player'
     form_fields = ['solved_round1', 'notSolved_round1'] 
     

class p10a_interim(Page):
     pass
        
page_sequence = [p9a, Task_round1, p10a_interim]
