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


author = 'Chi Trieu and Alexandra Stevens'

doc = """
Study on preferences for affirmative action
"""


class Constants(BaseConstants):
    name_in_url = 'app1_p1234_intro'
    players_per_group = None
    num_rounds = 1
    
    

import itertools

class Subsession(BaseSubsession):
    def creating_session(self):
         #Balanced treatment and color assignment
         # Be aware that this function runs for every round! We have 1 round.
    
      ####subgroup assignment: info_green, info_blue, spec_green, spec_blue, spec
      ##### 2/5 INFO, 2/5 SPECG, 1/5 SPEC
       # To run the session for replacement obs (due to dropouts or invalid data), modify the sequence of subgroups accordingly.

        subgroups = itertools.cycle(['INFO_Green','INFO_Blue', 'SPECG_Green', 'SPECG_Blue', 'SPEC'])


        for p in self.get_players():
            p.subgroup = next(subgroups)
         
        for p in self.get_players():
            if p.subgroup == 'INFO_Blue':
               p.treatment= 'INFO'
            if p.subgroup == 'INFO_Green':
               p.treatment= 'INFO'
            if p.subgroup == 'SPECG_Blue':
               p.treatment= 'SPECG'
            if p.subgroup == 'SPECG_Green':
               p.treatment= 'SPECG'
            if p.subgroup == 'SPEC':
               p.treatment= 'SPEC'

            if p.treatment == 'INFO':
               color1 = itertools.cycle(['Green', 'Blue'])
            if p.treatment == 'SPECG':
               color2 = itertools.cycle(['Green', 'Blue'])


        for p in self.get_players():
            if p.treatment == 'INFO':
               p.color = next(color1)
            
            if p.treatment == 'SPECG':
               p.color = next(color2)

            # Save to participant vars
            p.participant.vars['treatment'] = p.treatment
            p.participant.vars['color'] = p.color


        ###1/3 probability for each treatment 
        #treatments = itertools.cycle(['INFO','SPECG','SPEC'])

        #for p in self.get_players():
        #    p.treatment = next(treatments)
            
       #     if p.treatment == 'INFO':
        #      color1 = itertools.cycle(['Green', 'Blue'])
       #     
        #    if p.treatment == 'SPECG':
       #        color2 = itertools.cycle(['Green', 'Blue'])


class Player(BasePlayer):
    subgroup = models.StringField()
    treatment = models.StringField()
    color = models.StringField()

    ProlificID = models.StringField(
        label="Please enter your Prolific ID to start the study.",
        blank = False)




class Group(BaseGroup):
    pass



    