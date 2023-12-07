from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def album(request):
    if request.method == "POST":
        albumForm = forms.AlbumForm(request.POST)
        if albumForm.is_valid():
            albumForm.save()
            return redirect("add_album")
    else:
        albumForm = forms.AlbumForm()
    return render(request, "album.html", {"form": albumForm})
