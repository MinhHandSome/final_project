from django.core.checks import messages
from django.shortcuts import render
from myapp.models import Film,Director,Genres
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def api_all_film(request):
    films= Film.objects.all()
    res=[]
    for film in films:
        res.append({
            'id':film.id,
            'title':film.title,
            'image_url':film.image_url,
            'video_url':film.video_url,
            'director': film.director.name,
            'genres': film.genres.name,
            'actor':film.actor,
            'runtime':film.runtime,
            'rated':film.rated,
            'content':film.content,
            
        })
    return Response(data=res,status=200)
@api_view(['GET'])
def api_view_film(request,film_id):
    try:
        film= Film.objects.get(id=film_id)
        res={
            'title':film.title,
            'image_url':film.image_url,
            'video_url':film.video_url,
            'director': film.director.name,
            'genres': film.genres.name,
            'actor':film.actor,
            'runtime':film.runtime,
            'rated':film.rated,
            'content':film.content,
        }
        return Response(data=res,status=200)
    except Film.DoesNotExist:
        return Response(data={
            "message":f"Film id {film_id} Not Found!"},
            status=404
        )
@api_view(['POST'])
def api_create_film(request):
    create_id=Film.objects.create(**request.data)
    return Response(data={
        "message":f"Film id created {create_id}"
    },status=201)
    