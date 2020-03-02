from django.urls import path


from . import views

urlpatterns = [
    path('movies', views.get_movies, name='all_movies'),
    path('persons', views.get_persons, name='all_persons'),
    path('persons/<int:person_id>', views.get_person_by_id, name='person_by_id'),
    path('movies/<int:movie_id>', views.get_movie_by_id, name='movie_by_id'),
    path('register', views.register_user, name='register_user')
]