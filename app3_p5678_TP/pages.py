from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
       
class p5_TP_Blue(Page):
      def is_displayed(self):
        if self.player.color == 'Blue':
             return True
        else:
             return False

class p5_TP_Green(Page):
     def is_displayed(self):
        if self.player.color == 'Green':
             return True
        else:
             return False

    
class p6a(Page):
      pass

class p6b1(Page):
     form_model = 'player'
     form_fields = ['ctrq1_1','ctrq1_2']

class p6b2_1(Page):
     def is_displayed(self):
        if self.player.ctrq1_1== '3 and 6' and self.player.ctrq1_2 == '3 and 6':
             return True
        else:
             return False

class p6b2_2(Page):
    def is_displayed(self):
        if self.player.ctrq1_1 == '3 and 6' and self.player.ctrq1_2 != '3 and 6':
             return True
        else:
             return False

class p6b2_3(Page):
    def is_displayed(self):
        if self.player.ctrq1_1 != '3 and 6' and self.player.ctrq1_2 == '3 and 6':
             return True
        else:
             return False
class p6b2_4(Page):
    def is_displayed(self):
        if self.player.ctrq1_1 != '3 and 6' and self.player.ctrq1_2 != '3 and 6':
             return True
        else:
             return False

class p6b3(Page):
     form_model = 'player'
     form_fields = ['ctrq2_1','ctrq2_2']

class p6b4_1(Page):
     def is_displayed(self):
        if self.player.ctrq2_1 == '5 and 6' and self.player.ctrq2_2 == '1 and 6':
             return True
        else:
             return False

class p6b4_2(Page):
    def is_displayed(self):
        if self.player.ctrq2_1 == '5 and 6' and self.player.ctrq2_2 != '1 and 6':
             return True
        else:
             return False

class p6b4_3(Page):
    def is_displayed(self):
        if self.player.ctrq2_1 != '5 and 6' and self.player.ctrq2_2 == '1 and 6':
             return True
        else:
             return False
class p6b4_4(Page):
    def is_displayed(self):
        if self.player.ctrq2_1 != '5 and 6' and self.player.ctrq2_2 != '1 and 6':
             return True
        else:
             return False

class p8(Page):
     form_model = 'player'
     form_fields = ['belief1_tp', 'belief2_tp', 'belief3_tp','attention_check2']

     
class attention_check1(Page):
    form_model = 'player'
    form_fields = ['attention_check1']

class attention_check2(Page):
    form_model = 'player'
    form_fields = ['attention_check2']


page_sequence = [p5_TP_Blue, p5_TP_Green, p6a, attention_check1, 
p6b1, p6b2_1, p6b2_2, p6b2_3, p6b2_4, p6b3, p6b4_1, p6b4_2, p6b4_3, p6b4_4, p8]
