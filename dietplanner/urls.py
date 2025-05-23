from django.urls import path
from .views import diet_planner

urlpatterns = [
    path('', diet_planner, name='diet_planner'),
]
