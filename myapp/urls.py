from django.urls import path
from . import views

urlpatterns = [
    #path('', views.hi), # '' Refers to home / index app.
    path('', views.chatbot),
]