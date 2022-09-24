from . import views as main_views
from django.urls import path


urlpatterns = [
    path('', main_views.MainPage.as_view(), name = "MainPage"),
]

