from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login

def register(request):
    """register new user"""
    if request.method != 'POST':
        # No data submitted: blank form
        form = RegistrationForm()
    else:
        # Data submitted: process data
        form = RegistrationForm(data=request.post)
        if form.is_valid:
            new_user = form.save()

            login(request, new_user)
            return redirect('products:index')


    context = {'form': form}
    return render(request, 'registration/register.html', context)
        


