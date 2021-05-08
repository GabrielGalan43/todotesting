from django.shortcuts import render, redirect
from django.contrib import messages
from users_app.forms import CustomRegisterForm


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST or none)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'New account created!')
        return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'users_app/registration.html', {'register_form': register_form})
