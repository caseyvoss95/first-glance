from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from random import randint
from random import shuffle
from .models import Person, Question
from .forms import QuestionForm

#assets
names = ['Dorian', 'Amos', 'Flynn', 'Kori', 'Ellison', 'Harper', 'Wyatt', 'Asher']

images = [
    'https://images.generated.photos/RWgvMrrBsLFd8l-n8DRUpNswZF9A5qW2cN0qGUsnMps/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NzEyNTAzLmpwZw.jpg',
    'https://images.generated.photos/7E8THeypJSdoTZ4xY1PXUae9vqWLpmwVhzcDms50nUM/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NzE1MDg0LmpwZw.jpg',
    'https://images.generated.photos/1fhyHekdctHyc5xSl9VPxRD88zhU2b3C5O6ONBzXR8s/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MDUyNTEzXzAwMzU3/OTNfMDMwMjEwMi5q/cGc.jpg',
    'https://images.generated.photos/vJ2GZpArcKGX-fR26GBV8NwIIY61sdNcNJCuMKneQ1k/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MDU0MjY4XzA3NzE3/OThfMDc2NTUyMS5q/cGc.jpg',
    'https://images.generated.photos/vXh97jjk8eIrd8d8t4Ei-SPSrQ7tVnh5uX0xc2iiQBw/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTk3MDQzLmpwZw.jpg',
    'https://images.generated.photos/6AZE02WGr1kJvdJkpGndYH2G3LPcoZxIohIxL_ZrelY/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MjU5NTU1LmpwZw.jpg',
    'https://images.generated.photos/RgdJ6UxHJyqOejDLu-QsA0Cds3eEgRnZNXSwFSz9pKQ/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NDE3NjEyLmpwZw.jpg',
    'https://images.generated.photos/isEv8ypmyC47Dzn1WZLaLFGNQ__Zv-ok3SbXPRBIsqw/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTgxNjU0LmpwZw.jpg',
]

@login_required
def group_view(request):
    Person.objects.all().delete()
    Question.objects.all().delete()
    #create 4 random people with random name
    for idx in range(4):
        randName = names[randint(0,len(names) - 1)]
        randImg = images[randint(0, len(images) - 1)]
        Person.objects.create(name=randName, imgPath=randImg)
    people = Person.objects.all()
    currentId = Person.objects.first().id

    return render(request, 'person/detail.html', {'people': people, 'currentId' : currentId} )

@login_required
def quiz(request, person_id):
    currentPerson = Person.objects.get(id=person_id)
    question_form = QuestionForm()
    nextId = person_id + 1
    print(f'next_id is {nextId}')

    return render(request, 'person/quiz.html', {'currentPerson': currentPerson, 'question_form' : question_form, 'nextId' : nextId} )

@login_required
def submit_answer(request, person_id):
    #checking for last person
    if person_id == Person.objects.last().id: 
        lastQuestion = True
    else:
        lastQuestion = False
    form = QuestionForm(request.POST)
    if form.is_valid:
        new_answer = form.save(commit=False)
        new_answer.person_id = person_id
        new_answer.save()
    if not lastQuestion:
        return redirect(f'/quiz/{person_id + 1}/' )
    return redirect('results')

@login_required
def results(request):
    score = 0
    firstId = Person.objects.first().id
    lastId = Person.objects.last().id
    questionId = Question.objects.first().id
    for id in range(firstId, lastId + 1):
        answer = Question.objects.get(id=questionId)
        person = Person.objects.get(id=id)
        if answer.option_names == person.name:
            score += 1
        questionId += 1
    return render(request, 'results.html', {'score': score})

    


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('group_view')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)