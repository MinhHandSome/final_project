from django.conf.urls import url
from . import views
urlpatterns=[
    url(r"^api_all_films$",views.api_all_film,name='api_all_film'),
    url(r"api_view_film/(?P<film_id>[0-9]+)$",views.api_view_film,name="api_view_film"),
    url(r"^api_create_film$",views.api_create_film,name='api_create_film'),

]