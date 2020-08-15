from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post  # dołączamy nasz model, kropka oznacza bieżący katalog lub bieżącą aplikację - views.py i models.py znajdują się w tym samym katalogu, dzięki czemu możemy użyć kropki . i nazwy pliku bez .py
from .forms import PostForm  # importujemy funkcję PostForm
from django.shortcuts import redirect  # importujemy funkcję redirect

# Create your views here.


def post_list(request):  # funkcja post_list - widok, pobierająca request
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date')  # wybieramy posty do publikacji
    # W funkcji render mamy jeden parametr request (wszystko, co otrzymujemy od użytkownika za pośrednictwem Internetu) i inny podający plik szablonu ('blog/post_list.html').
    # Ostatni parametr, który wygląda tak: {} jest miejscem, w którym możemy dodać parę rzeczy do wykorzystania w szablonie.
    # zwraca wartość uzyskaną dzięki wywołaniu funkcji render, która wyrenderuje (złoży w całość) nasz szablon blog/post_list.html
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":  # jeżeli zmienna method jest równa POST
        # budujemy formularz PostForm z danymi z formularza
        form = PostForm(request.POST)
        if form.is_valid():  # sprawdzamy następnie czy formularz jest wypełniony poprawnie (wszystkie wymagane pola są uzupełnione i żadna nieprawidłowa wartość nie zostanie zapisana)
            # zapisujemy formularz, commit=False sygnalizuje, że jeszcze nie chcemy zapisywać modelu Post - najpierw chcemy dodać autora
            # przez większość czasu będziemy używać form.save() bez commit=False, ale w tym przypadku musimy zrobić to w ten sposób
            post = form.save(commit=False)
            post.author = request.user  # dodajemy autora
            post.published_date = timezone.now()
            post.save()  # zapisujemy post
            # robimy przekierowanie do nowo utworzonego posta
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


# Widok ten przypomina widok post_new, jednak nie do końca
def post_edit(request, pk):  # po pierwsze: przekazujemy dodatkowy parametr pk z urls
    # dalej - pobieramy model wpisu Post do edycji za pomocą get_object_or_404(Post, pk=pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # gdy tworzymy formularz, przekazujemy ten wpis pod zmienną instance zarówno w trakcie zapisywania formularza:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # jak i zaraz po otwarciu formularza z wpisem do edycji
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
