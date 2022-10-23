from django.urls import path
from . import views


urlpatterns = [
    path('', views.group_view, name = 'group_view'),
    path('person/<int:person_id>/add_person/', views.add_photo, name='add_photo'),

]