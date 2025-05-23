from django.urls import path
from .views import training_planner_list, training_planner

urlpatterns = [
    path('', training_planner, name='training_planner'),
    path('list/', training_planner_list, name='training_planner_list'),
]
