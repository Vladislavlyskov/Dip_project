from django.urls import path
from main_app.views import MainView, one, two

urlpatterns = [
    path('index/', MainView.as_view(), name="form_profile"),
    path('one/', one, name="jne"),
    path('two/', two, name="two"),
]
