from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from random import randint
from .models import Person, Question
from .forms import QuestionForm

#todo: move me somewhere better
names = ['John', 'Bobby', 'Amy', 'Julie', 'Barbara']

images = [
    'https://images.generated.photos/RWgvMrrBsLFd8l-n8DRUpNswZF9A5qW2cN0qGUsnMps/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NzEyNTAzLmpwZw.jpg',
    'https://images.generated.photos/7E8THeypJSdoTZ4xY1PXUae9vqWLpmwVhzcDms50nUM/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NzE1MDg0LmpwZw.jpg',
    'https://images.generated.photos/1fhyHekdctHyc5xSl9VPxRD88zhU2b3C5O6ONBzXR8s/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MDUyNTEzXzAwMzU3/OTNfMDMwMjEwMi5q/cGc.jpg',
]

def group_view(request):
    
    Person.objects.all().delete()
    randName = names[randint(0,len(names) - 1)]
    randImg = images[randint(0, len(images) - 1)]
    Person.objects.create(name=randName, imgPath=randImg)
    people = Person.objects.all()
    return render(request, 'person/detail.html', {'people': people} )


def quiz(request):
    currentPerson = Person.objects.all()[0]
    question_form = QuestionForm()
    return render(request, 'person/quiz.html', {'currentPerson': currentPerson, 'question_form' : question_form} )

def submit_answer(request):
    print('SUBMITTING ANSWER NOW')
    form = QuestionForm(request.POST)
    if form.is_valid:
        new_answer = form.save(commit=False)
        new_answer.person_id = 114
        new_answer.save()

    return redirect('quiz')