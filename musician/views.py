from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import MusicianForm
from .models import Musician
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView
# Create your views here.

# @login_required
# def add_musician(request):
#     if request.method=='POST':
#         musician_form=MusicianForm(request.POST)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('home')
#     else:
#         musician_form=MusicianForm(request.POST)
        
#     return render(request,'add_musician.html',{'form':musician_form})


class AddMusician(CreateView):
    model = Musician
    form_class= MusicianForm
    template_name='add_musician.html'
    success_url= reverse_lazy('home')

# @login_required
# def edit_musician(request, id):
#     musician= Musician.objects.get(pk=id)
#     musician_form= MusicianForm(instance=musician)
#     if request.method=='POST':
#         musician_form=MusicianForm(request.POST, instance=musician)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('home')
        
#     return render(request,'add_musician.html',{'form':musician_form})

class EditMusician(UpdateView):
    model=Musician
    form_class=MusicianForm
    template_name= 'add_musician.html'
    pk_url_kwarg='id'
    success_url= reverse_lazy('home')
