from django.shortcuts import render
from .forms import AlbumForm
# Create your views here.
def add_album(request):
    album_form=AlbumForm
    return render(request,'add_album.html',{'form': album_form})