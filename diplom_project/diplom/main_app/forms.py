from .models import News, Comments
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'full_text', 'date']

    widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название'
        }),
        "anons": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Анонс'
        }),
        "full_text": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст статьи'
        }),
        "date": DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Дата публикации'
        })
    }

class LoginForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        for field in self.fields:
            self.fields(field).widget.attrs['class'] = 'form-control'

class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields(field).widget.attrs['class'] = 'form-control'
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned.data["password"])
        if commit:
            user.save()
        return user



class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows':5})


