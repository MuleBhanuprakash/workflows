from django.shortcuts import render, HttpResponseRedirect
from app1 import forms


# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/bye')
    else:
        form = forms.RegistrationForm
        return render(request, 'registration.html', {'form': form})


def thank_you(request):
    return render(request, 'thanks.html')
