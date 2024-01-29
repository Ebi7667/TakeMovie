from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home_Page , name='home'),
    path('aboutus/', views.MovieTemplateView.as_view() , name='aboutus'),
    path('contactus/', views.MovieContactUsView.as_view() , name='contactus'),
    path('<int:pk>/', views.Detail_view.as_view() , name='frontend_Detail'),
    path('CreateMovie/', views.MovieCreateView.as_view() , name='frontend_Create'),
    path('UpdateMovie/<int:pk>/', views.MovieUpdateView.as_view() , name='frontend_Update'),
    path('DeleteMovie/<int:pk>/', views.MoviewDeleteView.as_view() , name='frontend_Delete'),
]
