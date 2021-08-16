from django.db import models
from django.forms import widgets
from .forms import FilmForm,DirectorForm, GenresForm
from django.db.models import fields
from django.shortcuts import render
from .models import Film,Genres,Director
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
def index(request):
    return render(
        request=request,
        template_name='index.html'
    )
class FilmListView(ListView):
    context_object_name="all_films"
    template_name = "Film/ListFilm.html"
    paginate_by=8
    def get_queryset(self):
        all_films =Film.objects.all()
        search= self.request.GET.get('search')
        if search:
            all_films =Film.objects.filter(
                Q(title__icontains=search)
            )
        return all_films
@method_decorator(login_required(login_url='/login'),name='dispatch')
class FilmDetailView(DetailView):
    model = Film
    context_object_name ="film"
    template_name="Film/DetailFilm.html "
@method_decorator(login_required(login_url='/login'),name='dispatch')
class FilmCreateView(CreateView):
    model = Film
    form_class=FilmForm
    template_name="Film/CreateFilm.html"
    success_url="all_film"
@method_decorator(login_required(login_url='/login'),name='dispatch')
class FilmUpdateView(UpdateView):
    model=Film
    form_class=FilmForm
    template_name="Film/UpdateFilm.html"
    def get_success_url(self):
        return reverse('all_film')
@method_decorator(login_required(login_url='/login'),name='dispatch')    
class FilmDeleteView(DeleteView):
    model=Film
    fields="__all__"
    template_name="Film/DeleteFilm.html"
    def get_success_url(self):
        return reverse('all_film')
@method_decorator(login_required(login_url='/login'),name='dispatch')
class DirectorCreateView(CreateView):
    model= Director
    form_class=DirectorForm
    template_name="Director/CreateDirector.html"
    success_url="all_film"
@method_decorator(login_required(login_url='/login'),name='dispatch')
class GenresCreateView(CreateView):
    model = Genres
    form_class=GenresForm
    template_name="Genres/CreateGenres.html"
    success_url="all_film"
class GenresListView(ListView):
    model = Genres
    form_class= GenresForm
    context_object_name="all_genres"
    template_name="Genres/ListGenres.html"
    # paginate_by=8
    def get_queryset(self):
        all_genres =Genres.objects.all()
        search= self.request.GET.get('search')
        if search:
            all_genres =Genres.objects.filter(
                Q(title__icontains=search)
            )
        return all_genres
@method_decorator(login_required(login_url='/login'),name='dispatch')
class GenresDetailView(DetailView):
    model = Film
    context_object_name ="genres"
    template_name="Genres/DetailGenres.html "
    def get_object(self, queryset=None):
        return get_object_or_404(Genres, pk=self.kwargs.get('pk'))
@method_decorator(login_required(login_url='/login'),name='dispatch')
class GenresUpdateView(UpdateView):
    model=Genres
    form_class=GenresForm
    template_name="Genres/UpdateGenres.html "
    def get_success_url(self):
        return reverse('all_genres')
@method_decorator(login_required(login_url='/login'),name='dispatch')   
class GenresDeleteView(DeleteView):
    model=Genres
    form_class=GenresForm
    template_name="Genres/DeleteGenres.html "
    def get_success_url(self):
        return reverse('all_genres')