from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants




class p10_SPECnSPECG(Page):
    def is_displayed(self):
        if self.player.treatment == 'SPECG':
             return True
        else:
             return False

# In-group favoritism
class p11_INFO (Page):
    def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False
    form_model = 'player'
    form_fields = ['ingroup1_info', 'ingroup2_info', 'ingroup3_info', 'ingroup4_info']


class p11_SPECG(Page):
    def is_displayed(self):
        if self.player.treatment == 'SPECG':
             return True
        else:
             return False
    form_model = 'player'
    form_fields = ['ingroup1_specs', 'ingroup2_specs', 'ingroup3_specs', 'ingroup4_specs']

# Sending smileys
class p12_INFO_men(Page):
    def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False
    form_model = 'player'
    form_fields = ['smiley1', 'smiley2', 'smiley3', 'smiley4', 'smiley5']


class p12_SPECnSPECG(Page):
    def is_displayed(self):
        if self.player.treatment == 'SPECG':
             return True
        else:
             return False
    form_model = 'player'
    form_fields = ['smiley1', 'smiley2', 'smiley3', 'smiley4', 'smiley5', 'smiley6']


#Questionnaires
class q0_aafavor1(Page):
    form_model = 'player'
    form_fields = ['aa_favor1','aa_favor2','aa_favor3']
    def is_displayed(self):
        if self.player.aa_rand == 'a':
             return True
        else:
             return False

class q0_aafavor2(Page):
    form_model = 'player'
    form_fields = ['aa_favor1','aa_favor3','aa_favor2']
    def is_displayed(self):
        if self.player.aa_rand == 'b':
             return True
        else:
             return False

class q0_aafavor3(Page):
    form_model = 'player'
    form_fields = ['aa_favor3','aa_favor2','aa_favor1']
    def is_displayed(self):
        if self.player.aa_rand == 'c':
             return True
        else:
             return False

class q0_aafavor4(Page):
    form_model = 'player'
    form_fields = ['aa_favor3','aa_favor1','aa_favor2']
    def is_displayed(self):
        if self.player.aa_rand == 'd':
             return True
        else:
             return False

class q0_aafavor5(Page):
    form_model = 'player'
    form_fields = ['aa_favor2','aa_favor3','aa_favor1']
    def is_displayed(self):
        if self.player.aa_rand == 'e':
             return True
        else:
             return False

class q0_aafavor6(Page):
    form_model = 'player'
    form_fields = ['aa_favor2','aa_favor1','aa_favor3']
    def is_displayed(self):
        if self.player.aa_rand == 'f':
             return True
        else:
             return False

class q1_risk(Page):
    form_model = 'player'
    form_fields = ['risk']

class q2_socialpref(Page):
    form_model = 'player'
    form_fields = ['social']


class q3_demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'gender_diverse', 'age', 'employment', 'children', 
    'socialclass','income', 'household_children', 'household_adults', 'ethnicity', 
    'ethnicity_other', 'mother_tongue', 'IQ', 'sexual_orientation', 'sexual_orientation_other']

class q4_politic(Page):
    form_model = 'player'
    form_fields = ['political']

class q5_discrimination(Page):
    form_model = 'player'
    form_fields = ['discrimination']


class q6_efficiencypref(Page):
    form_model = 'player'
    form_fields = ['token_1', 'token_2']

class q7_fairnessAA(Page):
    form_model = 'player'
    form_fields = ['fairness_AA', 'fairness_noAA']

class q8_1overconfidence_quiz(Page):
    pass

class q8_2overconfidence_quiz(Page):
    timeout_seconds = 120
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'quiz7','quiz8', 'quiz9', 'quiz10']

class q8_overconfidence(Page):
    form_model = 'player'
    form_fields = ['your_rank']

class attention_check3(Page):
    form_model = 'player'
    form_fields = ['attention_check3']


class goodbye(Page):
    pass

page_sequence = [p10_SPECnSPECG, p11_INFO, p11_SPECG, p12_INFO_men, p12_SPECnSPECG,
q0_aafavor1, q0_aafavor2, q0_aafavor3, q0_aafavor4, q0_aafavor5, q0_aafavor6, q1_risk, q2_socialpref, 
q3_demographics, attention_check3, q4_politic, q5_discrimination, q6_efficiencypref, q7_fairnessAA, 
q8_1overconfidence_quiz, q8_2overconfidence_quiz, q8_overconfidence, goodbye]

#page_sequence = [attention_check3, q6_efficiencypref]
