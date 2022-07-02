from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Unsure if these are needed yet
# from django.views import View
# import json

def hi(request):
    return render(request, 'app/home-page.html')

def chatbot(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        print(name, email)
    form = ContactForm()
    return render(request, 'form.html', {'form': form})