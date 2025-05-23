from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Training
from .forms import TrainingForm, ExerciseFormSet

@login_required
def training_planner(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        formset = ExerciseFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            training = form.save(commit=False)
            training.user = request.user
            training.save()
            formset.instance = training
            formset.save()
            return redirect('training_planner_list')  # przekierowanie do listy treningów
    else:
        form = TrainingForm()
        formset = ExerciseFormSet()

    workouts = Training.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'trainingplanner/training_planner.html', {
        'form': form,
        'formset': formset,
        'workouts': workouts,
    })

@login_required
def training_planner_list(request):
    trainings = Training.objects.filter(user=request.user)
    return render(request, 'trainingplanner/training_list.html', {'trainings': trainings})
