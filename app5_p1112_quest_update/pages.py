from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
import json

def creating_session(subsession):
    for p in subsession.get_players():
        groups = ['women', 'minorities', 'disabilities']
        p.aa_order_groups = json.dumps(random.sample(groups, k=3))

class p0_prolificID(Page):
    form_model = 'player'
    form_fields = ['ProlificID']

class p1_intro(Page):
    form_model = 'player'

class AAFavorPage(Page):
    form_model = 'player'

    def get_form_fields(self):
        if not self.player.aa_order_groups:
            return ['aa_favor_women', 'aa_favor_minorities', 'aa_favor_disabilities']
        groups = json.loads(self.player.aa_order_groups)
        return [f'aa_favor_{g}' for g in groups]


class AADisadvantagePage(Page):
    form_model = 'player'

    def get_form_fields(self):
        if not self.player.aa_order_groups:
            return ['aa_favor_women', 'aa_favor_minorities', 'aa_favor_disabilities']
        groups = json.loads(self.player.aa_order_groups)
        return [f'aa_belief_disadvantage_{g}' for g in groups]


class AAEffortPage(Page):
    form_model = 'player'

    def get_form_fields(self):
        if not self.player.aa_order_groups:
            return ['aa_favor_women', 'aa_favor_minorities', 'aa_favor_disabilities']
        groups = json.loads(self.player.aa_order_groups)
        return [f'aa_belief_effort_{g}' for g in groups]


class AASkillsPage(Page):
    form_model = 'player'

    def get_form_fields(self):
        if not self.player.aa_order_groups:
            return ['aa_favor_women', 'aa_favor_minorities', 'aa_favor_disabilities']
        groups = json.loads(self.player.aa_order_groups)
        return [f'aa_belief_skills_{g}' for g in groups]


class AAFairnessPage(Page):
    form_model = 'player'

    def get_form_fields(self):
        if not self.player.aa_order_groups:
            return ['aa_favor_women', 'aa_favor_minorities', 'aa_favor_disabilities']
        groups = json.loads(self.player.aa_order_groups)
        return [f'aa_belief_fairness_{g}' for g in groups]


class q11_efficiency_loss(Page):
    form_model = 'player'

    def get_form_fields(self):
        if not self.player.aa_order_groups:
            return ['aa_favor_women', 'aa_favor_minorities', 'aa_favor_disabilities']
        groups = json.loads(self.player.aa_order_groups)
        return [f'efficiency_loss_{g}' for g in groups]


#class p10_Intro_survey_update(Page):
 #   pass


#Questionnaires

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


class q6_efficiencypref_update(Page):
    form_model = 'player'
    form_fields = ['token_1', 'token_2']

class q8_1overconfidence_quiz(Page):
    pass

class q8_2overconfidence_quiz(Page):
    timeout_seconds = 120
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'quiz7','quiz8', 'quiz9', 'quiz10']

class q8_overconfidence(Page):
    form_model = 'player'
    form_fields = ['your_rank']

class attention_check1(Page):
    form_model = 'player'
    form_fields = ['attention_check1']

class attention_check3(Page):
    form_model = 'player'
    form_fields = ['attention_check3']

class q9_disability_status(Page):
    form_model = 'player'
    form_fields = ['deaf', 'blind', 'concentration', 'walking', 'dressing', 'errands']

class q10_AA(Page):
    form_model = 'player'
    form_fields = ['AA_affected', 'AA_affected_yes', 'AA_benefited', 'AA_context']

    def error_message(self, values):
        if values['AA_affected'] == 'Yes' and not values['AA_affected_yes']:
            return 'Please describe the context/kind if you answered "Yes".'
        if values['AA_affected'] == 'Yes' and not values['AA_benefited']:
            return 'Please indicate whether you have ever benefited from affirmative action in your life.'
        if values['AA_benefited'] == 'Yes, I believe I have rather benefited' and not values['AA_context']:
            return 'Please describe the context/kind.'
        if values['AA_benefited'] == 'No, I believe I have rather been harmed' and not values['AA_context']:
            return 'Please describe the context/kind.'

class goodbye(Page):
    pass

page_sequence = [p0_prolificID, p1_intro, AAFavorPage, AADisadvantagePage, AAEffortPage, AASkillsPage, AAFairnessPage, q11_efficiency_loss, q1_risk, q2_socialpref,
q3_demographics, attention_check3, q4_politic, q5_discrimination, q6_efficiencypref_update,
q8_1overconfidence_quiz, q8_2overconfidence_quiz, q8_overconfidence, attention_check1, q9_disability_status, q10_AA, goodbye]


