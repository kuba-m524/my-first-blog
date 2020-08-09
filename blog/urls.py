from django.urls import path  # importujemy funkcje path
from . import views  # importujemy widoki

urlpatterns = [
    # nasz pierwszy wzorzec adresu URL, dlatego że jest puste to będzie domyślne
    path('', views.post_list, name='post_list'),
]
