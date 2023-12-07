from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def musician(request):
    if request.method == "POST":
        musicianForm = forms.MusicianForm(request.POST)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect("add_musician")
    else:
        musicianForm = forms.MusicianForm()
    return render(request, "musician.html", {"form": musicianForm})
