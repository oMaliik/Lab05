from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

people = []

class Person:
    def __init__(self, name, password):
        self.username = name
        self.password = password

    def __str__(self):
        return self.username

class NewPersonForm(forms.Form):
    name = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)    

def index(request):      
    return render(request, "Person/index.html", {
        "people": people
    })

def add(request):
    if request.method == "POST":
        form = NewPersonForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            person = Person(name,password)
            people.append(person)
            return HttpResponseRedirect(reverse("Person:index"))
        else:
            return render(request, "Person/add.html",{
                "form": form
            })
    else:
        return render(request, "Person/add.html",{
            "form": NewPersonForm()
        })