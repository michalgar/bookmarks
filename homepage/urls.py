from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # this will hold the feed
    path('product/<int:book_id>/', views.product, name='product'), # this will hold the borrowing a book functionality
    path('add/', views.add, name='add'),  # this will hold the adding a book to collection functionality
    #path('static/images', views.add, name='add'),  # this will hold the adding a book to collection functionality
]
