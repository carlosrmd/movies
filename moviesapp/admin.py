from django.contrib import admin
from .models import Movie, Person, Acts, Directs, Produces
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'get_casting', 'get_directors', 'get_producers')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_movies_as_acting', 'get_movies_as_director',
                    'get_movies_as_producer')


admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Acts)
admin.site.register(Directs)
admin.site.register(Produces)
