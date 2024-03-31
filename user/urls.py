from django.urls import path
from . import views
urlpatterns = [
    # path('login/',views.user_login,name='user_login'),
    path('login/',views.Login.as_view(),name='user_login'),
    path('signup/',views.SignUp.as_view(),name='user_signup'),
    path('logout/',views.Logout.as_view(),name='user_logout'),
]
