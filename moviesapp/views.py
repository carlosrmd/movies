from django.http import JsonResponse, Http404, HttpResponse, HttpResponseBadRequest
from .models import Movie, Person
from django.contrib.auth.models import User
from moviesapp.serializers import MovieSerializer, PersonSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from http import HTTPStatus
import json
import roman


class HttpResponseConflict(HttpResponse):
    status_code = HTTPStatus.CONFLICT


def with_roman_year(movie):
    return {**{'roman_release_year': roman.toRoman(movie['release_year'])}, **movie}


def get_movies(request):
    return JsonResponse({'movies': [
                                 with_roman_year(MovieSerializer(instance=movie).data) for movie in Movie.objects.all()
                             ]
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
        try:
            r = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest()
        try:
            user = r['user']
            email = r['email']
            password = r['password']
        except KeyError:
            return HttpResponseBadRequest()
        try:
            User.objects.create_superuser(user, email, password)
        except IntegrityError:
            return HttpResponseConflict()
        return JsonResponse({'status': 'ok'})
