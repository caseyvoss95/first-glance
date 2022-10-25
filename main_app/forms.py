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
    
    product_name = forms.ChoiceField(label='', choices=[], widget=forms.RadioSelect)

    def __init__(self, products=None, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        if products:
            batch = []
            for product in products:
                batch.append(product)

            self.fields['product_name'].choices = batch


    person = Person.objects.all()[0]
    class Meta:
        model = Question
        fields = ['query']