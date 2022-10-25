from operator import truediv
from django.shortcuts import render, redirect
from random import randint
from .models import Person, Question
from .forms import QuestionForm
from random import shuffle
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required




#todo: move me somewhere better
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
    
    #create random person with name - todo: iterate for more people!
    randName = names[randint(0,len(names) - 1)]
    randImg = images[randint(0, len(images) - 1)]
    newPerson = Person.objects.create(name=randName, imgPath=randImg)
    people = Person.objects.all()
    return render(request, 'person/detail.html', {'people': people} )

@login_required
def quiz(request):
    
    currentPerson = Person.objects.all()[0]

    
    options = [
    ('0', currentPerson),
    ('1', 'Larry Voss'),
    ('2', 'Mickey Narsisian'),
    ('3', 'Mary Lou')
]   
    shuffle(options)

    question_form = QuestionForm()
    return render(request, 'person/quiz.html', {'currentPerson': currentPerson, 'question_form' : question_form} )

@login_required
def submit_answer(request):
    print('SUBMITTING ANSWER NOW')
    Question.objects.all().delete()
    currentPersonID = Person.objects.all()[0].id
    form = QuestionForm(request.POST)
    # print(form)
    if form.is_valid:
        new_answer = form.save(commit=False)
        new_answer.person_id = currentPersonID
        new_answer.save()

    return redirect('results')

@login_required
def results(request):
    answer = Question.objects.all()[0]
    currentPerson = Person.objects.all()[0]
    
    if answer.option_names == currentPerson.name:
        win = True
    else:
        win = False

    return render(request, 'results.html', {'win': win})

#special thanks to GA Markdown for this function
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
