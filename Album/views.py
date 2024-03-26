from django.shortcuts import render,redirect
from .forms import AlbumForm
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form=AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    else:
        album_form=AlbumForm(request.POST)
    return render(request,'add_album.html',{'form': album_form})