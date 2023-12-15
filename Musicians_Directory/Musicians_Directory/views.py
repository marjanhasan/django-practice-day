from django.shortcuts import render
from album.models import Album
from album.forms import AlbumForm
from musician.models import Musician
from musician.forms import MusicianForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


def home(request):
    data = Album.objects.all()
    return render(request, "index.html", {"data": data})


class EditAlbum(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "album.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("homepage")


class EditMusician(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = "musician.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("homepage")


class DeleteRow(DeleteView):
    model = Album
    template_name = "delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("homepage")
