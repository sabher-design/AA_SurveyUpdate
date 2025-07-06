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
    name_in_url = 'app3_p5678_w'
    players_per_group = None
    num_rounds = 1
    

class Subsession(BaseSubsession):
    # carry on treatment and color assignment from previous apps
    def creating_session(self):
        for p in self.get_players():
            p.treatment = p.participant.vars['treatment']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()

    #Control questions
    ctrq1_1 = models.StringField(
        label= 'Question 1: Assuming that the special rule does not apply, who are the two winners?',
        choices = ['2 and 3', '3 and 6', '4 and 6'],
        widget = widgets.RadioSelect)

    ctrq1_2 = models.StringField(
        label= 'Question 2: Assuming that the special rule applies, who are the two winners?',
        choices = ['2 and 3', '3 and 6', '4 and 6'],
        widget = widgets.RadioSelect)

    ctrq2_1 = models.StringField(
        label= 'Question 3: Assuming that the special rule does not apply, who are the two winners?',
        choices = ['3 and 4', '1 and 6', '5 and 6'],
        widget = widgets.RadioSelect)

    ctrq2_2= models.StringField(
        label= 'Question 4: Assuming that the special rule applies, who are the two winners?',
        choices = ['3 and 4', '1 and 6', '5 and 6'],
        widget = widgets.RadioSelect)

    #AA choice
    aa_choice = models.StringField(
        label= '',
        choices=['Apply the special rule', 'Do not apply the special rule'],
        widget= widgets.RadioSelectHorizontal)
    
    #Beliefs
    belief1_info = models.StringField(
        label= '',
        choices = ['Less likely', 'Equally likely', 'More likely'],
        widget = widgets.RadioSelectHorizontal)

    belief2_info = models.IntegerField(label="")
    belief3_info = models.IntegerField(label="")


    belief1_specs = models.StringField(
        label= '',
        choices = ['Less likely', 'Equally likely', 'More likely'],
        widget = widgets.RadioSelectHorizontal)

    belief2_specs = models.StringField(
        label= '',
        choices = ['Less likely', 'Equally likely', 'More likely'],
        widget = widgets.RadioSelectHorizontal)

    belief3_specg = models.StringField(
        label= '',
        choices = ['Less likely', 'Equally likely', 'More likely'],
        widget = widgets.RadioSelectHorizontal)

    belief3_g_spec = models.StringField(
        label= '',
        choices = ['Less likely', 'Equally likely', 'More likely'],
        widget = widgets.RadioSelectHorizontal)

    belief3_b_spec = models.StringField(
        label= '',
        choices = ['Less likely', 'Equally likely', 'More likely'],
        widget = widgets.RadioSelectHorizontal)
    
    belief4_specs = models.StringField(
        label= '',
        choices = ['With the special rule, both genders have about the same chance',
                   'With the special rule, men have a higher chance of winning than women',
                   'With the special rule, women have have a higher chance of winning than men'],
        widget = widgets.RadioSelect)

    belief5_specs = models.IntegerField(label="")

    belief6_specs = models.IntegerField(label="")
    belief7_specs = models.IntegerField(label="")
    belief8_specs = models.IntegerField(label="")
    belief9_specs = models.IntegerField(label="")
    belief10_specs = models.IntegerField(label="")
    belief11_specs = models.IntegerField(label="")
    belief12_specs = models.IntegerField(label="")

    attention_check1 = models.StringField(
        label = 'Question: What is your favorite city?')

    attention_check2 = models.StringField(
        label= '',
        choices = ['Less likely', 'Equally likely', 'More likely'],
        widget = widgets.RadioSelectHorizontal)


