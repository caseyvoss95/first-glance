from django.shortcuts import render


def group_view(request):
    return render(request, 'person/detail.html')