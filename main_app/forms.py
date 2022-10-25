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
    
    options = forms.ChoiceField(label='', choices=[], widget=forms.RadioSelect)

    def __init__(self, options=None, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        if options:
            batch = []
            for option in options:
                batch.append(option)

            self.fields['options'].choices = batch


    person = Person.objects.all()[0]
    class Meta:
        model = Question
        fields = []