from django.urls import path
from . import views

urlpatterns = [
    path('librarian/library/', views.view_library_history, name='view_library_history'),
    path('librarian/students/', views.view_students, name='librarian_students'),
]
