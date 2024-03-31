from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views.generic import CreateView,View
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# def user_login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form=AuthenticationForm(request,request.POST)
#             if form.is_valid():
#                 user_name= form.cleaned_data['username']
#                 user_pass= form.cleaned_data['password']
#                 user= authenticate(username=user_name,password=user_pass)
#                 if user is not None:
#                     messages.success(request,'Logged in successfully')
#                     login(request,user)
#                     return redirect('home')
#                 else:
#                     messages.warning(request,'Invalid Information Entered')
#                     return redirect('user_login')
#         else:
#             form= AuthenticationForm(request,request.POST)
#         return render(request,'user_login.html',{'form':form})
#     else:
#         return redirect('user_profile')

class Login(LoginView):
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    template_name = 'user_login.html'

# def user_signup(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             signup_form= SignUpForm(request.POST)
#             if signup_form.is_valid():
#                 signup_form.save()
#                 messages.success(request,'SignUp Successfully')
#                 return redirect('user_login')
#         else:
#             signup_form= SignUpForm(request.POST)
#         return render(request,'user_signup.html',{'form':signup_form})
#     else :
#         return redirect('user_logout')

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'user_signup.html'
    success_url = reverse_lazy('user_login')

# @login_required
# def user_logout(request):
#     logout(request)
#     messages.success(request,'Logged Out Successfully')
#     return redirect('user_login')

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('user_login')
