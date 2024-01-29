from django.shortcuts import render
from .models import Movies
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed
#List_View
# def Movie_View(request):
#     video=Movies.objects.all()
#     return render(request,'home.html',{'Listdb':video})
# class List_View(ListView):
#     model=Movies
#     template_name='home.html'
#     context_object_name='Listdb'
#Detail_View
# def Detail_View(request , Movie_id):
#     video=Movies.objects.get(id=Movie_id)
#     return render(request,'Detail.html',{'Detaildb':video})
# class Detail_view(DetailView):
#     model=Movies
#     template_name='Detail.html'
#     context_object_name='Detaildb'
def Home_Page(request):
    film=Movies.objects.filter(entity_type='فیلم')
    series=Movies.objects.filter(entity_type='سریال')
    new_film=Movies.objects.filter(entity_type='تریلر')
    inception=Movies.objects.get(entity_type='تک فیلم')
    return render(request,'index.html', {'filmdb':film , 'seriesdb':series , 'incdb':inception , 'new_film':new_film })
class Detail_view(DetailView):
     model=Movies
     template_name='movie-details.html'
     context_object_name='detaildb'
class MovieCreateView(CreateView):
    model=Movies
    template_name='movie_create.html'
    fields=['user','name','entity_type','zhanr','running_time','photo','limit_age']
class MovieUpdateView(UpdateView):
    model=Movies
    template_name='movie_update.html'
    fields=['name','zhanr','running_time','limit_age','photo']
class MoviewDeleteView(DeleteView):
    model=Movies
    template_name='movie_delete.html'
    success_url=reverse_lazy('frontend_Create')
class MovieTemplateView(TemplateView):
    template_name='AboutUs.html'
class MovieContactUsView(TemplateView):
    template_name='ContactUs.html'
