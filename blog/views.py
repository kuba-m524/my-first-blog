from django.shortcuts import render

# Create your views here.
def post_list(request): # funkcja post_list - widok, pobierająca request
    return render(request, 'blog/post_list.html', {}) # zwraca wartość uzyskaną dzięki wywołaniu funkcji render, która wyrenderuje (złoży w całość) nasz szablon blog/post_list.html