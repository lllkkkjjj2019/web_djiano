from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from learning_logs.views import index


# Create your views here.:
def register(request):
    """register new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
        login(request,new_user)
        return redirect('learning_logs:index')

    # Display a new form or indicate that the form data is invalid
    context = {'form':form}
    return render(request,'registration/register.html',context)