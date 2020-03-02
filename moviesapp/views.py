from django.http import JsonResponse, Http404
from .models import Movie, Person
from django.contrib.auth.models import User
from moviesapp.serializers import MovieSerializer, PersonSerializer
from django.views.decorators.csrf import csrf_exempt
import json
import roman


def with_roman_year(movie):
    return {**{'roman_release_year': roman.toRoman(movie['release_year'])}, **movie}


def get_movies(request):
    return JsonResponse({'movies':
                             [with_roman_year(MovieSerializer(instance=movie).data) for movie in Movie.objects.all()]
                         })


def get_persons(request):
    return JsonResponse({'persons': [PersonSerializer(instance=person).data for person in Person.objects.all()]})


def get_person_by_id(request, person_id):
    try:
        return JsonResponse(PersonSerializer(instance=Person.objects.get(id=person_id)).data)
    except Person.DoesNotExist:
        raise Http404


def get_movie_by_id(request, movie_id):
    try:
        return JsonResponse(MovieSerializer(instance=Movie.objects.get(id=movie_id)).data)
    except Movie.DoesNotExist:
        raise Http404


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        r = json.loads(request.body)
        user = r['user']
        email = r['email']
        password = r['password']
        User.objects.create_superuser(user, email, password)
        return JsonResponse({'status': 'ok'})

