from django.urls import path
from .views import MainPageView, Login, logout_func, RegistrationView, Profile, AddPost





urlpatterns = [
    path('', MainPageView.as_view()),
    path('login/', Login.as_view()),
    path('logout/', logout_func),
    path('registration/', RegistrationView.as_view()),
    path('profile/', Profile.as_view()),
    path('add_post/', AddPost.as_view()),
]