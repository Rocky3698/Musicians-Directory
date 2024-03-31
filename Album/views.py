from django import dispatch
from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

# @login_required
# def add_album(request):
#     if request.method == 'POST':
#         album_form=AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('home')
#     else:
#         album_form=AlbumForm(request.POST)
#     return render(request,'add_album.html',{'form': album_form})
@method_decorator(login_required,name='dispatch')
class AddAlbum(CreateView):
    model = Album
    form_class=AlbumForm
    template_name='add_album.html'
    success_url=reverse_lazy('home')

# @login_required
# def edit_album(request,id):
#     album= Album.objects.get(pk=id)
#     album_form=AlbumForm(instance=album)

#     if request.method == 'POST':
#         album_form=AlbumForm(request.POST, instance=album)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('home')
        
#     return render(request,'add_album.html',{'form': album_form})
@method_decorator(login_required,name='dispatch')
class EditAlbum(UpdateView):
    model = Album
    template_name='add_album.html'
    form_class= AlbumForm
    pk_url_kwarg= 'id'
    success_url=reverse_lazy('home')

# @login_required
# def delete_album(request,id):
#     album= Album.objects.get(pk=id)
#     album.delete()
#     return redirect('home')
@method_decorator(login_required,name='dispatch')
class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    pk_url_kwarg= 'id'
    success_url = reverse_lazy('home')
