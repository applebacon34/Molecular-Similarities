from django.urls import path
from Similarity_search import views

urlpatterns = [
    path("", views.home, name ="home"),
    #path("result", views.todos, name ="result"),
]