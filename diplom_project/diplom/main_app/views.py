from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm, LoginForm, RegisterUserForm, CommentForm
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy


def news(request):
    news = News.objects.all()
    return render(request, 'main_app/main.html', {'news': news})

class NewsDetailView(FormMixin, DetailView):
    model = News
    template_name = 'main_app/datails_view.html'
    context_object_name = 'news'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('news-detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)



def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            print(form.errors)
            error = 'Форма была не верной'
    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main_app/create.html', data)

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('main')
    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_usr = reverse_lazy('main')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data('username')
        password = form.cleaned_data('password')
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class LagoutView(LogoutView):
    pass


