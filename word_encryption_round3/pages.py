from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class p9a(Page):
      pass    

class Task_round3(Page):
     timeout_seconds = Constants.timeout_seconds
     form_model = 'player'
     form_fields = ['solved_round3', 'notSolved_round3'] 
     

class p10a_interim(Page):
     pass
        
page_sequence = [Task_round3, p10a_interim]
