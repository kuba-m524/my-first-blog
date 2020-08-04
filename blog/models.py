from django.db import models # dodanie biliotek
from django.utils import timezone

# definicja modelu
class Post(models.Model): # class - sygnalizacja że tworzymy obiekt, Post - nazwa naszego modelu, od dużej litery, models.Model - Post jako jeden z modelów Django
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # odnośnik do innego modelu
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): # metoda publikująca wpis, przy nazwach metod używamy małych liter oraz znaków podkreślenia zamiast spacji
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # należy pamiętać o tych "dunder" - "double-underscore"
        return self.title
