from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
#from otreeutils.surveys import generate_likert_field


author = 'Chi Trieu, Alexandra Stevens and Sabrina Herzog'

doc = """
Study on preferences for affirmative action
"""


class Constants(BaseConstants):
    name_in_url = 'app1_p1234_intro_wm'
    players_per_group = None
    num_rounds = 1
    

import itertools


class Subsession(BaseSubsession):
    def creating_session(self):
         #Balanced treatment and color assignment
         # Be aware that this function runs for every round! We have 1 round.
    
      ####subgroup assignment: info_women, info_men, spec_women, spec_men
      ##### 1/2 INFO, 1/2 SPECG
       # To run the session for replacement obs (due to dropouts or invalid data), modify the sequence of subgroups accordingly.

        subgroups = itertools.cycle(['INFO', 'SPECG'])

        for p in self.get_players():
            p.subgroup = next(subgroups)
         
        for p in self.get_players():
            if p.subgroup == 'INFO':
               p.treatment= 'INFO'
            if p.subgroup == 'SPECG':
               p.treatment= 'SPECG'

            # Save to participant vars
            p.participant.vars['treatment'] = p.treatment


class Player(BasePlayer):
    subgroup = models.StringField()
    treatment = models.StringField()

    ProlificID = models.StringField(
        label="Please enter your Prolific ID to start the study.",
        blank = False)


class Group(BaseGroup):
    pass



    