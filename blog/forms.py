from django import forms

from .models import Post

# ModelForm - сохранения содержимого формы в модель

# Форма
class PostForm(forms.ModelForm):

# Модель для создания формы
    class Meta:
        model = Post
        fields = ('title', 'text',)