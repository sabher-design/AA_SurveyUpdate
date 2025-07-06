from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class p0_prolificID(Page):
    form_model = 'player'
    form_fields = ['ProlificID']
    
class p1p2_TP(Page):
    pass

class p3p4_TP(Page):
     pass


page_sequence = [p0_prolificID, p1p2_TP, p3p4_TP]
