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
     ####No separation
        color1 = itertools.cycle(['Green', 'Blue'])
        for p in self.get_players():
            p.treatment = 'TP'
            p.color = next(color1)
        

     ####Separation
      #  treatments = itertools.cycle(['TP_SPEC', 'TP_SPECG'])

     ##   for p in self.get_players():
      #      p.treatment = next(treatments)
            
     #       if p.treatment == 'TP_SPEC':
      #         color1 = itertools.cycle(['Green', 'Blue'])
            
     #       if p.treatment == 'TP_SPECG':
      #         color2 = itertools.cycle(['Green', 'Blue'])


     #   for p in self.get_players():
     #       if p.treatment == 'TP_SPEC':
      #         p.color = next(color1)
            
      #      if p.treatment == 'TP_SPECG':
      #         p.color = next(color2)

            # Save to participant vars
            p.participant.vars['treatment'] = p.treatment
            p.participant.vars['color'] = p.color
           

class Player(BasePlayer):
    treatment = models.StringField()
    color = models.StringField()

    ProlificID = models.StringField(
    label="Please enter your Prolific ID to start the study.",
    blank = False)


class Group(BaseGroup):
    pass



    