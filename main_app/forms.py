from django.forms import ModelForm
from django import forms

from .models import Question, Person
from random import shuffle
from main_app import views


options = [
    ('0', 'foo'),
    ('1', 'Larry Voss'),
    ('2', 'Mickey Narsisian'),
    ('3', 'Mary Lou')
]
shuffle(options)


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['option_names']