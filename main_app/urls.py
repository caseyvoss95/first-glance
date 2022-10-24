from django.urls import path
from . import views


urlpatterns = [
    path('', views.group_view, name='group_view'),
    path('quiz/', views.quiz, name='quiz'), 
    path('quiz/answer', views.submit_answer, name='submit_answer')
]