from django.urls import path
from .views import  MainView, SumView


urlpatterns = [
    path('', MainView.as_view()), # Путь который отобразит MainView
    path('sum/', SumView.as_view()), # Путь который отобразит MainView
]