from django.forms import ModelForm
from django import forms

from .models import Question
from random import shuffle
options = [
    ('0', 'Peter George'),
    ('1', 'Larry Voss'),
    ('2', 'Mickey Narsisian'),
    ('3', 'Mary Lou')
]

shuffle(options)

class QuestionForm(ModelForm):

    query = forms.ChoiceField(choices=options, widget=forms.RadioSelect)
    class Meta:
        model = Question
        fields = ['query']