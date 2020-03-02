from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=128)
    release_year = models.PositiveSmallIntegerField(blank=True, null=True)
    casting = models.ManyToManyField('Person', through='Acts', through_fields=('movie', 'person'))
    directors = models.ManyToManyField('Person', related_name='directors', through='Directs',
                                       through_fields=('movie', 'person'))
    producers = models.ManyToManyField('Person', related_name='producers', through='Produces',
                                       through_fields=('movie', 'person'))

    def get_casting(self):
        return ", ".join([str(p) for p in self.casting.all()])

    def get_directors(self):
        return ", ".join([str(p) for p in self.directors.all()])

    def get_producers(self):
        return ", ".join([str(p) for p in self.producers.all()])

    def __str__(self):
        return self.title + ' (' + str(self.release_year) + ')'


class Person(models.Model):
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    movies_as_acting = models.ManyToManyField(Movie, through='Acts', through_fields=('person', 'movie'))
    movies_as_director = models.ManyToManyField(Movie, related_name='as_director', through='Directs',
                                                through_fields=('person', 'movie'))
    movies_as_producer = models.ManyToManyField(Movie, related_name='as_producer', through='Produces',
                                                through_fields=('person', 'movie'))

    def get_movies_as_acting(self):
        return ", ".join([str(p) for p in self.movies_as_acting.all()])

    def get_movies_as_director(self):
        return ", ".join([str(p) for p in self.movies_as_director.all()])

    def get_movies_as_producer(self):
        return ", ".join([str(p) for p in self.movies_as_producer.all()])

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Acts(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person) + ' is acting in ' + str(self.movie)

    class Meta:
        verbose_name_plural = 'Acting'


class Directs(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person) + ' directs ' + str(self.movie)

    class Meta:
        verbose_name_plural = 'Directing'


class Produces(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person) + ' produces ' + str(self.movie)

    class Meta:
        verbose_name_plural = 'Producing'
