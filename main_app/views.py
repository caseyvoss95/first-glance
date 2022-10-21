from django.shortcuts import render


def group_view(request):
    return render(request, 'group_view.html')