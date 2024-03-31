from django.urls import path
from . import views
urlpatterns = [
    # path('add/',views.add_musician,name='add_musician'),
    path('add/',views.AddMusician.as_view(),name='add_musician'),
    # path('edit/<int:id>',views.edit_musician,name='edit_musician')
    path('edit/<int:id>',views.EditMusician.as_view(),name='edit_musician')
]
