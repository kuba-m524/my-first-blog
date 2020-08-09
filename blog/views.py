from django.shortcuts import render
from django.utils import timezone
from .models import Post  # dołączamy nasz model, kropka oznacza bieżący katalog lub bieżącą aplikację - views.py i models.py znajdują się w tym samym katalogu, dzięki czemu możemy użyć kropki . i nazwy pliku bez .py

# Create your views here.


def post_list(request):  # funkcja post_list - widok, pobierająca request
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date')  # wybieramy posty do publikacji
    # W funkcji render mamy jeden parametr request (wszystko, co otrzymujemy od użytkownika za pośrednictwem Internetu) i inny podający plik szablonu ('blog/post_list.html').
    # Ostatni parametr, który wygląda tak: {} jest miejscem, w którym możemy dodać parę rzeczy do wykorzystania w szablonie.
    # zwraca wartość uzyskaną dzięki wywołaniu funkcji render, która wyrenderuje (złoży w całość) nasz szablon blog/post_list.html
    return render(request, 'blog/post_list.html', {'posts': posts})
