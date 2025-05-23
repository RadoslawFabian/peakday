from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainpage:home')  # ← poprawione
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
