import django_tables2 as tables
from .models import *

class TrialTable(tables.Table):
    class Meta:
        model = Trial
        exclude = ['session', 'id']
        attrs = {'id': 'trials'}
