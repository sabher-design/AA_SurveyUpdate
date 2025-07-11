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

import random
import json

# from otreeutils.surveys import generate_likert_field


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'quest'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            groups = ['women', 'minorities', 'disabilities']
            p.aa_order_favor = json.dumps(random.sample(groups, k=3))
            p.aa_order_disadvantage = json.dumps(random.sample(groups, k=3))
            p.aa_order_effort = json.dumps(random.sample(groups, k=3))
            p.aa_order_skills = json.dumps(random.sample(groups, k=3))



class Group(BaseGroup):
    pass



class Player(BasePlayer):

    ProlificID = models.StringField(
        label="Please enter your Prolific ID to start the study.",
        blank = False)

    aa_order_favor = models.StringField()
    aa_order_disadvantage = models.StringField()
    aa_order_effort = models.StringField()
    aa_order_skills = models.StringField()


    # --- Favor/Oppose ---
    aa_favor_women = models.StringField(
        choices=['Favor', 'Oppose', 'No opinion'],
        label='Do you generally favor or oppose affirmative action programs for women?',
        widget=widgets.RadioSelectHorizontal)

    aa_favor_minorities = models.StringField(
        choices=['Favor', 'Oppose', 'No opinion'],
        label='Do you generally favor or oppose affirmative action programs for racial minorities?',
        widget=widgets.RadioSelectHorizontal)

    aa_favor_disabilities = models.StringField(
        choices=['Favor', 'Oppose', 'No opinion'],
        label='Do you generally favor or oppose affirmative action programs for people with disabilities?',
        widget=widgets.RadioSelectHorizontal)

    # --- Belief Questions (Likert 1–10) ---
    aa_belief_disadvantage_women = models.IntegerField(label="To which extent do you believe that women are facing unjustified disadvantage and/or discrimination in everyday life?",
                                                       widget=widgets.RadioSelectHorizontal,
                                                       choices=list(range(0, 11)))

    aa_belief_effort_women = models.IntegerField(label="To which extent do you believe that women are exerting less effort to perform strongly in everyday life (e.g. in education or work environments) than men?",
                                                 widget=widgets.RadioSelectHorizontal,
                                                 choices=list(range(0, 11)))

    aa_belief_skills_women = models.IntegerField(label="To which extent do you believe that women tend to have lower inborn skills than men?",
                                                 widget=widgets.RadioSelectHorizontal,
                                                 choices=list(range(0, 11)))

    aa_belief_disadvantage_minorities = models.IntegerField(label="To which extent do you believe that racial minorities are facing unjustified disadvantage and/or discrimination in everyday life?",
                                                            widget=widgets.RadioSelectHorizontal,
                                                            choices=list(range(0, 11)))

    aa_belief_effort_minorities = models.IntegerField(label="To which extent do you believe that racial minorities are exerting less effort to perform strongly in everyday life (e.g. in education or work environments) than people who do not belong to a racial minority?",
                                                      widget=widgets.RadioSelectHorizontal,
                                                      choices=list(range(0, 11)))

    aa_belief_skills_minorities = models.IntegerField(label="To which extent do you believe that racial minorities tend to have lower inborn skills than people who do not belong to a racial minority?",
                                                      widget=widgets.RadioSelectHorizontal,
                                                      choices=list(range(0, 11)))

    aa_belief_disadvantage_disabilities = models.IntegerField(label="To which extent do you believe that people with disabilities are facing unjustified disadvantage and/or discrimination in everyday life?",
                                                              widget=widgets.RadioSelectHorizontal,
                                                              choices=list(range(0, 11)))

    aa_belief_effort_disabilities = models.IntegerField(label="To which extent do you believe that people with disabilities are exerting less effort to perform strongly in everyday life (e.g. in education or work environments) than people who are not disabled?",
                                                        widget=widgets.RadioSelectHorizontal,
                                                        choices=list(range(0, 11)))

    aa_belief_skills_disabilities = models.IntegerField(label="To which extent do you believe that people with disabilities tend to have lower inborn skills than people who are not disabled?",
                                                        widget=widgets.RadioSelectHorizontal,
                                                        choices=list(range(0, 11)))


    risk = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label=''' 
        How do you see yourself? 
        Are you generally a person who is fully prepared to take risks or do you try to avoid taking risks? 
        Please tick a box on the scale, where the value 0 means: ‘unwilling to take risks’ and the value 10 means: ‘fully prepared to take risk’.''')

    social = models.IntegerField(
        label='''
        Imagine the following situation:
        Today you unexpectedly received 1,000 USD. How much of this amount would you donate to a good cause?''',
        min=0, max=1000)

    gender = models.StringField(
        choices=['Male', 'Female', 'Diverse'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    gender_diverse = models.StringField(
        label="If you answered Diverse:",
        blank=True)

    age = models.IntegerField(
        label='What is your age?',
        min=18, max=100)

    employment = models.StringField(
        label='What is your employment status?',
        choices=['Full-time employee', 'Part-time employee', 'Retired', 'Student',
                 'Self-employed or business owner', 'Unemployed and looking for work',
                 'Not working and not currently looking for work'],
        widget=widgets.RadioSelect)

    socialclass = models.StringField(
        label='''
        If you had to use one of these five commonly-used names 
        to describe your social class, which one would it be?''',
        choices=['Lower Class or Poor', 'Working Class', 'Middle Class',
                 'Upper-middle Class', 'Upper Class'],
        widget=widgets.RadioSelect)

    children = models.IntegerField(
        label='How many children do you have?',
        min=0, max=100)

    income = models.StringField(
        label='''
        Which category represents your total combined household income during the past 12 months? 
        This includes money from jobs, net income from business, farm or rent, pensions, dividends, interests, 
        social security payments and any other money income received.''',
        choices=['Less than $5,000', '$5,000 to $7,499',
                 '$7,500 to $9,999', '$10,000 to $12,499', '$12,500 to $14,999',
                 '$15,000 to $19,999', '$20,000 to $24,999', '$25,000 to $29,999',
                 '$30,000 to $34,999', '$35,000to $39,999', '$40,000 to $49,999',
                 '$50,000 to $59,999', '$60,000 to $74,999', '$75,000 to $99,999',
                 '$100,000 to $149,999', '$150,000 or more'],
        widget=widgets.RadioSelect)

    household_children = models.IntegerField(
        label='How many children does your household have?',
        min=0, max=100)

    household_adults = models.IntegerField(
        label='How many adults does your household have?',
        min=0, max=100)

    ethnicity = models.StringField(
        label='What is your ethnicity or cultural background?',
        choices=['White', 'Hispanic', 'Latino or Spanish origin',
                 'Black or African American', 'American Indian', 'Alaska Native', 'Native American',
                 'Asian', 'Pacific Islander', 'Other'],
        widget=widgets.RadioSelect)

    ethnicity_other = models.StringField(
        label='If you selected Other:',
        blank=True)

    mother_tongue = models.StringField(
        label='What is your mother tongue(s)?')

    IQ = models.StringField(
        label='''What is the highest level of school you 
        have completed or the highest degree you have received?''',
        choices=['No high school diploma', 'High school diploma or equivalent',
                 'Some college but no degree', 'Associate degree in college (2-year college)',
                 '''Bachelor's degree (4-year college)''',
                 '''Master's degree (For example: MA, MS, MEng, MEd, MSW, MBA)''',
                 'Professional School Degree or Doctorate Degree (For example: MD, DDS,DVM,LLB,JD, PhD, EdD)'],
        widget=widgets.RadioSelect)

    sexual_orientation = models.StringField(
        label='What is your sexual orientation?',
        choices=['Heterosexual', 'Homosexual', 'Other', 'Prefer not to say'],
        widget=widgets.RadioSelect)

    sexual_orientation_other = models.StringField(
        label='If you selected Other:',
        blank=True)

    political = models.StringField(
        label='''We hear a lot of talk these days about ‘liberals’ and ‘conservatives’. 
        Here is a 7-point-scale on which people’s political views are arranged 
        from extremely liberal to extremely conservative. 
        Where would you place yourself on this scale?''',
        choices=['Extremely liberal', 'Liberal', 'Slightly liberal',
                 'Moderate, middle of the road', 'Slightly conservative',
                 'Conservative', 'Extremely conservative'],
        widget=widgets.RadioSelect)

    discrimination = models.StringField(
        label='''Have you ever experienced discrimination because of your race, 
        ethnicity, gender, age, religion, physical appearance, 
        sexual orientation, or other characteristics?''',
        choices=['Yes – very often', 'Yes – often', 'Yes – sometimes', 'Yes – rarely',
                 'No – never'],
        widget=widgets.RadioSelect)

    # Efficiency preference
    ###Token for Person A
    token_1 = models.IntegerField(label="")
    ###Token for Person B
    token_2 = models.IntegerField(label="")

    # Fairness perception
    fairness_AA = models.IntegerField(
        choices=list(range(7)),
        widget=widgets.RadioSelectHorizontal,
        label='')

    fairness_noAA = models.IntegerField(
        choices=list(range(7)),
        widget=widgets.RadioSelectHorizontal,
        label='')

    # Overconfidence
    quiz1 = models.StringField(
        label='What is the capital city of France?',
        choices=['Barcelona', 'Paris'],
        widget=widgets.RadioSelect)

    quiz2 = models.StringField(
        label='''How much does an average chimpanzee weigh?''',
        choices=['500kg', '50kg'],
        widget=widgets.RadioSelect)

    quiz3 = models.StringField(
        label=''' "The starry night" is a famous painting by...''',
        choices=['Jackson Pollock', 'Vincent van Gogh'],
        widget=widgets.RadioSelect)

    quiz4 = models.StringField(
        label=''' "Verre" means "glass" in which language?''',
        choices=['Italian', 'French'],
        widget=widgets.RadioSelect)

    quiz5 = models.StringField(
        label='''Amsterdam is nearer to?''',
        choices=['Antwerp', 'Rotterdam'],
        widget=widgets.RadioSelect)

    quiz6 = models.StringField(
        label='''The capital of Hawaii is...''',
        choices=['Waikiki', 'Honolulu'],
        widget=widgets.RadioSelect)

    quiz7 = models.StringField(
        label='''Which weighs more?''',
        choices=['The London Eye', 'The Eiffel Tower'],
        widget=widgets.RadioSelect)

    quiz8 = models.StringField(
        label=''' "Kieselstein" means "pebble" in which language?''',
        choices=['Russian', 'German'],
        widget=widgets.RadioSelect)

    quiz9 = models.StringField(
        label=''' "The Creation of Adam" is a painting by...''',
        choices=['Leonardo da Vinci', 'Michelangelo'],
        widget=widgets.RadioSelect)

    quiz10 = models.StringField(
        label=''' "Dronning" means "queen" in which language?''',
        choices=['Serbian', 'Norwegian'],
        widget=widgets.RadioSelect)

    # Overconfidence
    your_rank = models.IntegerField()

    attention_check1 = models.StringField(
        label = 'Question: What is your favorite city?')

    attention_check3 = models.StringField(
        label='',
        choices=['Wine', 'Beer', 'Whiskey', 'Carrot juice', 'Vodka', 'Other'],
        widget=widgets.RadioSelect)

    # Disability status
    deaf = models.StringField(
        label='Are you deaf, or do you have serious difficulty hearing?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect)

    blind = models.StringField(
        label='Are you blind, or do you have serious difficulty seeing, even when wearing glasses?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect)

    concentration = models.StringField(
        label='Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering,'
              ' or making decisions?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect)

    walking = models.StringField(
        label='Do you have serious difficulty walking or climbing stairs?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect)

    dressing = models.StringField(
        label='Do you have difficulty dressing or bathing?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect)

    errands = models.StringField(
        label='Because of a physical, mental, or emotional condition, do you have difficulty doing errands alone such as '
              'visiting a doctor\'s office or shopping?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect)

    # AA
    AA_affected = models.StringField(
        label='Do you believe that you have ever been affected by affirmative action in your life?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect)

    AA_affected_yes = models.StringField(
        label='If yes, please state the context/kind of affirmative action measures:',
        blank=True)

    AA_benefited = models.StringField(
        label='Do you believe that you have ever benefited from affirmative action in your life?',
        choices=['Yes, I believe I have rather benefited', 'No, I believe I have rather been harmed'],
        widget=widgets.RadioSelect)

    AA_context = models.StringField(
        label='Please state the context/kind of affirmative action measure(s):')

    # Efficiency loss
    efficiency_loss_women = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''To which extent do you believe that affirmative action programs for <strong>women</strong> induce efficiency losses, 
        e.g., due to less productive people being admitted to university or being hired or promoted?''')

    efficiency_loss_racial_minorities = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''To which extent do you believe that affirmative action programs for <strong>racial minorities</strong>
         induce efficiency losses, e.g., due to less productive people being admitted to university or being hired or 
         promoted?''')

    efficiency_loss_disabilities = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''To which extent do you believe that affirmative action programs for <strong>people with disabilities</strong>
         induce efficiency losses, e.g., due to less productive people being admitted to university or being hired or promoted?''')