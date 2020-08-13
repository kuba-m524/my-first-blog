from django.urls import path  # importujemy funkcje path
from . import views  # importujemy widoki

urlpatterns = [
    # nasz pierwszy wzorzec adresu URL, dlatego że jest puste to będzie domyślne
    path('', views.post_list, name='post_list'),
    # dodajemy kolejny wzorzec
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # Część post/<int:pk>/ określa wzorzec URL:
    # post/ oznacza, że adres URL powinien zaczynać się od słowa post, po którym nastąpi /
    # <int:pk> - ta trudniejsza część oznacza, że Django spodziewa się liczby całkowitej i przekaże jej wartość do widoku jako zmienną pk
    # / - i znów potrzebujemy / zanim skończymy wzorzec URL
    # To wszystko oznacza, że gdy wpiszemy w przeglądarce adres:
    # http://127.0.0.1:8000/post/5/
    # Django zrozumie, że potrzebujemy widoku zwanego post_detail i przekaże informację, że pk jest równe 5 temu widokowi
]
