from django.urls import path
from django.urls import include
from django.urls.resolvers import URLPattern
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]