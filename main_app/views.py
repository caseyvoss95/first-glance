from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from random import randint
from random import shuffle
from .models import Person, Question
from .forms import QuestionForm

#assets
names = ['Dorian', 'Amos', 'Flynn', 'Kori', 'Ellison', 'Harper', 'Wyatt', 'Asher', 'River', 'Logan', 'Cameron', 'Rowan', 'Peyon', 'Ryan', 'Hayden']

images = [
    'https://images.generated.photos/RWgvMrrBsLFd8l-n8DRUpNswZF9A5qW2cN0qGUsnMps/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NzEyNTAzLmpwZw.jpg',
    'https://images.generated.photos/7E8THeypJSdoTZ4xY1PXUae9vqWLpmwVhzcDms50nUM/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NzE1MDg0LmpwZw.jpg',
    'https://images.generated.photos/1fhyHekdctHyc5xSl9VPxRD88zhU2b3C5O6ONBzXR8s/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MDUyNTEzXzAwMzU3/OTNfMDMwMjEwMi5q/cGc.jpg',
    'https://images.generated.photos/vJ2GZpArcKGX-fR26GBV8NwIIY61sdNcNJCuMKneQ1k/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MDU0MjY4XzA3NzE3/OThfMDc2NTUyMS5q/cGc.jpg',
    'https://images.generated.photos/vXh97jjk8eIrd8d8t4Ei-SPSrQ7tVnh5uX0xc2iiQBw/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTk3MDQzLmpwZw.jpg',
    'https://images.generated.photos/6AZE02WGr1kJvdJkpGndYH2G3LPcoZxIohIxL_ZrelY/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MjU5NTU1LmpwZw.jpg',
    'https://images.generated.photos/RgdJ6UxHJyqOejDLu-QsA0Cds3eEgRnZNXSwFSz9pKQ/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NDE3NjEyLmpwZw.jpg',
    'https://images.generated.photos/isEv8ypmyC47Dzn1WZLaLFGNQ__Zv-ok3SbXPRBIsqw/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTgxNjU0LmpwZw.jpg',
    'https://images.generated.photos/uIi20RXpJRth_wL4X328Lrhk0-dPbketmewWxpYheDM/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NDcyMDIzLmpwZw.jpg',
    'https://images.generated.photos/0kTfTK1NMd1kaMxX7LD8lou4M22jWq0SWn2je8sSn8E/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MTc3MTcyLmpwZw.jpg',
    'https://images.generated.photos/yZe4-qr0QKM1djPOhY9TfynsPSNdAWX7TzDpiXDFWas/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MjU0ODE0LmpwZw.jpg',
    'https://images.generated.photos/WwPo1RYmEG_jGgYgs55Pe6_ro0KUOItDnBP5Q4xixxc/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MTg4ODk0LmpwZw.jpg',
    'https://images.generated.photos/beOlEbcLFvwyyF4NcWl41CHzOUM_j1JBmiVv9rfXNdo/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MzAzMzAyLmpwZw.jpg',
    'https://images.generated.photos/hcOSbwasMacRvMSLBZU7vPR1j6OCHmO-2pz1RY2J2KE/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTIyMjM3LmpwZw.jpg',
    'https://images.generated.photos/sg6_f1W-Gavm9iLSKNTDI6LXE9HRe12fid1hAp_m7rU/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/ODc1ODM4LmpwZw.jpg',
    'https://images.generated.photos/BMTF3WJvA_XfwfVO_KlfMrDNk1sTsGSZoDSigC-TiqQ/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NzYyOTkzLmpwZw.jpg',
    'https://images.generated.photos/s3c2hmlLpJ4re4mrEhh31trI6J80CZ6sX8HCPkd4TVo/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTQ4OTM0LmpwZw.jpg',
    'https://images.generated.photos/Sl38uFmDvGDzoiXW3cdpfvx4gIvQAzftxE2hqi0LGwg/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MzI3MjUzLmpwZw.jpg',
    'https://images.generated.photos/Cd-Jnz68aQn3IFk73HXJjFo7e69mM9MS3B8N3b_LaGs/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/ODQwMDQ2LmpwZw.jpg'
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