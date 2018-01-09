from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add, name='add'),  # this will hold the adding a book to collection functionality
]