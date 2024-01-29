from django.urls import path
from . import views
urlpatterns = [
    path('register/' , views.UserRegistareView.as_view(),name='form_creation') 
]
