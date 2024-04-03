from django.urls import path
from . import views

urlpatterns = [
    # Add task
    path('addTask/', views.addTask, name='addTask'),
    # Mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as Undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit Feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # Delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]

# urls.py

from django.urls import path
from .views import input_view, search_view

urlpatterns = [
    path('input/', input_view, name='input_view'),
    path('search/', search_view, name='search_view'),
]

# urls.py

