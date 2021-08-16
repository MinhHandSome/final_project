from django.conf.urls import url
from . import views,user_views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r"^$",views.index,name='index'),
    url(r"^all_film$",views.FilmListView.as_view(),name="all_film"),
    url(r"^view_film/(?P<pk>[0-9]+)$",views.FilmDetailView.as_view(),name='view_film'),
    url(r"^insert_film$",views.FilmCreateView.as_view(),name="insert_film"),
    url(r"^edit_film/(?P<pk>[0-9]+)$",views.FilmUpdateView.as_view(),name="edit_film"),
    url(r"^remove_film/(?P<pk>[0-9]+)$",views.FilmDeleteView.as_view(),name="remove_film"),
    url(r"^insert_director$",views.DirectorCreateView.as_view(),name="insert_director"),
    url(r"^insert_genres$",views.GenresCreateView.as_view(),name="insert_genres"),
    url(r"^all_genres$",views.GenresListView.as_view(),name="all_genres"),
    url(r"^view_genres/(?P<pk>[0-9]+)$",views.GenresDetailView.as_view(),name='view_genres'),
    url(r"^edit_genres/(?P<pk>[0-9]+)$",views.GenresUpdateView.as_view(),name="edit_genres"),
    url(r"^remove_genres/(?P<pk>[0-9]+)$",views.GenresDeleteView.as_view(),name="remove_genres"),
    url(r"^login$",user_views.login_user,name='login'),
    url(r"^register$",user_views.register_user,name= 'register_user'),
    url(r"^logout$",auth_views.LogoutView.as_view(next_page="/"),name='logout_user'),


]