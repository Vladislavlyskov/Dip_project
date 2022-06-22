from django.urls import path
from . import views

urlpatterns = [
    path('main', views.news, name='main'),
    path('register', views.RegisterUserView.as_view(), name='register'),
    path('create', views.create, name='create'),
    path('login', views.LoginView.as_view(), name='login'),
    path('loguot', views.LogoutView.as_view(), name='logout'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
]