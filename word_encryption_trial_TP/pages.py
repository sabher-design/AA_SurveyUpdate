from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Task(Page):
    timeout_seconds = Constants.timeout_seconds
    form_model = 'player'
    form_fields = ['solved_trial', 'notSolved_trial']


class Results(Page):
    pass


page_sequence = [Task,Results]
