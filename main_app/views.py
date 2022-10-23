from django.shortcuts import render, redirect
import uuid
import boto3
from random import randint
from .models import Photo, Person

S3_BASE_URL = "https://s3.us-east-1.amazonaws.com"
BUCKET = "first-glance"

#todo: move me somewhere better
names = ['John', 'Amy', 'Julie', 'Barbara']


def group_view(request):
    
    Person.objects.all().delete()
    randName = names[randint(0,len(names) - 1)]
    randomPerson = Person.objects.create(name=randName, imgPath='url')
    people = Person.objects.all()
    return render(request, 'person/detail.html', {'people': people} )

def add_photo(request, person_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, person_id=person_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', person_id=person_id)