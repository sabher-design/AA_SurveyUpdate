from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class p0_prolificID(Page):
    form_model = 'player'
    form_fields = ['ProlificID']

class p1p2_INFO(Page):
    def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False

class p1p2_SPECnSPECG(Page):
    def is_displayed(self):
        if self.player.treatment == 'SPECG':
             return True
        else:
             return False

class p3p4_INFO(Page):
     def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False

   
class p3p4_SPECnSPECG(Page):
    def is_displayed(self):
        if self.player.treatment == 'SPECG':
             return True
        else:
             return False


page_sequence = [p0_prolificID, p1p2_INFO, p1p2_SPECnSPECG, p3p4_INFO, p3p4_SPECnSPECG]
