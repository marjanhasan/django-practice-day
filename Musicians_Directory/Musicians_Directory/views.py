from django.shortcuts import render, redirect
from album.models import Album
from album.forms import AlbumForm
from musician.models import Musician
from musician.forms import MusicianForm


def home(request):
    data = Album.objects.all()
    return render(request, "index.html", {"data": data})


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    albumForm = AlbumForm(instance=album)
    if request.method == "POST":
        albumForm = AlbumForm(request.POST, instance=album)
        if albumForm.is_valid():
            albumForm.save()
            return redirect("homepage")
    return render(request, "album.html", {"form": albumForm})


def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    musicianForm = MusicianForm(instance=musician)
    if request.method == "POST":
        musicianForm = MusicianForm(request.POST, instance=musician)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect("homepage")
    return render(request, "musician.html", {"form": musicianForm})


def delete_row(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect("homepage")
