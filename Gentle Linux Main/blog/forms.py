from django import forms


from .models import Post


class CreateForm(forms.ModelForm):
    """Простая форма с тремя полями: автор, описание, текст, загрузка изображения,
    А так же отмена публикации - draft.
    Добавляется во вьюху в виде функции и не только.
    Форму можно сделать во вьюхе, а не этим отдельным файлом."""
    class Meta:
        model = Post
        fields = ['author', 'title', 'image', 'text','draft', 'publish']
