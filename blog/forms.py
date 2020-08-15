from django import forms  # importujemy formularze

from .models import Post  # importujemy nasz model

# informujemy Django, że ten formularz jest formularzem modelu (ModelForm), dzięki czemu Django wyręczy nas w pewnych czynnościach


class PostForm(forms.ModelForm):  # PostForm - nazwa naszego formularza

    # klasa Meta, gdzie przekazujemy Django informację o tym, jaki model powinien być wykorzystany do stworzenia tego formularza (model = Post)
    class Meta:
        model = Post
        # wskazujemy, które pole/pola powinny pojawić się w naszym formularzu
        fields = ('title', 'text',)
